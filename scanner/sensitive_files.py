import requests

SENSITIVE_FILES = [
    "/robots.txt",
    "/.git/",
    "/backup.zip",
    "/config.php",
    "/admin/"
]

def scan_sensitive_files(base_url):
    found = []

    for file in SENSITIVE_FILES:
        url = base_url + file

        try:
            r = requests.get(url, timeout=5)

            if r.status_code == 200:
                found.append(url)

        except:
            pass

    return found