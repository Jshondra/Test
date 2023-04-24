import os
import urllib.error
from urllib.request import urlopen

try:
    os.mkdir('./src')
except FileExistsError:
    pass


def get_urls() -> None:
    # lst = [s for s in input().split()]
    lst = ['https://docs.python.org/3/library/urllib.request.htm',
           'https://docs.python.org/3/library/urllib.request.html']
    i = 1
    for elem in lst:
        try:
            page = urlopen(elem)
        except urllib.error.HTTPError:
            print(f'HTTP Error:{elem}')
            continue
        with open(f"src/test_{i}.html", "wb") as fh:
            fh.write(page.read())
        i += 1


get_urls()