import bs4
import requests
from fake_useragent import UserAgent




# фиктивные заголовки для обхода защиты сайта от парсинга 
HEADERS = {
    'User-Agent': UserAgent().random
    }

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# адрес сайта для парсинга
base_url = "https://habr.com"
url = base_url + '/ru/all/'

# отправляем запрос к сайту
response = requests.get(url, headers=HEADERS)
# получаем ответ и применяем метод text выходит весь запутанный код страницы в HTML
text = response.text

# превращаем сложный код в красивый суп
soup = bs4.BeautifulSoup(text, features="html.parser")

# узнав в каком контейнере находится нужная информайция, начинаем к ней копать через find\find_all
articles = soup.find_all(class_="tm-articles-list__item")

for article in articles:
    headline = article.find(class_="tm-article-snippet__title-link").find('span').text
    print(111111111111111111, headline)

    preview_info = article.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-2").find('p')
    print(333333333333333333, preview_info)
    # hubs = [hub.text.strip() for hub in hubs]
    # for hub in HUBS:
    #     title = article.find('h2').find('span').text
    #     href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    #     link = base_url+ href
    #     print(f"{title} ---> {link}")