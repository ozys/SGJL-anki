from lxml import html
import os.path
import requests
from bs4 import BeautifulSoup


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
            for tag in pool.findAll('div', attrs={'class':'col_a col text'}):
                kanji = html.fromstring(tag.next.next).text
                keyword = html.fromstring(tag.findNextSibling().next.next).text
                things.append((kanji, keyword))
            levels.append(things)

        level_counter = 1
        sort_order = 1
        for level in levels:
            with open("{}.txt".format(level_counter), 'w') as f:
                for thing in level:
                    kanji = thing[0]
                    keyword = thing[1]
                    print(kanji + "\t" + keyword)
                    f.write("{},{},{}\n".format(sort_order, kanji, keyword))
                    sort_order += 1
            level_counter += 1

def main():
    get_course(1091255)

if __name__ == "__main__":
    main()
