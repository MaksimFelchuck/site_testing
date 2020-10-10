import sys
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def doctype_check(session, url):
    soup = BeautifulSoup(session.get(url).content, "html.parser")
    if soup.prettify().startswith('<!DOCTYPE html>'):
        return True
    else:
        return False


def main():
    session = HTMLSession()
    if doctype_check(session, sys.argv[1]):
        print(f'Site {sys.argv[1]} starts with <!DOCTYPE html>')
    else:
        print(f'Site {sys.argv[1]} does not start with <!DOCTYPE html>')



if __name__ == '__main__':
    main()