import requests
from bs4 import BeautifulSoup

class DivanLightingSpider:
    def __init__(self):
        self.base_url = "https://www.divan.ru"
        self.lighting_url = "/catalog/svetilniki/"

    def fetch_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = []

        # Assuming the items are within a specific class or tag
        for item in soup.select('.product-card'):  # Adjust the selector as needed
            name = item.select_one('.product-card__title').get_text(strip=True)
            price = item.select_one('.product-card__price').get_text(strip=True)
            link = self.base_url + item.select_one('a')['href']
            items.append({'name': name, 'price': price, 'link': link})

        return items

    def run(self):
        url = self.base_url + self.lighting_url
        html = self.fetch_page(url)
        if html:
            items = self.parse_html(html)
            for item in items:
                print(f"Name: {item['name']}, Price: {item['price']}, Link: {item['link']}")

# Run the spider
spider = DivanLightingSpider()
spider.run()
