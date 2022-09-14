import bs4
import requests
from fake_useragent import UserAgent

# Проверка на наличие в тексте ключевых слов
def checking_availab(url: str, keywords: list) -> bool: 

    response = requests.get(url)
    text = response.text

    soup = bs4.BeautifulSoup(text, features="html.parser")

    # получение всего текста по ссылке и удаление лишних пробелов
    all_text = soup.find(id='post-content-body').get_text(strip=True)
    all_text = all_text.lower()

    for word in keywords:
        word = word.lower()
        if word in all_text:
            return True
    else: 
        return False


HEADERS = {
    'User-Agent': UserAgent().random
    }

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

base_url = "https://habr.com"
url = base_url + '/ru/all/'


if __name__ == '__main__':
    response = requests.get(url, headers=HEADERS)
    text = response.text

    soup = bs4.BeautifulSoup(text, features="html.parser")

    articles = soup.find_all(class_="tm-articles-list__item")

    for article in articles:
        # получение cсылки на статью
        full_link_article = base_url + article.h2.a['href']

        if checking_availab(full_link_article, KEYWORDS):
            date_article = article.time['title']

            title_article = article.find(class_="tm-article-snippet__title-link").find('span').text

            print(f'{date_article} "{title_article}" ---> {full_link_article}')

        else:
            print('- нет совпадений по ключевым словам')