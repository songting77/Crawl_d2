import urllib
import urllib.request
'''
错误的url和http error，利用cookie 模拟登陆
'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Cookie':'bid=Ujhmjig5joY; ll="118281"; gr_user_id=79774fa1-d276-44ba-b7e2-263bc80b0c9c; _vwo_uuid_v2=DB31EE46671049A2833E07E59E57BAA28|dc84014332bfaec4480fc8bdebec95c0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1537163872%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSaqYXz8FAmdCDBspRmKoqMiCHW7nBuax4gqsxZQKkfgkIo76e8pFhI9U86J3XYvq%26wd%3D%26eqid%3Dfbab9bac00044aae000000065b9f424c%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1860660712.1534160395.1536821604.1537163874.6; __utmc=30149280; __utmz=30149280.1537163874.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ps=y; dbcl2="184655032:5WzbkJeC3bU"; ck=0r-H; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18465; __yadk_uid=eKYOS9qUiJQ2CLS81Lhue0TDhRmX427d; ap_v=0,6.0; douban-profile-remind=1; ct=y; _pk_id.100001.8cb4=d04ff90b1f82c70b.1534775678.4.1537164314.1536824974.; __utmb=30149280.19.10.1537163874'
}


url = "https://www.douban.com/people/184655032/"
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))