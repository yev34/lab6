import requests
from bs4 import BeautifulSoup


def process_page(url: str):
    response = requests.get(url)

    parser = BeautifulSoup(response.text, "html.parser")

    words = parser.get_text().split(' ')

    words = [word.replace('\n', '') for word in words]

    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    tag_frequency = {}
    for tag in parser.find_all():
        tag_frequency[tag.name] = tag_frequency.get(tag.name, 0) + 1

    return word_frequency, tag_frequency


words, tags = process_page('https://time.com/6107134/who-sago-covid-19-origins/')

print(f'Частота слів: {words}')
print(f'Частота тегів: {tags}')
print(f'Кількість картинок: {tags.get("img", 0)}')
print(f'Кількість посилань: {tags.get("a", 0)}')
