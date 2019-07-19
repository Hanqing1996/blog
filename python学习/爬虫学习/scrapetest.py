from urllib.request import urlopen 
html=urlopen("https://www.zhihu.com/")
print(html.read()); 