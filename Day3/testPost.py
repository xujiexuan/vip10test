import requests, json

urlstr = 'http://httpbin.org/post'

payload = {'qq群名': 'selenium+jmeter+loadrunner', 'qq群名': '106014970'}

payload = json.dumps(payload)

r = requests.post(url=urlstr, data=payload)

print(r.text)

print(r.json())
