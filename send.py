
from csv import excel
from http.client import CONFLICT
import json
from lib2to3.pgen2 import token
from urllib import response
import  requests
from requests.auth import HTTPBasicAuth
from decouple import config

counter = 0


def request_to_client(url: str, data):
    try:
        response = requests.post(
            url,

            headers = {
                
                'Authorization': f"Token {data['token']}"
            },


            data = data,
            
            )

        
        return response
    except Exception as e:
        print(e)


# TODO: Read json file 
with open('payload.json') as payload:
    data = json.load(payload)


while counter < len(data):
    try:
        response = request_to_client(f"{config('HOST')}:{config('PORT')}/{config('BASE_URL')}/{config('END_POINT')}/{data[counter]['patient_id']}",data[counter])
        print(response.json())
        counter += 1
        print(counter)
    except Exception as e:
        print(e)