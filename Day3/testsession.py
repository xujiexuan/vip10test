import requests, json

urlstr = 'https://www.wanandroid.com/user/login'

payload = {'username': 'xujiexuan', 'password': 'xujiexuan126'}
s = requests.session()
r = s.post(url=urlstr, data=payload)
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
print(s)
print('*****', r.text)
print('**********', r2.text)
s.cookies