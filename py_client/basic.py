import requests

endpoint = "http://127.0.0.1:8000/api/add"

response = requests.post(endpoint, json={'content': "this is a test"})
# print(response.status_code)
print(response.json())
