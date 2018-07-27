# coding:utf-8 :)
# author:gyk

import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)

        #请求失败的话
        if response.getcode()!=200:
            return None

        #返回下载好的内容
        return response.read()
