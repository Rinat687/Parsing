import scrapy

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]  # Уберите "https://", оставьте только домен
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Парсим товары на текущей странице
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'url': svet.css('a').attrib['href']
            }

        # Ищем ссылку на следующую страницу
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if next_page:
            # Если ссылка найдена, переходим на следующую страницу
            yield response.follow(next_page, callback=self.parse)