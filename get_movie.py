# coding：utf-8
import requests
from bs4 import BeautifulSoup
import re
import json


# 输入电影关键字
def get_movie(movie_name):
    url = "http://www.ifkdy.com/?q=" + movie_name + "&p=1"
    # url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
        , 'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
    }
    # 请求头
    r = requests.get(url=url, headers=headers)
    r1 = BeautifulSoup(r.text, "html.parser")
    # print(r1.find_all('a'))
    # 第一个汤
    # 正则筛第一波
    key = str(r1)
    p = "<a href=.*?\n<span.*?</span>\n<span>.*?</span>"
    rule = re.compile(p)
    key2 = rule.findall(key)
    key2 = str(key2)
    r2 = BeautifulSoup(key2, "html.parser")
    # print(r2)
    list1 = []
    list2 = []
    list3 = []
    # 靓汤筛第二波
    for link in r2.find_all('a'):
        cup = str(link.get('href'))
        list1.append(cup)

    for link2 in r2.find_all('span'):
        cup2 = str(link2.get_text())
        # out = ''.join(cup2.split())
        out = cup2.replace(u'\\xa0', u' ')
        list2.append(out)

    n = len(list1)
    # n=0
    # for item in list1:
    mum = len(list1)
    for n in range(mum):
        list3.append({'url': list1[n], 'title': list2[2 * n] + list2[2 * n + 1]})

    result = json.dumps({"data": list3})
    return result
