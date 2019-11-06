# -*- coding: utf-8 -*-
import os

websites = [{
    "script":
    "ssr/ssr.py",
    "config": [{
        "email": "cmcc_email",
        "passwd": "cmcc_passwd",
        "base_url": "base_url"
    }]
}]


def runner():
    for website, config_list in websites:
        command = "python ./lib/"
        for config in config_list:
            os
