import sys
import requests
from find_forms import Forms
from urllib.parse import urljoin
from pprint import pprint


class Injection(object):
    def __init__(self, url):
        self.url = url

    def scan(self):
        session = requests.Session()
        session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        for c in "\"'":
            new_url = f"{self.url}{c}"
            print("Trying...", new_url)
            res = session.get(new_url)
            if self.is_vulnerable(res):
                print("SQL Injection vulnerability detected, link:", new_url)
                return
        forms = Forms(session, self.url)
        forms = forms.search_forms()
        if not forms:
            return 0

        for form, detail in forms.items():
            for c in "\"'":
                data = {}
                for input_tag in detail["inputs"]:
                    if input_tag["value"] or input_tag["type"] == "hidden":
                        try:
                            data[input_tag["name"]] = input_tag["value"] + c
                        except:
                            pass
                    elif input_tag["type"] != "submit":
                        data[input_tag["name"]] = f"test{c}"
            url = urljoin(self.url, detail["action"])
            if detail["method"] == "post":
                res = session.post(url, data=data)
            elif detail["method"] == "get":
                res = session.get(url, params=data)
            if self.is_vulnerable(res):
                print("SQL Injection vulnerability detected, link:", url)
                print("Form:")
                pprint(form)
                break

    def is_vulnerable(self, response):
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


def main():
    injection = Injection(sys.argv[1])
    injection.scan()


if __name__ == '__main__':
    main()
