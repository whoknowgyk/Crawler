# coding:utf-8 :)
# author:gyk

from bs4 import BeautifulSoup
import re

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        #将结果传到一个列表里面
        new_urls=set()
        #匹配正则表达式
        links = soup.find_all('a', href=re.compile(r"http://www.sohu.com/a/*?"))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    #解析数据，需要解析title和summary两个数据
    def _get_new_data(self, page_url, soup):
        #建立一个字典来存放数据
        data=[]
        res_data = {}

        res_data['url']=page_url
        title_node = soup.find('div',class_="text-title").find("h1")
        res_data['title']=title_node.get_text()
        summary_all = soup.find_all("p")
        s=''
        for summary in summary_all:
            s=s+summary.get_text().strip()#消除空格,合并正文数据
        res_data['summary'] = s
        data.append(res_data)
        return data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_data=self._get_new_data(page_url,soup)
        return new_data

    def url_parser(self,url,html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(url,soup)
        return new_urls