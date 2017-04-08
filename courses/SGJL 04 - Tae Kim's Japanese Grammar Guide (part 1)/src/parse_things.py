import os
import json
import requests


def download_file(url, filename):
    # NOTE the stream=True parameter
    """
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    """

def parse_vocab_thing_info(filename):
    with open(filename, 'r') as f:
        json_data = json.loads(f.read())
        #print(json.dumps(json_data, indent=4, sort_keys=True))
        japanese = json_data["thing"]["columns"]["1"]["possible_answers"]["typing"][0]
        english = json_data["thing"]["columns"]["2"]["accepted"][0]
        pronunciation = json_data["thing"]["columns"]["3"]["possible_answers"]["typing"][0]
        audios = json_data["thing"]["columns"]["4"]["val"]
        audio_url = None
        for audio in audios:
            if audio["url"][-4:] == ".mp3":
                audio_url = "https://d107cgb5lgj7br.cloudfront.net/{}".format(audio["url"])
                break
        else:
            audio_url = "https://d107cgb5lgj7br.cloudfront.net/{}".format(json_data["thing"]["columns"]["4"]["val"][0]["url"])
        print("{}\t{}\t{}\t{}".format(japanese, english, pronunciation, audio_url))
        #print("")
        return (japanese, english, pronunciation, audio_url)

def save_vocab_levels():
    vocab_directories = [
        "level_002",
        "level_005",
        "level_009",
        "level_013",
        "level_017",
        "level_020",
        "level_023",
        "level_028",
        "level_031",
        "level_035",
        "level_041",
    ]
    level_counter = 1
    for directory in vocab_directories:
        with open("deck_{:02}_vocab.txt".format(level_counter), 'w') as f:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file[-5:] == ".json":
                        sort_order = file.split("_")[0].lstrip("0")
                        japanese, english, pronunciation, audio_url = parse_vocab_thing_info("{}/{}".format(root, file))
                        downloaded_filename = "SGJL04_{}.mp3".format(japanese)
                        download_file(audio_url, downloaded_filename)
                        f.write("{},{},{},{},[sound:{}]\n".format(sort_order, japanese, english, pronunciation, downloaded_filename))
        level_counter += 1


def parse_grammar_thing_info(filename):
    with open(filename, 'r') as f:
        json_data = json.loads(f.read())
        #print(json.dumps(json_data, indent=4, sort_keys=True))
        japanese = json_data["thing"]["columns"]["1"]["possible_answers"]["typing"][0]
        pronunciation = json_data["thing"]["columns"]["2"]["possible_answers"]["typing"][0]
        english = json_data["thing"]["columns"]["3"]["accepted"][0]
        audios = json_data["thing"]["columns"]["4"]["val"]
        audio_url = None
        for audio in audios:
            if audio["url"][-4:] == ".mp3":
                audio_url = "https://d107cgb5lgj7br.cloudfront.net/{}".format(audio["url"])
                break
        else:
            audio_url = "https://d107cgb5lgj7br.cloudfront.net/{}".format(json_data["thing"]["columns"]["4"]["val"][0]["url"])
        print("{}\t{}\t{}\t{}".format(japanese, english, pronunciation, audio_url))
        #print("")
        return (japanese, english, pronunciation, audio_url)


def save_grammar_levels():
    grammar_directories = [
        "level_004",
        "level_008",
        "level_012",
        "level_016",
        "level_019",
        "level_022",
        "level_027",
        "level_030",
        "level_034",
        "level_040",
        "level_044",
    ]
    level_counter = 1
    for directory in grammar_directories:
        with open("deck_{:02}_grammar.txt".format(level_counter), 'w') as f:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file[-5:] == ".json":
                        sort_order = file.split("_")[0].lstrip("0")
                        downloaded_filename = "SGJL04_sentence_{}.mp3".format(sort_order)
                        japanese, english, pronunciation, audio_url = parse_grammar_thing_info("{}/{}".format(root, file))
                        download_file(audio_url, downloaded_filename)
                        f.write("{},{},{},{},[sound:{}]\n".format(sort_order, japanese, english, pronunciation, downloaded_filename))
        level_counter += 1

def main():
    save_vocab_levels()
    save_grammar_levels()

if __name__ == "__main__":
    main()