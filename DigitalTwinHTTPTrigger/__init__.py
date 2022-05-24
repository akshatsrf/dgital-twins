import os
import json
import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    os.environ['AZURE_CLIENT_ID'] = '3615c5eb-0caf-4e6e-af4b-6e60f1a251a0'
    os.environ['AZURE_TENANT_ID'] = 'e4e34038-ea1f-4882-b6e8-ccd776459ca0'
    os.environ['AZURE_CLIENT_SECRET'] = 'eLS7Q~wdqwkNjFHl_~EvLChpqEGc_6wTqa6tC'
    url = "testtwin.api.wcus.digitaltwins.azure.net"
    
    credential = DefaultAzureCredential()
    service_client = DigitalTwinsClient(url, credential)

    query_expression = 'SELECT * FROM digitaltwins'
    query_result = service_client.query_twins(query_expression)
    dataset = []
    for twin in query_result:
        dataset.append(twin)

    return func.HttpResponse(json.dumps(dataset),mimetype='application/json')