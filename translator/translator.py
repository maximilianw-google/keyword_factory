# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math
import logging
from alive_progress import alive_it
from google.cloud import translate_v2

SCOPES = ['https://www.googleapis.com/auth/cloud-translation']
# Maximum number of segments accepted by the translate API
TRANSLATE_BATCH_SIZE = 128

class Translator():
  """Class with utils using Google Cloud Translate API."""

  def __init__(self) -> None:
    self.client = translate_v2.Client()

  def translate_list(
      self,
      batch_text: list[str],
      target_lang: str,
      source_lang: str = 'en'
  ) -> list[str]:
    """Returns the translated text."""

    num_batches = math.ceil(len(batch_text) / TRANSLATE_BATCH_SIZE)
    progress_bar = alive_it(
        range(0, num_batches),
        stats=False,
        title='Translating Product Batch Text',
    )

    responses = []
    for batch_idx in progress_bar:
        batch_start = batch_idx * TRANSLATE_BATCH_SIZE
        batch_end = batch_start + TRANSLATE_BATCH_SIZE
        batch = batch_text[batch_start:batch_end]
        response = self.client.translate(
            batch,
            target_language=target_lang,
            source_language=source_lang,
            format_='text',
        )
        logging.info(response)
        responses.extend([t['translatedText'] for t in response])
    return responses

    

