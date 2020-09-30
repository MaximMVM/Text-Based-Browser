from bs4 import BeautifulSoup
from colorama import Fore, Style
import requests

HEADERS = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}


def get_body(url):
    url = 'https://' + url
    req = requests.get(url, headers=HEADERS)
    return req.text

def parse_body(content):
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    html = BeautifulSoup(content, 'html.parser')
    return html.find_all(tags)

def parse_and_print(url):
    html = get_body(url)
    content = parse_body(html)
    text = ""
    for sent in content:
        if '<a' in str(sent):
             web_string = Fore.BLUE + sent.text + '\n' + Style.RESET_ALL   # add blue color fol hyperlink
        else:
             web_string = (sent.text + '\n')
        text += web_string
    return text




