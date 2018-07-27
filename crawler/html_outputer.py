# coding:utf-8 :)
# author:gyk

import xlwt
import sys
import pymysql
reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # def output_html(self):
        book = xlwt.Workbook(encoding='utf-8')
        sheet=book.add_sheet('News',cell_overwrite_ok='True')
        sheet.write(0, 0, 'url')
        sheet.write(0, 1, 'title')
        sheet.write(0, 2, 'text')
        hang=1

        for data in self.datas:
            sheet.write(hang, 0, data['url'].decode('UTF-8'))
            sheet.write(hang, 1, data['title'].decode('UTF-8'))
            sheet.write(hang, 2, data['text'].decode('utf-8'))
            hang=hang+1
        book.save('/Users/gyk/Desktop/output.xls')

    # def __init__(self):
    #     # 打开数据库连接
    #     # 这里是连接数据库
    #     self.conn = pymysql.connect(
    #         # host
    #         host='localhost',
    #         # 3306
    #         port=3306,
    #         user='root',
    #         # 密码已修改
    #         passwd='123456',
    #         # 数据库名称
    #         db='crawler_news',
    #         # 编码方式
    #         charset="utf8"
    #     )
    #     # 获取游标
    #     self.cur = self.conn.cursor()
    #
    #     # 建表
    #     self.cur.execute("DROP TABLE IF EXISTS crawler_txt")
    #
    #     sql1 = """CREATE TABLE crawler_txt (
    #                      URL  CHAR(100) NOT NULL,
    #                      TITLE CHAR(250) ,
    #                      COMMENT_TXT VARCHAR(15000))"""
    #     # 执行语句
    #     self.cur.execute(sql1)
    #
    #     # 创建一个list
    #     self.datas = []
    #
    # def collect_data(self, data):
    #     if data is None:
    #         return
    #     self.datas.append(data)
    #
    # def output_html(self):
    #     # 创建数据表
    #     # 遍历
    #     for data in self.datas:
    #         # 遍历
    #         for i in data:
    #             #print ("Name:",dict['Name'])
    #             #Name:jeo
    #             try:
    #                 self.cur.execute('insert into crawler_txt values("%s","%s","%s")' % (
    #                     i['url'].decode('UTF-8'),
    #                     i['title'].decode('UTF-8'),
    #                     i['summary']))
    #             except:
    #                 continue
    #
    #             # 提交到数据库执行
    #             self.conn.commit()
    #
    #     self.datas = []
    #
    # def output(self):
    #
    #     self.conn.close()