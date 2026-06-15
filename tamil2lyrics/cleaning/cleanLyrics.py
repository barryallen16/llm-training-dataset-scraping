import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
JSONL_DIR = PROJECT_ROOT / "jsonl_files"
JSONL_FILE_PATH = JSONL_DIR / "tamil2lyrics_allrawlyrics.jsonl"

with open(JSONL_FILE_PATH, "r", encoding="utf-8") as in_file:
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
                    cleanEnglishLyrics = "".join(rawEnglishLyrics).strip()

                    if cleanEnglishLyrics:
                        jsonl = {"text" : cleanEnglishLyrics }
                        with open(SCRIPT_DIR/'test.txt', 'w', encoding='utf-8') as out_file:
                            out_file.write(json.dumps(jsonl, ensure_ascii=False) + "\n")
        break
