[Markdown语法](https://www.jianshu.com/p/q81RER)<br>
[git安装及使用](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)<br>
[Git-Bash教程](https://xiedaimala.com/tasks/ac98cafe-86d3-4842-81f6-d0eec4930e80/text_tutorials/354cf717-8e2d-41fe-9f6f-456935c12967)<br>
[SSH的配置，推荐看这篇](https://www.jianshu.com/p/d136dee10561)<br>
[git加速](https://jscode.me/t/topic/789)<br>
[github桌面版下载（图形界面代替命令行）](https://desktop.github.com/)<br>
[github桌面版使用流程](https://www.jianshu.com/p/6063974849db)<br>

[push 时报错：fatal: The current branch master has no upstream branch.](https://blog.csdn.net/benben_2015/article/details/78803753)
#### 常用命令
> clone：将远程仓库复制至本地，适用于远程有仓库、本地无仓库的情况

> add：将本地仓库复制至远程，适用于远程无仓库、本地有仓库的情况

> push：将针对本地仓库所做的修改上交至远程仓库

> pull：将针对远程仓库所做的修改下拉至远程仓库

> commit：push、pull的前置操作

#### git clone https://github.com/Hanqing1996/react-wheels.git .
> . 表示当前目录。意为在当前目录下创建 react-wheels 文件夹

#### 在github上下载单个文件夹
> 比如我要单独下载redux/examples 下的[ counter 目录](https://github.com/reduxjs/redux/tree/master/examples/counter) 
1. 找一个临时目录，初始化 git
```
git init
```
2. 配置 sparseCheckout
```
git config core.sparseCheckout true
```
3. 与目的文件夹所在远程仓库建立联系
```
git remote add -f origin https://github.com/reduxjs/redux.git
```
4. echo 目的文件路径 >> .git/info/sparse-checkout
```
echo examples/counter >> .git/info/sparse-checkout
```
5. pull 就完事了
```
git pull origin master
```
 
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

#### branch
* 参考
  * [一个年轻人的Git笔记](https://www.cnblogs.com/fydeblog/p/9513736.html#2045321468)
  * [官方文档](https://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6)
* 一个关于master的大坑
```
master分支在第一次add和commit前是不会创建的。所以git init后无法直接创建新分支，必须先在master进行一次add和commit。
```
* 在 branch_A 进行 commit 后，如果创建并切换至 branch_B,在 git bash 中是看不到待 add 的文件的。这是因为 branch_B 是在 branch_A 进行 commit 后创建的，是 branch_A 进度的一个副本。
* 对于 remote 的一个分支，本地应该只有一个仓库
* 查看当前所处分支
```
git branch
```
* 创建分支（创建分支后不会自动切换到所创建的分支）
```
git branch testing
```
* 切换分支
```
git checkout testing
```
* 创建新的分支并切换到新的分支
```
git checkout -b new_branch 
```
* 推送本地分支至远程仓库
```
git push origin button-and-input:button-and-input
```
* 从查看当前分支的commit历史
```
git log
```
* git log如何退出
```
q
```
* HEAD -> master, testing 的意思是：HEAD 说当前分支是 master，而且 testing 与 master 指向同一个 commit
* 切换至 master 分支，合并iss53分支
```
git branch master
git merge iss53
```
* 如何解决分支冲突：逻辑上说，这种问题只能由人来裁决
  * git status查看冲突的文件
  * 手动处理去除的内容（git会在merge失败后显示diff）
  * git add 1.js
  * git commit -m"冲突已解决"
*  在开始新工作前，保存当前进度的正确姿势
```
git branch currentVersion // 只创建分支，不切换。currentVersion 相当于副本，保存到当前为止所有信息
do something // 开始新工作
git add somefiles
git commit -m"开始新工作" // 由于是在 master 上提交的，currentVersion 不包含新工作信息
```
也就是说，想要保存当前进度，只要新建一个分支。无需其它多余的操作。

#### 跟踪,暂存区等概念
* [参考](https://www.cnblogs.com/fydeblog/p/9513736.html#2045321468)
* git add
未跟踪的文件(Untracked files)/尚未暂存以备提交的变更： => 要提交的变更(Changes to be committed)

* git　commit

* 您的分支领先 'origin/master' 共 4 个提交
我 commit 了４次，还没 push 

#### 把代码提交到其他用户的仓库的某一分支
1. 添加远程仓库 
```
git remote add otherusersorigin https://github.com/user2/user2-project.git
```
 * 删除远程仓库
 ```
 git remote rm otherusersorigin
 ```
 * 查看目前所设置的远程仓库
 ```
 git remote -v
 ```
2. 创建并切换分支
```
git branch zhq
git checkout zhq
```
 * [git 错误 fatal: Not a valid object name: 'master'.](https://blog.csdn.net/hengyunabc/article/details/6058145)
3.推送本地的zhq分支到远程otherusersorigin的zhq分支(没有会自动创建)
```
$  git push otherusersorigin zhq:zhq 
```
4. 之后push只需要
```
git push otherusersorigin zhq:zhq
```

#### 已有远程仓库，建立本地仓库
> clone:拉取远程仓库数据到本地，并自动建立与远程仓库建立联系
```
// 该命令将在当前目录下生成JavaScript-advance文件夹
git clone https://github.com/Hanqing1996/JavaScript-advance.git
```
此时，JavaScript-advance已经是一个远程仓库了，我们可以随意的add,commit,push
