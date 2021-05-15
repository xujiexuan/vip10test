# 导入
import requests

# 请求
urlstr = 'http://www.wanandroid.com/article/query'

# 参数
payload = {'k': 'Android'}

# 发送
r = requests.get(url=urlstr, params=payload)

# 打印结果
print(r.text)
print(r.status_code)
print("headers")
print(r.headers)
print("encoding")
print(r.encoding)
print("content")
print(r.content)
print("url")
print(r.url)
#print(r.json())
print("cookies")
print(r.cookies)
#print(r.text)
print("raw")
print(r.raw)
print(r.raise_for_status())