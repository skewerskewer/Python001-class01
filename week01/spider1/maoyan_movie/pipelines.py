# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# 注册到settings.py文件的ITEM_PIPELINES中，激活组件

import pandas

class MaoyanmoviePipeline:
#    def process_item(self, item, spider):
#        return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        name= item['name']
        genre = item['genre']
        time = item['time']
        output = [f'|{name}|\t|{genre}|\t|{time}|\n\n']
        
        movie = pandas.DataFrame(data=output)
        movie.to_csv('./maoyan_movie.csv', mode='a', encoding='utf8',index=False, header=False)


