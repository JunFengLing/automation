import requests


def http_get(url):
    print('Http get start')
    res = requests.get(url=url)
    return res


def http_post(url, headers, body):
    print('Http post start')
    res = requests.post(url=url, data=body, headers=headers)
    return res
