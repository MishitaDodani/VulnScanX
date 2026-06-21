import requests

SQLI_PAYLOADS = [
    "'",
    "' OR '1'='1",
    "\" OR \"1\"=\"1"
]

SQL_ERRORS = [
    "mysql",
    "sql syntax",
    "syntax error",
    "unclosed quotation mark"
]

def scan_sqli(url):
    vulnerable = []

    for payload in SQLI_PAYLOADS:
        test_url = url + payload

        try:
            r = requests.get(test_url)

            for error in SQL_ERRORS:
                if error.lower() in r.text.lower():
                    vulnerable.append(test_url)

        except:
            pass

    return vulnerable