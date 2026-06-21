import requests

def make_request(url):
    try:
        response = requests.get(url, timeout=10)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None