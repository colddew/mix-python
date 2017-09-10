import hashlib


'''
curl
-H 'Host: api.dzwbaike.xyz'
-H 'Content-Type: text/html;charset=UTF-8'
-H 'Accept: */*' -H 'Accept-Language: zh-cn'
-H 'token: 05e33d91-dd85-40d5-aa67-a90130270a95'
-H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.15 NetType/WIFI Language/zh_CN'
-H 'sign: b59fc7995e1dae61de5b768f58ea3367'
-H 'timestamp: 1505011126698'
-H 'Referer: https://servicewechat.com/wx56f5e9f2dde583b2/4/page-frame.html'
--compressed
'https://api.dzwbaike.xyz/api/tdouroubaikenew/list?page=6&limit=20'
'''
m2 = hashlib.md5()
sign = 'https://api.dzwbaike.xyz/api/tdouroubaikenew/list?page=6&limit=20'
m2.update(sign)
print m2.hexdigest()
