# 使用BeautifulSoup解析网页

import requests
import pandas
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

movie_list = []

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class':'movie-item-hover'},limit=10):
    # for atag in tags.find_all('a'):
    #     print(atag.get('href'))
    #     # 获取所有链接
    #     print(atag.find('span').text)
    #     # 获取电影名字
    name = tags.find(class_='name').text
    movie_info = tags.find_all(class_='movie-hover-title')
    genre = movie_info[1].text.strip()
    time = movie_info[3].text.strip()
    movie_summary = {'name': name, 'genre': genre, 'time': time }
    movie_list.append(movie_summary)

print(bs_info)
print(bs_info.find_all('div', attrs={'class':'movie-item-hover'},limit=10))

# print(movie_list)

movie_csv = pandas.DataFrame(movie_list)

movie_csv.to_csv('./movie_first_10.csv', encoding='utf8', index=False, header=False)