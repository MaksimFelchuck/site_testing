import time

from selenium import webdriver
import sys
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class TestParser(object):
    def __init__(self, driver, url, links):
        self.driver = driver
        self.url = url
        self.links = links

    def parse(self):
        self.go_to_page()

    def go_to_page(self):
        try:
            self.driver.get(self.url)
        except WebDriverException as error:
            print(error)

        for link in self.links:
            self.check_link(link)

    def check_link(self, link):
        try:
            link = self.driver.find_element_by_link_text(link)
            link.click()
            time.sleep(5)
        except NoSuchElementException:
            print(f'link "{link}" not found')


def main():
    driver = webdriver.Chrome()
    args = []
    for arg in range(2, len(sys.argv)):
        args.append(sys.argv[arg])
    parser = TestParser(driver, sys.argv[1], args)
    parser.parse()


if __name__ == '__main__':
    main()