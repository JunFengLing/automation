from api.http_util import http_get


url = 'http://www.baidu.com'
res = http_get(url=url)
print(res.text)

