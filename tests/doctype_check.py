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
# FILE: doctype_check.py
# Author: Maxim Felchuck
#
##############################################################################
"""
doctype_check - function to check url starts with <!DOCTYPE html>:

Usage: doctype_check <url>

    <url> - url where checking doctype
"""
import sys
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def doctype_check(session, url):
    """
    check url starts with <!DOCTYPE html>
    """
    soup = BeautifulSoup(session.get(url).content, "html.parser")
    if soup.prettify().startswith('<!DOCTYPE html>'):
        return True
    return False


def main():
    """
    doctype_check - function to check url starts with <!DOCTYPE html>:

    Usage: doctype_check <url>

        <url> - url where checking doctype
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    session = HTMLSession()
    if doctype_check(session, sys.argv[1]):
        print(f'Site {sys.argv[1]} starts with <!DOCTYPE html>')
    else:
        print(f'Site {sys.argv[1]} doesnt start with <!DOCTYPE html>')


if __name__ == '__main__':
    main()
