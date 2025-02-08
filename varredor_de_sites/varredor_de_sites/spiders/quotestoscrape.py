import scrapy
#CamelCase

class QuotesToScrapeSpider(scrapy.Spider):
    #Identidade;
    name = 'frasebot'
    #REquest;
    def start_requests(self):
       urls = ['https://quotes.toscrape.com']

       for url in urls:
           yield scrapy.Request(url=url, callback=self.parse)
    #Response;
    def parse(self, response):
        # Aui é onde você deve processar o que foi encontrado da response
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)