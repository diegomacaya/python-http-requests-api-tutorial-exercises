import requests

def get_post_tags(post_id):
    # Your code here
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response=requests.get(url)
    diccionario = response.json()
    posts = diccionario['posts']
    tags = {} #diccionario que incluye los tags que tiene un post
    if response.status_code == 200:
        for post in posts:
            if post_id == post['id']:
                tags = post['tags']
                break
            else:
                print("Failed to fetch data from the endpoint")


    return tags



print(get_post_tags(146))