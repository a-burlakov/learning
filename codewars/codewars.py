import os

def codewars(url):

    separators = ['http://', 'https://', 'www.']

    for sep in separators:
        if sep in url:
            url = url.split(sep)[1]

    if '.' in url:
        url = url.split('.')[0]

    return url

print(os.path.exists('tesxt/main.py'))
