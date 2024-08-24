# metamask_selenium_connectDapp

自动化 链接钱包

## Getting started

### 1、安装比特浏览器 https://www.bitbrowser.cn/ 注册登陆
### 2、打开比特浏览器，打开扩展中心，勾选metamask
### 3、打开比特浏览器，打开浏览器窗口，创建窗口，选择账户平台，选择其他平台，点击确定
### 4、使用requirements.txt 创建虚拟环境，或者poetry创建虚拟环境。运行main

注意
### 1、打开vpn
### 2、比特浏览器需要先启动，但不用打开创建的浏览器窗口
### 3、浏览器操作会有记录插件缓存，再次运行本脚本，会和第一次运行效果不同，所以需要删除浏览器窗口，删除方法，浏览器窗口-选中要删除的浏览器-更多操作-删除
### 4、poetry.toml 配置文件 cache-dir 是poetry的缓存文件，可以设置自己项目路径，若不使用poetry 则可不管
### 5、chromedriver版本会默认最新版本，系统中修改模板设置后不生效，使用代码也无法创建低版本的chromedriver，需要创建后手动修改chromedriver
