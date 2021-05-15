import requests, json

urlstr = 'https://www.wanandroid.com/user/login'

payload = {'username': 'xujiexuan', 'password': 'xujiexuan126'}
r = requests.post(url=urlstr, data=payload)
JSESSIONID = r.cookies["JSESSIONID"]
header = {'cookie': 'JSESSIONID=' + JSESSIONID}
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0', headers=header)
print('*****', r.text)
print('**********', r2.text)
