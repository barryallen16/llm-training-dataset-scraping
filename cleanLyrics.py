import json

with open("./tamil2lyrics_allrawlyrics.jsonl", "r", encoding="utf-8") as in_file:
    for line in in_file:
        data = json.loads(line)
        rawLyricsList = data["rawLyrics"]
        cleanEnglishLyrics, cleanTamilLyrics = "", ""
        if len(rawLyricsList) > 0:
            for rawLyrics in rawLyricsList:
                if "english" in rawLyrics:
                    rawEnglishLyrics = rawLyrics[
                        "english"
                    ]  # getting the english lyrics
                    rawEnglishLyrics = [
                        txt for txt in rawEnglishLyrics if txt != " "
                    ]  # removing empty lines
                    index_ = rawEnglishLyrics.index(
                        "Music by :"
                    )  # finding index of music director info line to skip it
                    if (
                        "\n" in rawEnglishLyrics[index_ + 1 :]
                        or " " == rawEnglishLyrics[index_ + 1 :]
                    ):
                        rawEnglishLyrics = rawEnglishLyrics[
                            index_ + 2 :
                        ]  # jump 2 indices to skip music director details
                    else:
                        rawEnglishLyrics = rawEnglishLyrics[
                            index_ + 1 :
                        ]  # one index skip is enough

                    cleanEnglishLyrics = "".join(rawEnglishLyrics)

                elif "tamil" in rawLyrics:
                    rawTamilLyrics = rawLyrics["tamil"]
        if cleanEnglishLyrics:
            print("-" * 5, "English Lyrics", "-" * 5)
            print(cleanEnglishLyrics)
        if cleanTamilLyrics:
            print("-" * 5, "Tamil Lyrics", "-" * 5)
            print(cleanTamilLyrics)
        break
