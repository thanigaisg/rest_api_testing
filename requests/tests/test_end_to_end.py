import requests
import json
import jsonpath


def test_add_new_data():
    # API URL
    url = "https://thetestingworldapi.com/api/studentsDetails"

    # Read Input JSON file
    file = open("create_student.json", "r")
    print(file)
    request_json = json.loads(file.read())

    # Make POST request with json input body
    response = requests.post(url, data=request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])