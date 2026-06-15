import scrapy
class Tamil2LyricSpider(scrapy.Spider):
    name = "tamil2lyrics"
    start_urls =["https://www.tamil2lyrics.com/movie/"]

    def parse(self, response):        
        all_links = response.css('.list-line a[href]::attr(href)').getall()
        unique_links = set(all_links)
        yield {'links': unique_links}

        next_page = response.xpath( "//a[text()='Next']").css('::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)