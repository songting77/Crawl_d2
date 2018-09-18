import urllib
import urllib.request
import urllib.parse

'''
form数据：
cname=
&pid=31
&pageIndex=5
&pageSize=10
'''
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

url_get = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid&cname=&pid=31&pageIndex=8&pageSize=10'
# url_get = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid&cname=&pid=31&pageIndex=6&pageSize=10'

if __name__ == '__main__':

    city = input('查询城市：')
    page = int(input('总计查询页码：'))
    for p in range(1,page+1):
        form = {'cname': city,
                'pid': 31,
                'pageIndex': p,
                'pageSize': '30'}
        form = urllib.parse.urlencode(form).encode('utf-8')
        request = urllib.request.Request(url=url,headers=headers,data=form)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # print(content)

        with open('./download/肯德基第%d页店铺文件.json'%(p),mode='wb') as fp:
            fp.write(content.encode('utf-8'))
