# coding:utf-8 :)
# author:gyk


from crawler import url_manager, html_downloader, html_parser, html_outputer
import selenium


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
        self.count=1


    def root_url_craw(self,root_url_front,root_url_medium,num,root_url_rear):
        new_urls=set()
        count_list=1
        while 1:
            root_url_num_of_list=num-count_list+1
            #拼接URL
            root_url = root_url_front + root_url_medium + str(root_url_num_of_list) + root_url_rear
            #下载对应页面
            root_html_cont = self.downloader.download(root_url)
            #得到新的URL
            new_urls = self.parser.url_parser(root_url, root_html_cont)
            #将新的URL添加进URL管理器
            self.urls.add_new_urls(new_urls)
            #爬取
            self.craw()
            #计数
            if self.count==50:
                break
            count_list=count_list+1


    def craw(self):
        while self.urls.has_new_url():#如果有待爬取的url
            try:
                new_url=self.urls.get_new_url()#取一个出来
                print 'craw %d : %s' %(self.count,new_url)
                html_cont=self.downloader.download(new_url)#下载对应的页面
                new_data=self.parser.parse(new_url,html_cont)#下载好以后，进行页面的解析，得到新的数据
                #self.urls.add_new_urls(new_urls)#将新的url补进url管理器
                self.outputer.collect_data(new_data)#同时进行数据的收集
                if self.count==50:
                    break

                self.count=self.count+1
            except:
                print 'craw failed'

        self.outputer.output_html()#输出收集好的数据

#main函数
if __name__=="__main__":
    #设置入口url
    kind_name=raw_input('please input the kind of news:')
    num=int(raw_input('please input num of list:'))
    #肢解url
    root_url_front="http://news.sohu.com/"
    root_url_medium=kind_name+'_'
    root_url_num_of_list=num
    root_url_rear=".shtml"
    obj_spider=SpiderMain()
    #启动爬虫
    obj_spider.root_url_craw(root_url_front,root_url_medium,root_url_num_of_list,root_url_rear)