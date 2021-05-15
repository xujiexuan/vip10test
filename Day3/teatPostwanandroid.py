import requests, json

urlstr = 'https://www.wanandroid.com/user/login'

payload = {'username': 'xujiexuan', 'password': 'xujiexuan1126'}
header = {'User-Agent': 'Mozilla/5.0'}
r = requests.post(url=urlstr, data=payload, headers=header)

print(r.text)
try:
    if r.status_code == 200:
        if r.json()['data']['username'] == 'xujiexuan':
            print(f'成功{r.json()["data"]["username"]}')
except TypeError as msg:
    print("登录失败")
