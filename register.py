#In this code we will call our api to register a user...You can do it via web also!!
#This is a working code... we will give you url once you reached us!

import requests
import json

# API URL where the PHP file is hosted
API_URL = ''  
def signup():
    data = {
        'api_key': '1ebeb745196d6995',
        'action': 'signup',
        'username': 'testus1er',
        'password': 'password123',
        'email': 'test@e1xample.com',
        'firstname': 'Test' # Optional
    }
    response = requests.post(API_URL, json=data)
    print("Raw Response:", response.text)  # Print raw response to debug
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("JSON Decode Error:", e)

# Example Check Secret Request

# Call the function you want to test
signup()

