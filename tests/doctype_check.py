"""
doctype_check - function to check url starts with <!DOCTYPE html>:

Usage: doctype_check <url>

    <url> - url where checking doctype
"""
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
    if sys.argv[1] == '-h' or '--help':
        print(__doc__)
        sys.exit(0)
    session = HTMLSession()
    if doctype_check(session, sys.argv[1]):
        print(f'Site {sys.argv[1]} starts with <!DOCTYPE html>')
    else:
        print(f'Site {sys.argv[1]} doesnt start with <!DOCTYPE html>')



if __name__ == '__main__':
    main()