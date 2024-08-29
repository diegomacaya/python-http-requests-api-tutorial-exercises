import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)

diccionario = response.json()

print(diccionario)

print(f'Current time: '+str(diccionario['hours'])+' h '+str(diccionario['minutes'])+' min '+str(diccionario['seconds'])+' sec')