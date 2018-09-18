import urllib
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           }

url = "http://www.baidu.com"

#urlopen处理方式，不能自己构建请求头，request对象不能使用代理
# request = urllib.request.urlopen(url=url)

#handler:http处理器对象，为了使用代理。
httpHandler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(httpHandler)
#使用opener访问网络数据==urllib.request.urlopen()
request = urllib.request.Request(url=url,headers=headers)
response = opener.open(request)
# response = opener.open(fullurl='http://www.baidu.com')
print(response.read().decode('utf-8'))
