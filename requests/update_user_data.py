import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read Input JSON file
file = open("create_user.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body
response = requests.put(url, data=request_json)
print(response.content)

assert response.status_code == 200

# Parse response to JSON format
response_json = json.loads(response.text)
updated_time = jsonpath.jsonpath(response_json, "updatedAt")
print(updated_time[0])