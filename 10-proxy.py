import urllib
import urllib.request
'''
使用快代理
'''
proxies = {
    'HTTP':'139.196.137.255:8118',
}

proxyhandler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxyhandler)

response = opener.open(fullurl='http://www.baidu.com')
print(response.read().decode('utf-8'))