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
            title = soup.find(class_='entry-title')
            a = title.find('a')
            href = a['href'].strip()
            print("找到最新发布页")
            
            response = requests.get(url=href)
            print("进入最新发布页")
            soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
            post_body = soup.find(class_='yd-unlocked-content')
            p = post_body.find('p')
            txt_url = ''
            findRay = False
            findClash = False
            while p:
                text = p.text
                if 'https://' in text and '.txt' in text:
                    txt_url = re.findall(r'https://.*?txt', text)[0]
                    findRay = True
                    print("找到最新v2ray订阅地址")
                if 'https://' in text and '.yaml' in text:
                    clash_url = re.findall(r'https://.*?yaml', text)[0]
                    findClash = True
                    print("找到最新clash订阅地址")
                    
                if findRay and findClash: 
                    break
                p = p.find_next_sibling('p')
                 
            print("获取v2ray订阅内容")   
            response = requests.get(url=txt_url)
            print("获取clash订阅内容")
            clash_response = requests.get(url=clash_url)
            
            # 保存
            with open('mibei.txt', 'w', encoding='utf-8') as f:
                f.write(response.text)    
            with open('mibei.yaml', 'w', encoding='utf-8') as f:
                f.write(clash_response.text)
            
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
