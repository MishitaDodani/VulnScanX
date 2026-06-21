def check_directory_listing(response):
    keywords = [
        "Index of /",
        "Parent Directory"
    ]

    for keyword in keywords:
        if keyword in response.text:
            return True

    return False