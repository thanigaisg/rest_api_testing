import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Send Delete Request
response = requests.delete(url)
print(response.status_code)

assert response.status_code == 204
