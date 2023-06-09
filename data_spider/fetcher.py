import requests
import urllib3
import brotli

from requests_html import HTMLSession
from .exceptions import FetchError
from .utils import UserAgentPool, Logs, Log

urllib3.disable_warnings()


class Fetcher:
    def __init__(self, use_dynamic: bool, log: Log = Log()):
        self.__use_dynamic = use_dynamic
        self.__session = HTMLSession()
        self.ua_tool = UserAgentPool()
        self.__headers = {
            'User-Agent': self.ua_tool.get_random_user_agent("pc", "chrome"),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Referer': "",
            'Upgrade-Insecure-Requests': '1',
        }
        self.log = log
        self.log.set(Logs.HEADERS, f"The current Headers information is as follows: {self.__headers}")
        self.log.set(Logs.UA, f"The UA currently in use is: {self.__headers.get('User-Agent', None)}")

    def get_header(self, key):
        return self.__headers.get(key, None)

    def update_refer(self, url: str):
        self.__headers.update({"Referer": url})

    def update_headers(self, headers: dict):
        self.__headers.update(headers)
        return self.__headers

    def override_headers(self, headers: dict):
        self.__headers = headers
        return self.__headers

    def clear_headers(self):
        self.__headers.clear()

    def delete_header(self, header_key: str):
        try:
            return self.__headers.pop(header_key)
        except KeyError:
            return None

    def fetch(self, url: str):
        try:
            response = self.__session.get(url, headers=self.__headers, verify=False) \
                if self.__use_dynamic else requests.get(url, headers=self.__headers, verify=False)
            if response.headers.get('Content-Encoding') == 'br':
                response = brotli.decompress(response.content).decode('utf-8')
            else:
                response = response.text
            self.log.set(Logs.SOURCE_RESPONSE, response)
            return response
        except Exception as e:
            raise FetchError(f"Failed to fetch {url}: {e}")
