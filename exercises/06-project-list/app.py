import requests

# Your code here
url= 'https://assets.breatheco.de/apis/fake/sample/project_list.php'

response=requests.get(url)
print(response.text)

diccionario = response.json()

print(diccionario[1]["name"]) # imprimir el segundo elemento de la lista, se pone el 1 en parentesis cuadrado
