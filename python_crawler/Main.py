import requests
from lxml import etree
import json

data = []
html = requests.get('https://www.linuxcool.com/').text
content = etree.HTML(html)
urls = content.xpath("//div[contains(@class, 'column col-half')]/ul[@class='category-posts'][1]/li[@class='format-standard']/a/@href")

def dealSuburl(url, it):
    it['params'] = []
    html = requests.get(url).text
    content = etree.HTML(html)
    usage = content.xpath('//p/strong[contains(text(), "语法格式")]/parent::node()/text()')
    it['usage'] = usage
    params = content.xpath('//article//table//td/text()')
    for index in range(int(len(params) / 2)):
        tmp = {}
        tmp['param'] = params[index * 2].strip()
        tmp['content'] = params[index * 2 + 1].strip()
        it['params'].append(tmp)

# To print the href attribute of each link
for url in urls:
    it = {}
    it['name'] = (url.split('/')[-1])
    data.append(it)
    dealSuburl(url, it)

file_name = 'data.json'

with open(file_name, 'w') as f:
    f.write(json.dumps(data, ensure_ascii=False))

print(data)
