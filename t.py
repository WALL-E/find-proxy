#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import sys
import os
import time

import requests

from loguru import logger
from spider import get_proxy_list

def main():
    proxy_list = get_proxy_list()

    while True:
        if len(proxy_list) == 0:
            break
            proxy_list = get_proxy_list()

        proxies = {
            "http": "http://%s" % (proxy_list[0]),
        }
        proxy_list.pop(0)

        try:
            response = requests.get("http://checkip.amazonaws.com", proxies=proxies, timeout=1)
            if response.status_code == 200:
                logger.info(proxies)
                text = response.text.strip()
                if text.replace(".", "").replace(",", "").replace(" ", "").isdigit():
                    logger.info("text: %s" % (response.text.strip(),))
                else:
                    logger.info("%s: ProxyError[2]" % (proxies))
                    continue
            else:
                logger.info("%s: ProxyError[3]" % (proxies))
                continue
        except requests.exceptions.ConnectTimeout as e:
            logger.info("%s: ConnectTimeout" % (proxies))
            continue
        except requests.exceptions.ReadTimeout as e:
            logger.info("%s: ReadTimeout" % (proxies))
            continue
        except requests.exceptions.ProxyError as e:
            logger.info("%s: ProxyError[1]" % (proxies))
            continue
        except requests.exceptions.TooManyRedirects as e:
            logger.info("%s: TooManyRedirects" % (proxies))
            continue
        except requests.exceptions.ChunkedEncodingError as e:
            logger.info("%s: ChunkedEncodingError" % (proxies))
            continue
        except requests.exceptions.ConnectionError as e:
            logger.info("%s: ConnectionError" % (proxies))
            continue

        # logger.info("sleep 1")
        time.sleep(1)


if __name__ == '__main__':
    main()
