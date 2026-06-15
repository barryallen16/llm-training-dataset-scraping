import scrapy
import json

class getAllSongLinks(scrapy.Spider):
    name = "getsonglinks"
    start_urls=[]
    with open('./tamil2lyrics_movielinks.jsonl', 'r', encoding='utf-8') as in_file:
        for line in in_file:
            data = json.loads(line)
            start_urls += data["links"]
    
    def parse(self, response):
        all_links = response.css('.list-line .col-lg-6 a[href]::attr(href)').getall()
        unique_links = set(all_links)
        yield {'links': unique_links}
