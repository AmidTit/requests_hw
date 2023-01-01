import requests

def superhero_request():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    heroes = response.json()
    heroes_int = {}
    for hero in heroes:
        if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
            heroes_int[hero['name']] = hero['powerstats']['intelligence']
    print(max(heroes_int, key=heroes_int.get))


if __name__ == '__main__':
    superhero_request()