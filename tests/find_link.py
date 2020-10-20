"""
find_link - function to find link by link name:

Usage: find_link <url> <link_name>

    <url> - url where find a link
    <link_name> - link_name
"""
from selenium import webdriver
import sys

class TestParser(object):
    def __init__(self, driver, url, link):
        self.driver = driver
        self.url = url
        self.link = link

    def parse(self):
        self.go_to_page()

    def go_to_page(self):
        self.driver.get(self.url)
        self.find_link()

    def find_link(self):
        links = self.driver.find_elements_by_tag_name("a")
        count = 0
        for link in links:
            link = str(link.get_attribute("href"))
            if self.link == ('/' + link.split('/')[-1]):
                count+=1
        print('There {0} link(s) in this url'.format(count))


def main():
    if sys.argv[1] == '-h' or '--help':
        print(__doc__)
        sys.exit(0)
    driver = webdriver.Chrome()
    parser = TestParser(driver, sys.argv[1], sys.argv[2])
    parser.parse()


if __name__ == '__main__':
    main()
