import requests
from lxml import html
import re

def get_zhihu_hot():
    headers={
	    'Host':'www.zhihu.com',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Pargma': 'np-cache',
        'Cookie': '',       # 复制填写自己的cookie
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Inter Mac OS X 10_12_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    url = "https://www.zhihu.com/hot"
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    urls = root.xpath('//div[@class="HotItem-content"]')


    all = []
    for i in range(50):
        term = []
        html_text = html.tostring(urls[i], encoding='utf-8').decode('utf-8')
        ul = re.findall(r"href=\"(.+?)\" title=\"", html_text)
        title = re.findall(r"title=\"(.+?)\" target", html_text)
        term.append(title)
        term.append(ul)
        all.append(term)

    return all


if __name__ == '__main__':
    
    print(" ")
    get_zhihu_hot()
