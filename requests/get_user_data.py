import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
print(response)

# Display Response Content
print(response.content)
print(response.headers)

# Parse response content into the JSON format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using JSON Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])

assert pages[0] == 2

first_names = jsonpath.jsonpath(json_response, 'data')
print(first_names)
print(first_names[0][0]['first_name'])