# blog个人学习博客
### 如何安装linux系统
* [虚拟机安装](https://xiedaimala.com/tasks/11ad5683-7e18-4883-879d-8425e6a6ceb7video_tutorials/7e65ef68-50e1-49a8-9c44-7f9b2772d0ae)
#### 单系统安装linux
1. U盘制作,注意ios文件不要解压，不要放在U盘
2. [BIOS设置](https://ywnz.com/linuxjc/3803.html)
#### linux下安装软件
* [安装ss](https://github.com/Shadowsocks-Wiki/shadowsocks/blob/master/6-linux-setup-guide-cn.md)

#### [ubuntu卸载Chromium](https://www.jianshu.com/p/3d4c4d415442)


### vs code配置
* [去除vscode编辑器pylink绿色波浪线](https://www.jianshu.com/p/6a125a2ae7f2)
* [快捷键设置](https://jingyan.baidu.com/article/9faa7231ef1383473c28cb12.html)
* git免密码
```
git config  credential.helper store     
```
### pycharm配置
* [去除绿色warning波浪线](https://blog.csdn.net/xiemanr/article/details/72583718)
* 字符替换：Ctrl+R
* [如何从vs code上传项目至Github](https://www.jianshu.com/p/154322554d9d)
* [代码整体左移或右移](https://blog.csdn.net/yihaizhiyan/article/details/39529659)
* md预览:ctrl+shift+v
* [在vscode添加python运行终端run code](https://blog.csdn.net/qq_36770306/article/details/83782451)
* [打开终端](https://blog.csdn.net/MengRui2333/article/details/82707948)
* [设置断点，关键是将【program】字段的值修改为自己程序的入口文件](https://www.jianshu.com/p/dfa9595d74bf)
* [插件：JavaScript (ES6) code snippets的快捷键](https://www.jianshu.com/p/c56ea43b2b34)
* vscode选中相同内容:ctrl+shift+L
* vs code 代码格式化(On Ubuntu): Ctrl + Shift + I

#### vim
* [vi编辑模式中按方向键变ABCD的解决方法](https://blog.csdn.net/leem1986/article/details/80100804)
* [vim /etc/profile 写入时 出现 E121:无法打开并写入文件解决方案](https://blog.csdn.net/cuiyaoqiang/article/details/78967694)
* 启动vim
```
vi /a.text
```
* 进入编辑模式
```
按i键
```
* 退出编辑模式
```
按esc键
```
* 保存文件并推出vim
```
:wq
```

#### webstorm
1. shift+shift(注意必须在zh模式下)t
  * 打开快捷键搜索框
  * 查询reformat快捷键：在搜索框输入
2. shift+shift->vcs
  * 展示可行的git操作
3. 修改快捷键
  * File->Settings->Keymap->搜索vcs  
4. 必要的设置
 * Settings->搜索unsign->Allow打钩
5. css模糊搜索(jsi->justify-content)
 * Settings->搜索emmet->CSS->第二个选项打钩
6. Local Histrory：查看本地修改记录
7. 批量修改作用域内所有变量名
 * 选中一个，右击 refactor
8. Button.log 按 Tab 键
```
console.log(Button)
```

#### linux学习
那个，本机没有Desktop,只有桌面
* 主目录
> 第一次登陆终端时的工作目录将被设置为主目录。在本机中为home/zhq。注意终端中当前工作目录为主目录和根目录时不显示
* 根目录
> 本机根目录为计算机,即bin的父目录
* pwd
> 显示当前工作目录
* cd /home
> 切换到根目录下的home目录
* cd ..
> 切换至当前工作目录的父目录
cd -
> 回到上一个工作目录(可能父级，可能子级)
* cd ./zhq
> 切换至当前工作目录的子目录zhq,注意./常被省略
* ls
> 当前目录的文件和目录
* cp
> 复制文件河目录
* 进入以lin开头的文件
> cd lin*
* 打开当前目录子目录
> gnome-open .
* 创建文件
> touch .gitignore
* 为命令创建别名[解决Linux系统在设置alias命令重启后失效的问题](https://blog.csdn.net/qianfu111/article/details/45221131)
> alias zz='. ~/.zshrc'
* 删除别名
> unalias zz
* 编辑bashrc文件
> vim ~/.bashrc
* 在当前目录下创建package.json文件
> npm init -y
* [如何取消一个目录的git初始化](https://segmentfault.com/q/1010000006717152)
> rm -rf .git
* 在linux中,80端口是不能被普通用户使用的，要使用必须加sudo
```
sudo node server.js 80
```
* [ubuntu录制gif](https://jingyan.baidu.com/article/15622f24239a43fdfcbea53e.html)
* linux截图
```
gnome-screenshot -a
```
* 命令行清屏(命令历史记录不会清除，仍能通过方向键访问) 
```
clear
```
* 光标跳至行首
CTRL+A
* 光标跳至行尾
CTRL+E
