import scrapy
import json


class getAllLyrics(scrapy.Spider):
    name = "getlyrics"
    start_urls = []
    with open("./tamil2lyrics_songlinks.jsonl", "r", encoding="utf-8") as in_file:
        for line in in_file:
            data = json.loads(line)
            start_urls += data["links"]

    def parse(self, response):
        container = response.css(".lyrics-title")
        lyricsData = {
            "lyricist": container.css("h3 a::text").get(),
            "songName": container.css(".pull-left h1::text").get(),
            "movieName": container.css(".pull-left a::text").get(),
            "rawLyrics": [],
        }

        englishContainer = response.css("#English")
        if englishContainer:
            englishLyrics = englishContainer.css("::text").getall()
            if englishLyrics:
                lyricsData["rawLyrics"].append({"english": englishLyrics})
        tamilContainer = response.css("#Tamil")
        if tamilContainer:
            tamilLyrics = tamilContainer.css("::text").getall()
            if tamilLyrics:
                lyricsData["rawLyrics"].append({"tamil": tamilLyrics})

        yield lyricsData