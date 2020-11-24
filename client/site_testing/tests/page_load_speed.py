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
# FILE: page_load_speed.py
# Author: Maxim Felchuck
#
##############################################################################
"""
page_load_speed - function to check site load speed:

Usage: page_load_speed <url>

    <url> - url where checking load speed
"""
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def page_load_time(link):
    """
    link: site link
    return: backend_performance_calc, frontend_performance_calc
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("chromedriver", options=chrome_options)
    driver.get(link)

    navigation_start = driver.execute_script("return window.performance.timing.navigationStart")
    response_start = driver.execute_script("return window.performance.timing.responseStart")
    time.sleep(5)
    dom_complete = driver.execute_script("return window.performance.timing.domComplete")
    backend_performance_calc = response_start - navigation_start
    frontend_performance_calc = dom_complete - response_start
    driver.quit()
    return backend_performance_calc, frontend_performance_calc


def main():
    """
    page_load_speed - function to check site load speed:

    Usage: page_load_speed <url>

        <url> - url where checking load speed
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    backend_performance_calc, frontend_performance_calc = page_load_time(sys.argv[1])
    print(f"Back End: {backend_performance_calc}ms")
    print(f"Front End: {frontend_performance_calc}ms")


if __name__ == '__main__':
    main()
