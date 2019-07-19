#### 视频
[Django入门与实战](http://www.imooc.com/learn/790)

#### 命令
创建项目
```
django-admin startproject mydemo
```
启动服务器（然后直接访问http://127.0.0.1:8000/ 或者localhost:8000）
```
python manage.py runserver
```
创建应用（记得把应用名添加到settings.py的INSTALLED_APPS中）
```
python manage.py startapp demo
```
生成数据表
```
python manage.py makemigrations demo
```
```
python manage.py migrate
```
查看sql语句
```
python manage.py sqlmigrate demo 0001
```
创建超级用户（必须在cmd中执行，用Git Bash会报错）
```
python manage.py createsuperuser
```
打开一个交互式命令行
```
python manage.py shell
```
#### 注意事项
* 一个项目有一个INSTALLED_APPS，有多个应用，这些应用的名字都写在INSTALLED_APPS中
* 一个应用有一个templates文件夹
* Django会按照INSTALLED_APPS查找Templates，所以不同应用下templates文件夹中的同名.html文件会发生冲突，解决方法是把.html文件放入以应用名命名的文件夹中





