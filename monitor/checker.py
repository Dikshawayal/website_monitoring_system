import requests
import time


def check_website(url):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=5)

        response_time = round(
            (time.time() - start_time) * 1000,
            2
        )

        return {
            'status': 'UP',
            'status_code': response.status_code,
            'response_time': response_time
        }

    except:
        return {
            'status': 'DOWN',
            'status_code': 0,
            'response_time': None
        }