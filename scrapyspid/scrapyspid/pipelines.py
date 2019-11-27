# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from w3lib.html import remove_tags

from models.es_type import ArticleType



class ScrapyspidPipeline(object):
    def process_item(self, item, spider):
        article = ArticleType()

        article.ranking = item['ranking']
        article.movie_name = item['movie_name']

        article.content = item['score_num']
        article.score = item['score']

        # article.front_image_url = item['front_image_url']
        # if "front_image_path" in item:
        #     article.front_image_path = item['front_image_path']
        #
        # article.fav_nums = item['fav_nums']
        # article.comment_nums = item['comment_nums']
        # article.praise_nums = item['praise_nums']
        #
        # article.url = item['url']
        # article.meta.id = item['url_object_id']

        article.save()

        return item
