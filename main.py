import requests


if __name__ == '__main__':

    proxies = {
        'https': '51.254.32.245:3128'
    }

    response = requests.get('https://ipinfo.io/json')
    print(response.json())

    response = requests.get('https://ipinfo.io/json', proxies=proxies)
    print(response.json())
