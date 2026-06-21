def check_clickjacking(response):
    headers = response.headers

    if "X-Frame-Options" not in headers:
        return True

    return False