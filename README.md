# find-proxy

从网上爬取到FREE PROXY并进行可用性验证, 目前只实现了对HTTP的抓取


## 安装

```
pip3 install -r requirements.txt

```

## 启动

直接运行t.py就可行

```
# ./t.py
* | DEBUG    | __main__:main:37 - {'http': 'http://180.168.13.26:8000'}: ProxyError[3]
* | DEBUG    | __main__:main:40 - {'http': 'http://114.80.62.134:8080'}: ConnectTimeout
* | DEBUG    | __main__:main:40 - {'http': 'http://114.80.62.134:8080'}: ConnectTimeout
* | INFO     | __main__:main:32 - {'http': 'http://203.110.164.139:52144'}: Ok
* | DEBUG    | __main__:main:40 - {'http': 'http://180.164.24.165:53281'}: ConnectTimeout
* | INFO     | __main__:main:32 - {'http': 'http://180.159.253.218:9000'}: Ok
* | DEBUG    | __main__:main:37 - {'http': 'http://49.51.193.128:1080'}: ProxyError[3]
* | DEBUG    | __main__:main:37 - {'http': 'http://49.51.193.134:1080'}: ProxyError[3]
* | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
* | DEBUG    | __main__:main:40 - {'http': 'http://111.160.236.84:40610'}: ConnectTimeout
* | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
* | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
* | DEBUG    | __main__:main:43 - {'http': 'http://221.239.86.26:32228'}: ReadTimeout
* | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
* | DEBUG    | __main__:main:40 - {'http': 'http://111.160.236.84:40610'}: ConnectTimeout
* | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
* | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
```
