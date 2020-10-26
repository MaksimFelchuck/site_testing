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
# FILE: js_errors_check.py
# Author: Maxim Felchuck
#
##############################################################################
"""
js_errors_check - function to check there any js errors on the site:

Usage: js_errors_check <url>

    <url> - url where checking js errors
"""
import sys
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def check_browser_errors(driver):
    """
    driver - driver to interface with the chosen browser
    return: found errors
    """
    try:
        browser_logs = driver.get_log('browser')
    except (ValueError, WebDriverException) as error:
        logging.debug("Could not get browser logs for driver %s due to exception: %s",
                      driver, error)

        return []

    errors = []
    for entry in browser_logs:
        if entry['level'] == 'SEVERE':
            errors.append(entry)
    return errors


def main():
    """
    js_errors_check - function to check there any js errors on the site:

    Usage: js_errors_check <url>

        <url> - url where checking js errors
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    driver = webdriver.Chrome()
    driver.get(sys.argv[1])
    errors = check_browser_errors(driver)
    if len(errors) > 0:
        print(*errors, sep='\n')
    else:
        print('No js errors')


if __name__ == '__main__':
    main()
