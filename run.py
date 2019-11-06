# -*- coding: utf-8 -*-

import os


websites = {
    "cmcc": [
        {"script": "ssr/ssr.py",
        "email": "cmcc_email",
        "passwd": "cmcc_passwd",
        "base_url": "cmcc_base_url"}}
    ]
}


def runner():
    for website, config_list in websites:
        for config in config_list:
            os.system(f"python ./lib/{config.script} ${{ secrets.}}")
