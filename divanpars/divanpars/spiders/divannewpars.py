import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css("div._Ud0k")
        for divan in divans:
            yield {
                "name": divan.css("div.lsooF span::text").get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': divan.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                # Атрибуты — это настройки тегов
                'url': divan.css('a').attrib['href']
            }
