[Markdown语法](https://www.jianshu.com/p/q81RER)<br>
[git安装及使用](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)<br>
[Git-Bash教程](https://xiedaimala.com/tasks/ac98cafe-86d3-4842-81f6-d0eec4930e80/text_tutorials/354cf717-8e2d-41fe-9f6f-456935c12967)<br>
[SSH的配置，推荐看这篇](https://www.jianshu.com/p/d136dee10561)<br>
[git加速](https://jscode.me/t/topic/789)<br>
[github桌面版下载（图形界面代替命令行）](https://desktop.github.com/)<br>
[github桌面版使用流程](https://www.jianshu.com/p/6063974849db)<br>
#### 常用命令
> clone：将远程仓库复制至本地，适用于远程有仓库、本地无仓库的情况

> add：将本地仓库复制至远程，适用于远程无仓库、本地有仓库的情况

> push：将针对本地仓库所做的修改上交至远程仓库

> pull：将针对远程仓库所做的修改下拉至远程仓库

> commit：push、pull的前置操作
#### 删除github上的编辑器配置文件(.idea,.vscode等)，并在push时忽略配置文件
* [参考](https://blog.csdn.net/leorx01/article/details/66968707)
* 流程(首先pull一下)
1. 创建.gitignore文件
2. 将.vscode文件移入.gitignore文件(可通过插件ignore "g" it实现)，用于设置下次提交时忽略.vscode文件
3. 在缓存区中移除.vscode(注意本地文件夹中仍有.vscode文件,未删除也不可删除)
这一步的作用是删除远程仓库(即github上)的.vscode文件,node_modules同理
```
git rm --cached -r .vscode
```
3. commit,push
