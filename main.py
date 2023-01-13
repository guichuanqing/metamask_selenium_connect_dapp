import time

from metamask_selenium_connectdapp.BitBrowser.bitbrowser import BitBrowser
from metamask_selenium_connectdapp.MetaMask.metamasksetup import metamask
from metamask_selenium_connectdapp.DAPP.dapp import dappclick

if __name__ == '__main__':
    # 使用示例
    # 使用前，安装依赖：
    # pip install requests selenium faker loguru
    # 请自行将104版本的chromedriver.exe和脚本放同一个目录下

    website = 'twitter'  # 网站名称，创建浏览器和查询浏览器时需要用到
    # 创建对象
    bit = BitBrowser(website)
    # 创建并打开浏览器
    # 创建浏览器，必传参数：username,password,proxyType,proxyIp,proxyPort,proxyUsername,proxyPassword
    # 即：用户名，密码，代理类型，代理ip，代理端口，代理用户名，代理密码
    # - 其他参数可以通过kwargs传入，也可以不传
    # - 传入的代理类型，如果不是在['noproxy', 'http', 'https', 'socks5']中，默认为提取代理，脚本会设置proxyMethod=3, proxyIp为提取链接，传入dynamicIpUrl
    driver, browser_id = bit.get_driver(username=f'', password='', proxyType='noproxy',
                                        proxyIp='', proxyPort='', proxyUsername='', proxyPassword='', dynamicIpUrl='')

    print("等待浏览器完全启动")
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://app.uniswap.org/')
    time.sleep(3)

    # 小狐狸插件的ID
    EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/home.html'.format(EXTENSION_ID))

    time.sleep(3)

    # 导入助记词
    recoveryPhrase = "cloud shove firm between fog faculty photo early output artwork woman scatter"
    metamask.metamaskSetup(driver, recoveryPhrase, "66666666")

    # 点击 窗口0 dapp 登陆按钮

    driver.switch_to.window(driver.window_handles[0])
    dappclick(driver)
    time.sleep(4)

    # 获取当前窗口所有句柄
    all_windows = driver.window_handles
    # 获取当前标签页窗口句柄
    current_window = driver.current_window_handle
    print(all_windows)
    print(current_window)

    # 窗口 2 是小狐狸小弹窗
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(2)
    print("切换后的窗口名称是：", driver.title)
    metamask.connectDapp(driver)

    # # 关闭浏览器
    # bit.close_browser(browser_id)
    # # # 删除浏览器
    # bit.del_browser(browser_id)

    # from undetected_chromedriver import Chrome
    # driver = Chrome(version_main=107)
