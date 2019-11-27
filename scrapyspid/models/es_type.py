
# -*- coding:utf-8 -*-

from elasticsearch_dsl import DocType,Nested,Date,Boolean,analyzer,Completion,Text,Keyword,Integer
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="http://192.168.4.19:31802/")

class ArticleType(DocType):
    # 文章类型
    #title = Text(analyzer="ik_max_word")
    create_date = Date()

    ranking = Keyword()
    movie_name = Keyword()

    score = Keyword()
    score_num = Keyword()


    #tags = Text(analyzer="ik_max_word")
    #content = Text(analyzer="ik_max_word")

    class Meta:
        # 数据库名称和表名称
        index = "douban"
        doc_type = "movice"

if __name__ == '__main__':
    ArticleType.init()

