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
# FILE: find_forms.py
# Author: Maxim Felchuck
#
##############################################################################
"""
find_forms - function to find forms:

Usage: find_forms <url>

    <url> - url where finding forms
"""
import sys
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def get_forms_details(form):
    """
    function to extract all form's details
    return: form's details
    """
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    name = form.attrs.get("name")
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["name"] = name
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


class Forms():
    """
    find all forms on url
    """

    def __init__(self, session, url):
        self.session = session
        self.url = url

    def search_forms(self):
        """
        function to print all forms and forms details
        return: forms details
        """
        forms = self.get_all_forms()
        if len(forms) == 0:
            print(f"There no forms in site {self.url}")
            return None

        form_details = {}
        print(f"There {len(forms)} form(s) on site {self.url}")
        for form in forms:
            details = get_forms_details(form)
            form_details[form] = details
            print('-------------------------')
            print("Form name: ", details["name"])
            print("Action: ", details["action"])
            print("Method: ", details["method"])
            print("Inputs: ")
            for inputs in details["inputs"]:
                print("  " * 3, "-" * 4)
                print("  " * 3, "Input name: ", inputs["name"])
                print("  " * 3, "Input type: ", inputs["type"])
                print("  " * 3, "Input value: ", inputs["value"] if inputs["value"] else "None")

        return form_details

    def get_all_forms(self):
        """
        function to find all forms
        return: sites forms
        """
        soup = BeautifulSoup(self.session.get(self.url).content, "html.parser")
        return soup.find_all("form")


def main():
    """
    find_forms - function to find forms:

    Usage: find_forms <url>

        <url> - url where finding forms
    """
    if sys.argv[1] == '-h':
        print(__doc__)
        sys.exit(0)
    session = HTMLSession()
    forms = Forms(session, sys.argv[1])
    forms.search_forms()


if __name__ == '__main__':
    main()
