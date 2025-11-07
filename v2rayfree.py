import requests
from bs4 import BeautifulSoup
import os
import time
import sys

# main
if __name__ == '__main__':
    # if(sys.argv.count() < 2):
    #     print("请输入url")
    #     sys.exit()
    while True:
        try:
            url = sys.argv[1]
            response = requests.get(url=url)
            soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
            title = soup.find(class_='entry-title')
            a = title.find('a')
            href = a['href'].strip()
            
            response = requests.get(url=href)
            soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
            post_body = soup.find(class_='post-body entry-content')
            p = post_body.find('p')
            txt_url = ''
            while p:
                text = p.text
                if 'https://' in text and '.txt' in text:
                    txt_url = text
                    break
                p = p.find_next_sibling('p')
                    
            response = requests.get(url=txt_url)
            
            # 保存
            with open('v2rayfree.txt', 'w', encoding='utf-8') as f:
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
