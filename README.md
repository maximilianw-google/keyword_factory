# Keyword Factory

## Prerequisites

1. [A Google Ads Developer token](https://developers.google.com/google-ads/api/docs/first-call/dev-token#:~:text=A%20developer%20token%20from%20Google,SETTINGS%20%3E%20SETUP%20%3E%20API%20Center.)

1. A new GCP project with billing attached

1. Create OAuth2 Credentials of type **Web** and refresh token with scopes **"Google Ads API"** and **"Google Sheets API"**. Follow instructions in [this video](https://www.youtube.com/watch?v=KFICa7Ngzng)

1. [Enable Google ads API](https://developers.google.com/google-ads/api/docs/first-call/oauth-cloud-project#enable_the_in_your_project)

1. Enable Sheets API


## Installation

1. Click the big blue button to deploy:
   
   [![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

1. Choose your designated GCP project and desired region.

1. Once installation is finished you will recieve your tool's URL. Save it.


## Usage

1. If it's your first time using this tool - fill in your credentials in the "Authentication" tab.

1. Choose if you want to run the analysis on all accounts under your MCC, or on selected accounts.

1. Choose your date range and search term thresholds, and click "RUN"

1. A link to a results spreadsheet will be presented once the run is complete


## Disclaimer
This is not an officially supported Google product.