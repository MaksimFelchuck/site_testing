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
# FILE: find_link.py
# Author: Maxim Felchuck
#
##############################################################################
"""
find_link - function to find link by link name:

Usage: find_link <url> <link_name>

    <url> - url where find a link
    <link_name> - link_name
"""
import sys
from selenium import webdriver


class TestParser():
    """
    driver - driver to interface with the chosen browser
    url - sites url
    links - links to find
    """
    def __init__(self, driver, url, link):
        self.driver = driver
        self.url = url
        self.link = link

    def parse(self):
        """
        starting parse
        """
        self.go_to_page()

    def go_to_page(self):
        """
        open a page
        """
        self.driver.get(self.url)
        count = self.find_link()
        print('There {0} link(s) in this url'.format(count))

    def find_link(self):
        """
        function to find all link on url
        return: count of found links
        """
        links = self.driver.find_elements_by_tag_name("a")
        count = 0
        for link in links:
            link = str(link.get_attribute("href"))
            if self.link == ('/' + link.split('/')[-1]):
                count += 1
        return count


def main():
    """
    find_link - function to find link by link name:

    Usage: find_link <url> <link_name>

        <url> - url where find a link
        <link_name> - link_name
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    driver = webdriver.Chrome()
    parser = TestParser(driver, sys.argv[1], sys.argv[2])
    parser.parse()


if __name__ == '__main__':
    main()
