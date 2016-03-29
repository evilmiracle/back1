#!/usr/bin/python
# -*- coding: UTF-8 -*-

into =[]
from bs4 import BeautifulSoup
import os
#with open('D:/Plan-for-combating-master/week1/1_2/1_2code_of_video/web/new_index.html','r') as wb_data:
Soup = BeautifulSoup(open('D:/Plan-for-combating-master/week1/1_2/1_2code_of_video/web/new_index.html'),'lxml')
images = Soup.select('body > div.main-content > ul > li > img')
titles = Soup.select('body > div.main-content > ul > li  > div.article-info > h3 > a')
descs = Soup.select('body > div.main-content > ul > li  > div.article-info > p.description')
rates = Soup.select('body > div.main-content > ul > li  > div.rate > span')
cates = Soup.select('body > div.main-content > ul > li  > div.article-info > p.meta-info')
#print cates
	#print images,titles,desc,rates,cates

for title,image,desc,rate,cate in zip(titles,images,descs,rates,cates):
	data = {
		'title':title.get_text(),
		'desc' :desc.get_text(),
		'rate' :rate.get_text(),
		'cate' :cate.get_text(),
		'image':image.get('src')
	}
	into.append(data)
for i in into:
	if float(i['rate'])>3:
		print i['title'],i['cate']
