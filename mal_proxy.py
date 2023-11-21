from bs4 import BeautifulSoup
import time
import requests as re

start = time.time()

try:
    params = {'type': 'airing'}
    response = re.get('https://myanimelist.net/topanime.php', params=params)
except re.RequestException as e:
    print(f"Error: {e}")

soup = BeautifulSoup(response.text, 'html.parser')
ranking_containers = soup.find_all('tr', class_="ranking-list")
anchor_tags = [rc.find('a') for rc in ranking_containers]
anime_names = [at['href'].split("/")[5] for at in anchor_tags]

assert(len(anime_names) == 50)

end = time.time()
print(f'Total time elapsed in seconds: {end - start}')