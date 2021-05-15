import requests, json

urlstr = 'https://www.wanandroid.com/user/login'

payload = {'username': 'xujiexuan', 'password': 'xujiexuan126'}
r = requests.post(url=urlstr, data=payload)
cookie = r.cookies
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0', cookies=cookie)
print('*****', r.text)
print('**********', r2.text)
