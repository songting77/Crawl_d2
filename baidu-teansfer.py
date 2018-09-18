import urllib
import urllib.request
import urllib.parse
import json

'''
post请求典型案例，对form表单要求严格
'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://fanyi.baidu.com/',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'BAIDUID=8FC3E471D9D8D0298DED7555CCAC2729:FG=1; '
             'BIDUPSID=8FC3E471D9D8D0298DED7555CCAC2729; '
             'PSTM=1522748651; '
             'BDUSS=d-bU5-fkNYNXFWYXVSVzczU0FMeFFPRnRofkR0MU1zb3F-RVBXQ0FJU0c3UHBhQVFBQUFBJCQAAAAAAAAAAAEAAACwNFNjsc--ufXj9cmyu9TZwLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZf01qGX9Naaj; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSINO=6; H_PS_PSSID=1466_21108_26350_22158; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1536845085,1536888575,1536888581,1536888598; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1536888598; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'Host':'fanyi.baidu.com'
}

url = 'https://fanyi.baidu.com/v2transapi'

#from=zh
# &to=en
# &query=%E6%B3%95%E5%9B%BD
#transtype	realtime
# simple_means_flag	3
# sign	287735.32966
# &simple_means_flag=3
# &sign=287735.32966
# &token=713a04589aa01a8c2470aa9ccdfc944e
key=input('输入想要翻译的内容:')
form = {
    'from':'zh',
    'to':'en',
    'query':key,
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'477072.238753',
    'token':'713a04589aa01a8c2470aa9ccdfc944e',
}
#urlencode:form表单里专用
form = urllib.parse.urlencode(form).encode('UTF-8')

request = urllib.request.Request(url=url,headers=headers,data=form)

response = urllib.request.urlopen(request)
content = response.read().decode('unicode-escape')
#利用json.load 进行加载，然后dumps转码，不采用ascii
content1 = json.dumps(content,ensure_ascii=False)
content1 = json.loads(content1,encoding='UTF-8')
print(content1)