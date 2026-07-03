import requests
from bs4 import BeautifulSoup
import os
import time
import sys
import re

# main
if __name__ == '__main__':
    # if(sys.argv.count() < 2):
    #     print("请输入url")
    #     sys.exit()
    while True:
        try:
            url = sys.argv[1]
            response = requests.get(url=url)
            print("进入首页")
            soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
            title = soup.find(class_='item-heading')
            a = title.find('a')
            href = a['href'].strip()
            print("找到最新发布页")
            
            response = requests.get(url=href)
            print("进入最新发布页")
            soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
            post_body = soup.find(class_='article-content')
            p = post_body.find('p')
            txt_url = ''
            while p:
                text = p.text
                if 'https://' in text and '.txt' in text:
                    txt_url = re.findall(r'https://.*?txt', text)[0]
                    print("找到最新订阅地址")
                    break
                p = p.find_next_sibling('p')
                 
            print("获取订阅内容")   
            response = requests.get(url=txt_url)
            
            # 保存
            with open('mibei.txt', 'w', encoding='utf-8') as f:
                f.write(response.text)    
            
            print('获取成功')
            break            

        except requests.exceptions.Timeout:
            print('requests.exceptions.Timeout, 一分钟后重试')
            time.sleep(60)
            print('重试...')
        else:
            print('发生了其他异常，一分钟后重试')
            time.sleep(60)
            print('重试...')
