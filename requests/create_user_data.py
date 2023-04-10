import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read Input JSON file
file = open("create_user.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body
response = requests.post(url, data=request_json)
print(response.content)

assert response.status_code == 201

# Fetch headers from Response
print(response.headers)
print(response.headers.get('Report-To'))

# Parse response to JSON format
response_json = json.loads(response.text)
print(response_json)

# Pick ID using JSON Path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
