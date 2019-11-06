# -*- coding: utf-8 -*-

import requests
from urllib.parse import urljoin
import os


class CheckIn(object):
    def __init__(self, base_url):
        self.login_url = urljoin(base_url, "/auth/login")
        self.checkin_url = urljoin(base_url, "/user/checkin")
        self.session = requests.Session()

    def login(self, email, password):
        rep = self.session.post(self.login_url,
                                data={
                                    "email": email,
                                    "passwd": password,
                                    "code": ""
                                })
        print(rep.json())

    def checkin(self):
        rep = self.session.post(self.checkin_url)
        print(rep.json())


if __name__ == "__main__":
    base_url = "https://cmcc.bid"
    # email = "z794672847@qq.com"
    email = os.system("echo ${{ secrets.cmcc_email }}")
    password = "Zy950722"
    client = CheckIn(base_url)
    client.login(email, password)
    client.checkin()
