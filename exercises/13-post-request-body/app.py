import requests
content = {
    "id": 2323,
    "title": "Very big project"
}
headers = {'Content-type': 'application.json'}
response = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php",json=content,headers=headers)
print(response.text)