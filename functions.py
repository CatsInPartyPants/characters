import requests
import time
from bs4 import BeautifulSoup

def collect_all_links():
    target = 'https://you-anime.ru/characters?page='
    urls = []
    for i in range(1,2,1):
        urls.append(f'{target}{i}')
    print('\033[32m Ссылки готовы')
    return urls

def collect_all_characters_links(urls):
    character_urls = []
    for url in urls:
        res = requests.get(url)
        #time.sleep(1)
        soup = BeautifulSoup(res.text, 'lxml')
        print(f'\033[32m Парсим страницу {url}')
        part_of_url = [url for url in soup.find_all(attrs = {'class' : 'inner'})]
        for i in part_of_url:
           for a in i.find_all('a'):
               if 'characters' in a.get('href'):
                   character_urls.append(f"https://you-anime.ru{a.get('href')}")
    return character_urls
        
        
def get_all_characters_names(character_page):
    res = requests.get(character_page)
    soup = BeautifulSoup(res.text, 'lxml')
    names = [name.text for name in soup.find_all('dd')]
    return names


#attrs = {'class' : 'meta col-sm-24'}





