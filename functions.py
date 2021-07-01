import requests
import time
from bs4 import BeautifulSoup

def collect_all_links():
    """Функция возвращает список сформированных ссылок в формате https://you-anime.ru/characters?page=x
    где x от 1 до 2391"""
    target = 'https://you-anime.ru/characters?page='
    urls = []
    for i in range(1,2392,1):
        urls.append(f'{target}{i}')
    print('\033[32m Ссылки готовы')
    return urls

def collect_all_characters_links(urls):
    """функция принимает список ссылок, на каждой из которых находит ссылки на конкретных персонажей, возвращает их в качестве списка"""
    character_urls = []
    for url in urls:
        res = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(res.text, 'lxml')
        print(f'\033[32m Парсим страницу {url}')
        part_of_url = [url for url in soup.find_all(attrs = {'class' : 'inner'})]
        for i in part_of_url:
           for a in i.find_all('a'):
               if 'characters' in a.get('href'):
                   character_urls.append(f"https://you-anime.ru{a.get('href')}")
    return character_urls

def get_all_characters_names(character_page):
    """Функция на каждой странице персонажа находит его имя, возвращает список всех имен"""
    res = requests.get(character_page)
    time.sleep(1)
    soup = BeautifulSoup(res.text, 'lxml')
    names = [name.text for name in soup.find_all('dd')]
    return names
