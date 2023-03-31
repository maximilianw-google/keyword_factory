import functions_framework
from translator import Translator

@functions_framework.http
def translate(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        Should contain a JSON with with a list of KWs to categorize
    Returns:
        A Response object. A dict with each KW, it's full category path 
        and it's confidence score.
    """
    request_json = request.get_json()
    kws = request_json['kws']
    results = Translator().classify_list(kws)
    return results