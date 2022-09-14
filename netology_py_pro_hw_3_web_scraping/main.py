import bs4
import requests
from fake_useragent import UserAgent

# Проверка на наличие в тексте ключевых слов
def checking_availab(text: str, keywords: list) -> bool: 
    text = text.lower()
    for word in keywords:
        word = word.lower()
        if word in text:
            return True
    else: 
        return False


# фиктивные заголовки для обхода защиты сайта от парсинга 
HEADERS = {
    'User-Agent': UserAgent().random
    }

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# адрес сайта для парсинга
base_url = "https://habr.com"
url = base_url + '/ru/all/'

if __name__ == '__main__':
    # отправляем запрос к сайту
    response = requests.get(url, headers=HEADERS)
    # получаем ответ и применяем метод text выходит весь запутанный код страницы в HTML
    text = response.text

    # превращаем сложный код в красивый суп
    soup = bs4.BeautifulSoup(text, features="html.parser")

    # через F12 и браузер узнав в каком контейнере находится нужная информация, начинаем к ней копать через find\find_all, получаем все статьи в списке
    articles = soup.find_all(class_="tm-articles-list__item")

    for article in articles:
        # получение всего текста из контейнера и удаление лишних пробелов
        all_text = article.get_text(strip=True)

        if checking_availab(all_text, KEYWORDS):
            # получение даты создания статьи
            date_article = article.time['title']

            # получение заголовка статьи
            title_article = article.find(class_="tm-article-snippet__title-link").find('span').text

            # получение cсылки на статью
            link_article = article.h2.a['href']

            print(f'{date_article} "{title_article}" ---> {base_url+link_article}')

        else:
            print('- нет совпадений по ключевым словам')