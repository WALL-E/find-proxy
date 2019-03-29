#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import sys
import os
import time

import ipaddress
import requests

from bs4 import BeautifulSoup


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-Hans-CN;q=1, en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    
}


def com_xicidaili_1():
    results = []

    for i in range(1, 21):
        home_url = "https://www.xicidaili.com/nn/%s" % (i,)
        response = requests.get(home_url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll('table', id="ip_list")
        table = tables[0]
        for tr in table.findAll('tr'):
            tds = tr.findAll('td')
            if len(tds) > 0:
                ip = tds[1].string
                port = tds[2].string
                content = "%s:%s" %(ip, port)
                try:
                    ip_tmp = ipaddress.IPv4Address(ip)
                    if ip_tmp.is_private or ip_tmp.is_reserved or ip_tmp.is_multicast:
                        print("private,reserved,multicast is not valid")
                        continue
                except ipaddress.AddressValueError as e:
                    print(e)
                    continue
                results.append(content)
    return results


def com_xicidaili_2():
    results = []

    for i in range(1, 21):
        home_url = "https://www.xicidaili.com/wt/%s" % (i,)
        response = requests.get(home_url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll('table', id="ip_list")
        table = tables[0]
        for tr in table.findAll('tr'):
            tds = tr.findAll('td')
            if len(tds) > 0:
                ip = tds[1].string
                port = tds[2].string
                content = "%s:%s" %(ip, port)
                try:
                    ip_tmp = ipaddress.IPv4Address(ip)
                    if ip_tmp.is_private or ip_tmp.is_reserved or ip_tmp.is_multicast:
                        print("private,reserved,multicast is not valid")
                        continue
                except ipaddress.AddressValueError as e:
                    print(e)
                    continue
                results.append(content)
    return results



def cn_66ip():
    results = []
    for i in range(1, 30):
        home_url = "http://www.66ip.cn/areaindex_%s/1.html" % (i,)
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
                        print("private,reserved,multicast is not valid")
                        continue
                except ipaddress.AddressValueError as e:
                    print(e)
                    continue
                results.append(content)
    return results


def cn_31f():
    home_url = "http://31f.cn/http-proxy/"
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
                    print("private,reserved,multicast is not valid")
                    continue
            except ipaddress.AddressValueError as msg:
                print(msg)
                continue
            results.append(content)
    return results


def get_proxy_list():
    proxy_list = cn_66ip()
    return proxy_list


def main():
    print(get_proxy_list())


if __name__ == '__main__':
    main()
