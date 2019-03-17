# coding：utf-8
import requests
import json


def get_music(music_name):
    headers = {'Host': 'music.bbbbbb.me',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate',
               'Referer': 'http://music.bbbbbb.me/',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest',
               'Content-Length': '47',
               'Connection': 'keep-alive',
               'Pragma': 'no-cache',
               'Cache-Control': 'no-cache'}
    mname = music_name
    data = {'input': mname, 'filter': 'name', 'type': 'netease', 'page': '1'}
    url = 'http://music.bbbbbb.me/'
    wbdata = requests.post(url, headers=headers, data=data).text
    data = json.loads(wbdata)
    re_data = []
    for n in data['data']:
        dic = {}
        title = n['title']
        author = n['author']
        url = n['url']
        dic['title'] = title
        dic['author'] = author
        dic['url'] = url
        re_data.append(dic)
    data_r = json.dumps({"data": re_data})
    return data_r
