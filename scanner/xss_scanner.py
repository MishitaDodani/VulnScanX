import requests
from bs4 import BeautifulSoup

XSS_PAYLOAD = "<script>alert('xss')</script>"

def scan_xss(url):
    vulnerabilities = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        forms = soup.find_all("form")

        for form in forms:
            action = form.get("action")
            method = form.get("method", "get").lower()

            inputs = form.find_all("input")

            data = {}

            for input_tag in inputs:
                name = input_tag.get("name")

                if name:
                    data[name] = XSS_PAYLOAD

            target_url = url + action

            if method == "post":
                r = requests.post(target_url, data=data)
            else:
                r = requests.get(target_url, params=data)

            if XSS_PAYLOAD in r.text:
                vulnerabilities.append(target_url)

    except Exception as e:
        print(e)

    return vulnerabilities