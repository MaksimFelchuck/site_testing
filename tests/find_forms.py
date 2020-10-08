from bs4 import BeautifulSoup
from requests_html import HTMLSession
import sys


class Forms(object):

    def __init__(self, session, url):
        self.session = session
        self.url = url

    def search_forms(self):
        forms = self.get_all_forms()
        if len(forms) == 0:
            print(f"There no forms in site {self.url}")
            return None
        else:
            print(f"{self.url} site's forms: ")
        form_details = {}
        for form in forms:
            details = self.get_forms_details(form)
            form_details[form] = details
            print('-------------------------')
            print("Form name: ", details["name"])
            print("Action: ", details["action"])
            print("Method: ", details["method"])
            print("Inputs: ")
            for input in details["inputs"]:
                print("  " * 3, "-" * 4)
                print("  " * 3, "Input name: ", input["name"])
                print("  " * 3, "Input type: ", input["type"])
                print("  " * 3, "Input value: ", input["value"] if input["value"] else "None")

        return form_details

    def get_all_forms(self):
        res = self.session.get(self.url)
        # for javascript driven website
        # res.html.render()
        #soup = bs(s.get(url).content, "html.parser")
        soup = BeautifulSoup(self.session.get(self.url).content, "html.parser")
        return soup.find_all("form")

    def get_forms_details(self, form):
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


def main():
    session = HTMLSession()
    forms = Forms(session, sys.argv[1])
    forms.search_forms()


if __name__ == '__main__':
    main()
