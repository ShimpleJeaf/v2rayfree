# 创建python虚拟环境

```batch
uv venv .venv
.venv\Scripts\activate.bat
uv pip install -r requirements.txt
```

# 手动爬取

结果生成在mibei.txt里

```batch
.venv\Scripts\activate.bat
python mibei.py https://www.mibei77.com
```

# 自动更新

在windows的**任务计划程序**里添加定时执行mibei_run.bat