import urllib
import urllib.request

httphandler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(httphandler)

#方式1：直接使用opener发起请求
#方式2：将opener作为参数设置给urllib.request.urlopen
#方式2使用时，opener将变成全局的
urllib.request.install_opener(opener)

response = urllib.request.urlopen('http://ww.baidu.com')
print(response.read().decode('utf-8'))