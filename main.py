from functions import *

def start():
    data_for_record = []
    urls = collect_all_links()
    character_pages = collect_all_characters_links(urls)
    for i in character_pages:
        name = get_all_characters_names(i)
        try:
            data_for_record.append(f'{name[0]} xx {name[1]} xx {name[2]}')
        except:
            pass
    print(data_for_record)

if __name__ == "__main__":
    start()