import requests

url = "http://127.0.0.1:8000/api/auth"

response = requests.post(url, data={"username": "choiseungmin", "password": "1234"})

print(response.text)
myToken = response.text

headers = {"Authorization": "Token 6722badeeedeb2d3800745e6b7ae85dcfe9b69c7"}
response = requests.get('http://127.0.0.1:8000/api/student_list', headers=headers)
print(response.text)