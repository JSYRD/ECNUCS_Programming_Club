python打包
=====

[点击下载本文档PDF](https://raw.githubusercontent.com/JSYRD/ECNUCS_Programming_Club/main/Clubbbbbb/PackageUpCourse/python打包.pdf)

需要用到的工具：

* Inno Setup Compiler [点击下载](https://raw.githubusercontent.com/JSYRD/ECNUCS_Programming_Club/main/Clubbbbbb/PackageUpCourse/innosetup-6.2.0.exe)

* Pyinstaller 安装方法见下文

大致分为两步，先用pyinstaller把python文件打包为exe文件，再用Inno Setup Compiler将包打包成安装文件。

## 下载工具并安装

Pyinstaller的安装方法：

打开命令行并输入

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

安装完成后即可使用。全面的详细使用方法可自行百度或参考 [此处](https://pyinstaller.readthedocs.io/en/stable/spec-files.html)



## 用pyinstaller将python文件打包为exe文件

* 以Lecture4的源代码为例

![image-20211231231040327](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20211231231040327.png)

这是Lecture4源代码和相关资源的存放文件夹，在此处打开cmd（方法为在上方地址栏输入cmd，回车）

![image-20211231230956108](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20211231230956108.png)

输入

```shell
pyi-makespec main.py
```

main.py代表你的游戏主循环运行的py文件。执行完成后会生成一个main.spec文件，用文本编辑器打开。（pycharm, vscode或者记事本都可以）

![image-20220101020528645](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220101020528645.png)

初始内容如上图。参数意义如下：

* Analysis(scripts, pure, pathex, binaries, datas):

  > 用于定义Python源文件，包括搜索路径和源文件名等。
  >
  > 一般情况下，这里我们需要修改的地方有：
  >
  > * 第一个scripts源文件名。包含你所需要打包的python文件（这里有个小tip，如果需要打包的python文件在已经被打包的py文件所import了，就无需再进行填写了。例如这里components文件夹内有许多需要打包的python文件，但并不需要再单独填写了），初始自带你生成这个spec文件时的python文件名。格式和已经给的内容格式相同。
  >
  > * 第二个pure python modules，指被scripts需要的pure python modules。一般不需填写。
  >
  > * 第三个pathex是一个list， 指imports的包的路径。一般也不需要填写。
  >
  > * 第四个binaries，指被scripts需要的非python modules二进制文件（比如DLL文件）。一般也不需要填写。
  >
  > * 第五个datas，指需要打包的其他文件（也就是图片之类的数据文件），需要填写，例如Lecture4中需要打包的其他文件有文件夹components, data, fonts等，那么就按照以下格式填写：
  >
  >   ```python
  >   datas=[('components','.\\components'),('data','.\\data'),('fonts','.\\fonts'),('images','.\\images'),('gameState','.\\gameState')]
  >   ```
  >
  > * 其余选项一般不需填写。

未提到的详细信息可查看 [官方文档](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) 。

填写完毕后即可进行打包。在终端执行：

```shell
pyinstaller main.spec -w
```

执行就会自动开始打包。完成后会多出build和dist两个文件夹。其中build文件夹是临时文件，可以删除。dist文件夹就是打包完成的成品。在dist/main/文件夹里有一个可执行文件（main.exe或者自定义的其它名字（在spec文件中 EXE的选项中有name=''可以自行修改）。）

如果运行该exe文件没有问题。则pyinstaller打包结束，否则考虑填写格式错误或者缺失文件。



----



## 用Inno setup compiler将文件打包为安装文件

在pyinstaller打包结束后还需要使用Inno setup compiler打包为安装文件。

安装Inno setup compiler并打开。

![image-20220110221254550](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110221254550.png)

* 选择 `Create a new script file using the Script Wizard`



![image-20220110221353242](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110221353242.png)

* 不勾选 `Create a new empty script file`



![image-20220110221445708](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110221445708.png)

* 填写相应信息，应用名称，版本，发布方名称，官网等。



![image-20220110221623819](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110221623819.png)

* 填写`Application folder name`， 也就是这些东西安装之后的文件夹名字。



![image-20220110230600083](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110230600083.png)

* 选择要打包的exe文件和文件夹，也就是之前的游戏exe文件和文件夹，在dist目录下。这里上面选择Browse选择main.exe，下面选择Add folder，把整个main文件夹都加进去。



![image-20220110230620433](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110230620433.png)

* 选择是否将某个文件格式与之关联。比如你自己自定义了一个文件格式，那么就可以选择将这个后缀的文件与你的应用关联。



![image-20220110230717224](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110230717224.png)

* 选择是否向开始菜单中加入一个快捷方式。
* 选择是否允许用户创建一个桌面快捷方式。



![image-20220110230828422](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110230828422.png)

* 选择相应的说明文件（可选）。



![image-20220110230850088](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110230850088.png)

* 选择安装的模式。



![image-20220110230910492](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110230910492.png)

* 选择可使用的语言。这里需要注意，本身Inno setup compiler是不带中文语言包的，需要可以自行搜索。



![image-20220110231137628](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110231137628.png)

* 这里注意，是你的安装包输出设置。第一个是输出位置，例如桌面。第二个是文件名。第三个是图标（可选），第四个是安装密码（如果不设置密码可忽略）。



![image-20220110231213614](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110231213614.png)

* 直接Next即可。



![image-20220110231235098](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110231235098.png)

* 完成后选择立即编译。



![image-20220110231304259](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110231304259.png)

* 这里可能会提示是否保存。这里保存的是打包的配置文件，可以选择保存到某位置。



完成后就会开始编译。编译完成后就会在刚才选定的位置生成一个安装包。

![image-20220110231438090](C:\Users\FLOWERNOTFLOWER\AppData\Roaming\Typora\typora-user-images\image-20220110231438090.png)



这就是成品了。发给你的好朋友让别人玩玩你的游戏吧！



*By JSYRD*