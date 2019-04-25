import sys
import base64
import requests
import urllib

class Utils:
    """docstring for Utils"""
    def __init__(self):
        self._session = requests.Session()

    def urlEncode(self, url, path, params=[]):
        try:        # Works with python 2.x
            return url + path + '?' + urllib.urlencode(params)
        except:     # Works with python 3.x
            return url + path + '?' + urllib.parse.urlencode(params)

    def optionsContent(self, url, data=None, headers=None):
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None):
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        return self._session.delete(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        return self._session.put(url, headers=headers, data=data)
