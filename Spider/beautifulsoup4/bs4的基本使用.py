from bs4 import BeautifulSoup

# 解析本地文件

soup = BeautifulSoup(open('../source/bs4解析.html',encoding='utf-8'),'lxml')
# print(soup)
# 找到的是第一个符合条件的数据
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4 的一些函数

# find
# 返回的是第一个符合条件的数据

print(soup.find('a'))
print(soup.find('a',title='a2'))
# 根据class_的值找到对象
print(soup.find('a',class_='ab'))


# find_all

print(soup.find_all('a'))
# selecte


