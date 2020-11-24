##############################################################################
#
# Copyright (c) 2020 TomskSoft LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# FILE: check_link.py
# Author: Maxim Felchuck
#
##############################################################################
"""
check_link - function to check links works:

Usage: check_link <url> [links]

    <url> - url where checking links
    [links] - links to check. check link1 -> check link2 -> ...
"""
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options

class TestParser():
    """
    driver - driver to interface with the chosen browser
    url - sites url
    links - links to check
    """
    def __init__(self, driver, url, links):
        self.driver = driver
        self.url = url
        self.links = links

    def parse(self):
        """
        starting parse
        """
        self.go_to_page()

    def go_to_page(self):
        """
        open a page
        """
        try:
            self.driver.get(self.url)
        except WebDriverException as error:
            print(error)

        for link in self.links:
            self._check_link(link)

    def _check_link(self, link):
        try:
            link = self.driver.find_element_by_link_text(link)
            link.click()
            time.sleep(5)
        except NoSuchElementException:
            print(f'link "{link}" not found')


def main():
    """
    check_link - function to check links works:

    Usage: check_link <url> [links]

        <url> - url where checking links
        [links] - links to check. check link1 -> check link2 -> ...
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("chromedriver", options=chrome_options)
    args = []
    for arg in range(2, len(sys.argv)):
        args.append(sys.argv[arg])
    parser = TestParser(driver, sys.argv[1], args)
    parser.parse()


if __name__ == '__main__':
    main()
