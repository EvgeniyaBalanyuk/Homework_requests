import requests
import json

if __name__ == '__main__':
    heroes = ['Hulk', 'Captain america', 'Thanos']
    intelligence = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
    url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

    for hero in heroes:
        hero_dict = json.loads(requests.get(url + hero).content)
        intelligence[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

    print(intelligence)