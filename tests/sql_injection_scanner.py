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
# FILE: sql_injection_scanner.py
# Author: Maxim Felchuck
#
##############################################################################
"""
SQL_injection_Scanner - function to check site on SQL injection attack vulnerability:

Usage: SQL_injection_Scanner <url>

    <url> - url where checking SQL injection attack vulnerability
"""
import sys
from urllib.parse import urljoin
from pprint import pprint
import requests
from find_forms import Forms


def _is_vulnerable(response):
    errors = {
        "you have an error in your sql syntax;",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
        "supplied argument is not a valid mysql result resource in"
    }
    for error in errors:
        if error in response.content.decode("latin-1").lower():
            return True
    return False


class Injection():
    """
    url - url where checking SQL injection attack vulnerability
    """
    def __init__(self, url):
        self.url = url

    def scan(self):
        """
        function to check site on SQL injection attack vulnerability
        return: True/False
        """
        session = requests.Session()
        session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        for symbol in "\"'":
            new_url = f"{self.url}{symbol}"
            print("Trying...", new_url)
            res = session.get(new_url)
            if _is_vulnerable(res):
                print("SQL Injection vulnerability detected, link:", new_url)
                return True
        return self.scan_forms(session)

    def scan_forms(self, session):
        """
        function to check forms
        """
        forms = Forms(session, self.url)
        forms = forms.search_forms()
        is_vulnerable = False
        if not forms:
            print("No SQL Injection vulnerability detected, link:", self.url)
            return is_vulnerable
        for form, detail in forms.items():
            for symbol in "\"'":
                data = {}
                for input_tag in detail["inputs"]:
                    if input_tag["value"] or input_tag["type"] == "hidden":
                        try:
                            data[input_tag["name"]] = input_tag["value"] + symbol
                        except:
                            pass
                    elif input_tag["type"] != "submit":
                        data[input_tag["name"]] = f"test{symbol}"
            url = urljoin(self.url, detail["action"])
            if detail["method"] == "post":
                res = session.post(url, data=data)
            elif detail["method"] == "get":
                res = session.get(url, params=data)
            if _is_vulnerable(res):
                is_vulnerable = True
                print("SQL Injection vulnerability detected, link:", url)
                print("Form:")
                pprint(form)
                break

            print("No SQL Injection vulnerability detected, link:", url)
        return is_vulnerable


def main():
    """
    SQL_injection_Scanner - function to check site on SQL injection attack vulnerability:

    Usage: SQL_injection_Scanner <url>

        <url> - url where checking SQL injection attack vulnerability
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    injection = Injection(sys.argv[1])
    injection.scan()


if __name__ == '__main__':
    main()
