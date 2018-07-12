# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time


if __name__ == '__main__':
    list_url = []
    for num in range(1,10):
        url = 'http://www.mmonly.cc/mmtp/list_9_%d.html' % num
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url=url, headers=headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='ABox')

        for each in targets_url:
            list_url.append(each.a.get('href'))

    print('连接采集完成')

    for each_img in list_url:
        target_url = each_img
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        img_req = requests.get(url=target_url, headers=headers)
        img_req.encoding = 'gb18030'
        img_html = img_req.text
        img_bf_1 = BeautifulSoup(img_html, 'lxml')
        img_url = img_bf_1.find_all('div', class_='big-pic')
        img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
        img_url = img_bf_2.div.img.get('src')
        filename = img_bf_2.div.img.get('alt')
        print('正在下载：' + filename)
        if 'girls' not in os.listdir():
            os.makedirs('girls')
        urlretrieve(url=img_url, filename='girls/' + filename)
        time.sleep(1)
    print("over")