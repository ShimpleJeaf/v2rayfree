import base64
import json
from loguru import logger

class ReNumber:
    src_urls: list[str]
    
    def __init__(self, filename: str) -> None:
        self.load(filename)
        self.parser()
        
    def load(self, filename: str) -> None:
        # 读取源文件
        c = base64.b64decode(open(filename, 'rb').read()).decode('utf-8')
        self.src_urls = c.split('\r\n')
        
    def parser(self):
        i = 1
        new_urls = []
        for url in self.src_urls:
            if not url:
                continue
            
            # vmess 本身也是base64编码的
            if url.startswith('vmess'):
                segs = url.split('://')
                if(len(segs) != 2):
                    logger.error(f'不支持：{url}')
                    continue
                url = segs[1]
                url = base64.b64decode(url.encode('utf-8')).decode('utf-8')
                # 解码后的内容是json格式的
                # 名字是ps字段
                j = json.loads(url)
                name = str(i) + '-' + j['ps']
                j['ps'] = name
                # json转str
                url = json.dumps(j)
                # 编码
                url = base64.b64encode(url.encode('utf-8')).decode('utf-8')
                url = 'vmess://' + url
                new_urls.append(url)
                i = i + 1
                continue
                
            # #后面是代理的名字
            segs = url.split('#')
            if len(segs) != 2:
                logger.error(f'不支持：{url}')
                continue
            base = segs[0]
            name = segs[1]
            name = str(i) + '-' + name
            new_urls.append(base + '#' + name)
            i = i + 1
        self.src_urls = new_urls
            
    def base64(self):
        src = ''
        for url in self.src_urls:
            src = src + url + '\r\n'
        return base64.b64encode(src.encode('utf-8'))
        
        
if __name__ == '__main__':
    r = ReNumber('mibei.txt')
    logger.add('log.log', enqueue=True)
    open('mibei.txt', 'wb').write(r.base64())
    logger.complete()
