import requests, json

urlstr = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-KUAIDI1621064192535.html'

header = {'User-Agent': 'Mozilla/5.0'}
s = requests.session()
r = s.post(url=urlstr, headers=header)
result = r.json()
print(result["data"][0]["context"])

