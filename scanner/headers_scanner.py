SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

def scan_headers(response):
    missing_headers = []

    for header in SECURITY_HEADERS:
        if header not in response.headers:
            missing_headers.append(header)

    return missing_headers