import requests

url= 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

response=requests.get(url)
#print(response.text)

diccionario = response.json()

print(diccionario[-1]['images'][-1]) #ultimo elemento de la lista de imagenes