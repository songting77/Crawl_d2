import urllib
import urllib.request
import urllib.parse


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'',
    'Accept-Language':'zh-CN,zh;q=0.9',
}

url = 'https://tieba.baidu.com/f?kw=%s&pn=%d'


def write_to_file(content,i):
    with open('./download/贴吧第%d页.html'%(i+1),mode='w') as fp:
        fp.write(content)
        print('完成第%d页下载'%(i+1))

def load_url_data(key, page):
    for i in range(page):
        url_detail =url%(key,i*50)
        request = urllib.request.Request(url=url_detail, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('UTF-8')
        write_to_file(content,i)
        #read方法只能读一次，再读则为空
        print('---------------',content)


if __name__ == '__main__':
    key = input('输入相关内容：')
    key =urllib.parse.quote(key)

    try:
        page = int(input('输入爬取页码：'))
    except Exception as e :
        while True:
            print('请输入整数：')
            page = int(input('输入爬取页码：'))

    load_url_data(key,page)