#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import sys
import os
import time

import ipaddress
import requests

from bs4 import BeautifulSoup
from loguru import logger


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-Hans-CN;q=1, en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
}


def cn_66ip():
    results = []
    for i in range(1, 30):
        home_url = "http://www.66ip.cn/areaindex_%s/1.html" % (i,)
        logger.debug(home_url)
        response = requests.get(home_url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll('table')
        table = tables[2]
        for tr in table.findAll('tr')[1:]:
            tds = tr.findAll('td')
            if len(tds) > 0:
                ip = tds[0].string
                port = tds[1].string
                content = "%s:%s" %(ip, port)
                try:
                    ip_tmp = ipaddress.IPv4Address(ip)
                    if ip_tmp.is_private or ip_tmp.is_reserved or ip_tmp.is_multicast:
                        logger.debug("private,reserved,multicast is not valid")
                        continue
                except ipaddress.AddressValueError as e:
                    logger.debug(e)
                    continue
                results.append(content)
    return results


def cn_31f():
    home_url = "http://31f.cn/http-proxy/"
    logger.debug(home_url)
    response = requests.get(home_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.findAll('table')
    table = tables[0]
    results = []
    for tr in table.findAll('tr')[1:]:
        tds = tr.findAll('td')
        if len(tds) > 0:
            ip = tds[1].string
            port = tds[2].string
            content = "%s:%s" %(ip, port)
            try:
                ip_tmp = ipaddress.IPv4Address(ip)
                if ip_tmp.is_private or ip_tmp.is_reserved or ip_tmp.is_multicast:
                    logger.debug("private,reserved,multicast is not valid")
                    continue
            except ipaddress.AddressValueError as msg:
                logger.debug(msg)
                continue
            results.append(content)
    return results


def get_proxy_list():
    logger.debug("Spider working")
    proxy_list = cn_66ip() + cn_31f()
    return proxy_list


def main():
    logger.debug(get_proxy_list())


if __name__ == '__main__':
    main()
