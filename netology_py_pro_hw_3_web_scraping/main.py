import bs4
import requests
from fake_useragent import UserAgent

HUBS = ['Физика', 'Дизайн', 'ty']

HEADERS = {
    'User-Agent': UserAgent().random
    }

base_url = "https://habr.com"
url = base_url + '/ru/all/'


print(HEADERS)


response = requests.get(url, headers=HEADERS)
text = response.text


soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")

for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.strip() for hub in hubs]
    for hub in HUBS:
        title = article.find('h2').find('span').text
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = base_url+ href
        print(f"{title} ---> {link}")