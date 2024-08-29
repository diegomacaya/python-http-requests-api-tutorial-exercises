import requests

url= 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'

response=requests.get(url)
#print(response.text)

diccionario = response.json()

print(diccionario['posts'][0]['author']['name'])