import requests
import os
import pandas as pd
import time

BASE_URL = "https://api.dune.com/api/v1/"
API_KEY = os.environ.get("DUNE_API_KEY")
HEADER = {"x-dune-api-key" : API_KEY}

def make_api_url(module, action, ID):
    """
    We shall use this function to generate a URL to call the API.
    """
    
    url = BASE_URL + module + "/" + ID + "/" + action
    
    return url

def execute_query(query_id):
    """
    Takes in the query ID.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """
    
    url = make_api_url("query", "execute", query_id)
    response = requests.post(url, headers=HEADER)
    execution_id = response.json()['execution_id']
    
    return execution_id


def get_query_status(execution_id):
    """
    Takes in an execution ID.
    Fetches the status of query execution using the API
    Returns the status response object
    """
    
    url = make_api_url("execution", "status", execution_id)
    response = requests.get(url, headers=HEADER)
    
    return response


def get_query_results(execution_id):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """
    
    url = make_api_url("execution", "results", execution_id)
    response = requests.get(url, headers=HEADER)
    
    return response


def cancel_query_execution(execution_id):
    """
    Takes in an execution ID.
    Cancels the ongoing execution of the query.
    Returns the response object.
    """
    
    url = make_api_url("execution", "cancel", execution_id)
    response = requests.get(url, headers=HEADER)
    
    return response


execution_id = execute_query("1534184")

result = False
while not result:
    response = get_query_results(execution_id).json()
    result = response.get('result',False)
    if not result:
        time.sleep(1)

df = pd.DataFrame(response.get("result").get("rows"))
df.to_parquet("ens.parquet")