from functions import *

def start():
    data_for_record = []
    urls = collect_all_links()
    character_pages = collect_all_characters_links(urls)
    for i in character_pages:
        name = get_all_characters_names(i)
        try:
            data_for_record.append(f'Русское имя: {name[0]}\t Японское имя: {name[1]}\t Другое: {name[2]}')
        except:
            pass
    f = open('anime_characters.txt', 'w')
    for name in data_for_record:
        f.write(name + '\n')

if __name__ == "__main__":
    start()
