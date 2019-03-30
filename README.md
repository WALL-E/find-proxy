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
2019-03-30 13:56:14.666 | DEBUG    | __main__:main:37 - {'http': 'http://180.168.13.26:8000'}: ProxyError[3]
2019-03-30 13:56:15.670 | DEBUG    | __main__:main:40 - {'http': 'http://114.80.62.134:8080'}: ConnectTimeout
2019-03-30 13:56:16.674 | DEBUG    | __main__:main:40 - {'http': 'http://114.80.62.134:8080'}: ConnectTimeout
2019-03-30 13:56:17.181 | INFO     | __main__:main:32 - {'http': 'http://203.110.164.139:52144'}: Ok
2019-03-30 13:56:19.185 | DEBUG    | __main__:main:40 - {'http': 'http://180.164.24.165:53281'}: ConnectTimeout
2019-03-30 13:56:19.853 | INFO     | __main__:main:32 - {'http': 'http://180.159.253.218:9000'}: Ok
2019-03-30 13:56:21.598 | DEBUG    | __main__:main:37 - {'http': 'http://49.51.193.128:1080'}: ProxyError[3]
2019-03-30 13:56:22.058 | DEBUG    | __main__:main:37 - {'http': 'http://49.51.193.134:1080'}: ProxyError[3]
2019-03-30 13:56:22.575 | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
2019-03-30 13:56:24.579 | DEBUG    | __main__:main:40 - {'http': 'http://111.160.236.84:40610'}: ConnectTimeout
2019-03-30 13:56:25.074 | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
2019-03-30 13:56:26.573 | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
2019-03-30 13:56:28.591 | DEBUG    | __main__:main:43 - {'http': 'http://221.239.86.26:32228'}: ReadTimeout
2019-03-30 13:56:29.095 | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
2019-03-30 13:56:31.100 | DEBUG    | __main__:main:40 - {'http': 'http://111.160.236.84:40610'}: ConnectTimeout
2019-03-30 13:56:31.617 | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
2019-03-30 13:56:32.903 | INFO     | __main__:main:32 - {'http': 'http://221.239.86.26:32228'}: Ok
```
