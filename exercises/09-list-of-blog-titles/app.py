import requests

def get_titles():
    # Your code here
    titles = [0]
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response=requests.get(url)
    diccionario = response.json()
    posts = diccionario['posts']
    for post in posts:
        titles.append(post['title'])
    return titles



print(get_titles())