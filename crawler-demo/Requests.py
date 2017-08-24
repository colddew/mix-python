# -*- coding:utf-8 -*-

import requests
import json


r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.url

r = requests.get("a.json")
print r.text
print r.json()

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print r.url

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text

url = 'http://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}
r = requests.post(url, files=files)
print r.text

with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)

url = 'http://example.com'
r = requests.get(url)
print r.cookies
print r.cookies['example_cookie_name']

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text

requests.get('http://github.com', timeout=0.001)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r.text

proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text
