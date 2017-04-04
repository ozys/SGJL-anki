from lxml import html
import os.path
import requests
from bs4 import BeautifulSoup
import json


def download_file(url, filename):
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


def get_thing_info(thing_id):
    r = requests.get("https://www.memrise.com/api/thing/get/?thing_id={}".format(thing_id))
    json_data = json.loads(r.text)
    #print(json.dumps(json_data, indent=4, sort_keys=True))
    #print("")
    hiragana = json_data["thing"]["columns"]["2"]["possible_answers"]["typing"][0]
    katakana = json_data["thing"]["columns"]["1"]["possible_answers"]["typing"][0]
    audio_url = "https://d107cgb5lgj7br.cloudfront.net/{}".format(json_data["thing"]["columns"]["7"]["val"][0]["url"])
    #print("{}\t{}\t{}".format(hiragana, katakana, audio_url))
    return (hiragana, katakana, audio_url)


def get_course(course_id, fileName=False):
    course_id = str(course_id)
    if not fileName:
        fileName = course_id

    # Start a request session
    with requests.Session() as s:
        # get HTML source of course main page
        rc = s.get('http://www.memrise.com/course/' + course_id)

        # Parse it for python and extract each level URL
        pool = BeautifulSoup(rc.content, 'lxml')
        level_urls = []
        for tag in pool.findAll(attrs={'class':'level clearfix'}):
            level_urls.append(tag['href'])

        levels = []  # List of Memrise objects (they call them "things")

        for url in level_urls:
            rc = s.get('http://www.memrise.com/' + url)
            pool = BeautifulSoup(rc.content, 'lxml')
            things = []
            for tag in pool.findAll('div'):
                if tag.get('data-thing-id'):
                    things.append(tag.get('data-thing-id'))
            levels.append(things)

        output_file = os.path.join('{}.txt'.format(fileName))
        level_counter = 1
        sort_order = 1
        for level in levels:
            with open("{}.txt".format(level_counter), 'w') as f:
                for thing in level:
                    hiragana, katakana, audio_url = get_thing_info(thing)
                    print(hiragana + "\t" + katakana + "\t" + audio_url)
                    downloaded_filename = "SGJL02_{}.mp3".format(katakana)
                    download_file(audio_url, downloaded_filename)
                    f.write("{},{},{},[sound:{}]\n".format(sort_order, hiragana, katakana, downloaded_filename))
                    sort_order += 1
            level_counter += 1


def main():
    get_course(1100073)

if __name__ == "__main__":
    main()
