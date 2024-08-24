import os
import time
import random
import requests
import json
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


webgl_vendors = ['Google Inc.']
webgl_renders = ['ANGLE (Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) HD Graphics 5300 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) HD Graphics 620 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) HD Graphics 620 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (Intel(R) HD Graphics Direct3D11 vs_4_1 ps_4_1)', 'ANGLE (NVIDIA GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 1660 Ti Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) HD Graphics Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) HD Graphics Family Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (Intel(R) HD Graphics 4400 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 750 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro K600 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro M1000M Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (AMD Radeon (TM) R9 370 Series Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (AMD Radeon HD 7700 Series Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 750  Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 760 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 750 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 750 Ti Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 760 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 770 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 780 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 850M Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 850M Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 860M Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 950 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 950 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 950M Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 950M Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 960 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 960 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 960M Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 960M Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 970 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 970 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 980 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 980 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce GTX 980 Ti Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce GTX 980M Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce MX130 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce MX150 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce MX230 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce MX250 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce RTX 2060 Direct3D9Ex vs_3_0 ps_3_0)', 'ANGLE (NVIDIA GeForce RTX 2060 SUPER Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA GeForce RTX 2070 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro K620 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro FX 380 Direct3D11 vs_4_0 ps_4_0)', 'ANGLE (NVIDIA Quadro NVS 295 Direct3D11 vs_4_0 ps_4_0)', 'ANGLE (NVIDIA Quadro P1000 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro P2000 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro P400 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro P4000 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro P600 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (NVIDIA Quadro P620 Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (ATI Mobility Radeon HD 4330 Direct3D11 vs_4_1 ps_4_1)', 'ANGLE (ATI Mobility Radeon HD 4500 Series Direct3D11 vs_4_1 ps_4_1)', 'ANGLE (ATI Mobility Radeon HD 5000 Series Direct3D11 vs_5_0 ps_5_0)', 'ANGLE (ATI Mobility Radeon HD 5400 Series Direct3D11 vs_5_0 ps_5_0)',
                 'ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.8935)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1070 Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6079)', 'ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11-26.20.100.7870)', 'ANGLE (AMD, Radeon (TM) RX 470 Graphics Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.1034.6)', 'ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.8681)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-10.18.13.6881)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 970 Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.5671)', 'ANGLE (AMD, AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.14028.11002)', 'ANGLE (Intel, Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.8681)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 750 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.5671)', 'ANGLE (AMD, AMD Radeon RX 5700 XT Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.13025.1000)', 'ANGLE (AMD, AMD Radeon RX 6900 XT Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.13011.1004)', 'ANGLE (AMD, AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.13002.23)', 'ANGLE (Intel, Intel(R) HD Graphics 530 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.9466)', 'ANGLE (Intel, Intel(R) HD Graphics 5500 Direct3D11 vs_5_0 ps_5_0, D3D11-20.19.15.5126)', 'ANGLE (Intel, Intel(R) HD Graphics 6000 Direct3D11 vs_5_0 ps_5_0, D3D11-20.19.15.5126)', 'ANGLE (Intel, Intel(R) HD Graphics 610 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.9466)', 'ANGLE (Intel, Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.9168)', 'ANGLE (Intel, Intel(R) HD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6589)', 'ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.100.9126)', 'ANGLE (Intel, Mesa Intel(R) UHD Graphics 620 (KBL GT2), OpenGL 4.6 (Core Profile) Mesa 21.2.2)', 'ANGLE (NVIDIA Corporation, GeForce GTX 1050 Ti/PCIe/SSE2, OpenGL 4.5.0 NVIDIA 460.73.01)', 'ANGLE (NVIDIA Corporation, GeForce GTX 1050 Ti/PCIe/SSE2, OpenGL 4.5.0 NVIDIA 460.80)', 'ANGLE (NVIDIA Corporation, GeForce GTX 1050/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 1060 6GB/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 1080 Ti/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 1650/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 650/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 750 Ti/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 860M/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce GTX 950M/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce MX150/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, GeForce RTX 2070/PCIe/SSE2, OpenGL 4.5 core)', 'ANGLE (NVIDIA Corporation, NVIDIA GeForce GTX 660/PCIe/SSE2, OpenGL 4.5.0 NVIDIA 470.57.02)', 'ANGLE (NVIDIA Corporation, NVIDIA GeForce RTX 2060 SUPER/PCIe/SSE2, OpenGL 4.5.0 NVIDIA 470.63.01)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Ti Direct3D9Ex vs_3_0 ps_3_0, nvd3dumx.dll-26.21.14.4250)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1060 5GB Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7168)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1060 6GB Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7212)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1070 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6677)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7111)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7212)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7111)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7196)', 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 Ti Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.14.7196)']
color_depths = [1, 2, 3, 4, 5, 8, 12, 15, 16, 18, 24, 30, 32, 48]
systems = ['Win32', 'Linux i686', 'Linux armv7l', 'MacIntel']
payload_config = {
    "groupId": "",  # 群组ID，绑定群组时传入，如果登录的是子账号，则必须赋值，否则会自动分配到主账户下面去
    "platform": '',  # 账号平台
    "platformIcon": 'other',  # 取账号平台的 hostname 或者设置为other
    "url": '',  # 打开的url，多个用,分开
    "name": '',  # 窗口名称
    # 备注
    "remark": '',
    "userName": '',  # 用户账号
    # "password": password,  # 用户密码
    "password": '',  # 用户密码
    "cookie": '',  # cookie
    "proxyMethod": 2,  # 代理类型 2自定义;3提取IP
    # 自定义代理类型 ['noproxy', 'http', 'https', 'socks5']
    "proxyType": 'noproxy',
    "host": '',  # 代理主机
    "port": '',  # 代理端口
    "proxyUserName": '',  # 代理账号
    "proxyPassword": '',  # 代理密码
    'dynamicIpUrl': '',  # proxyMethod = 3时，提取IP链接
    'dynamicIpChannel': '',  # 提取链接服务商，rola | doveip | cloudam | common
    'isDynamicIpChangeIp': False,  # 每次打开都提取新IP，默认false
    # ip检测服务IP库，默认ip-api，选项 ip-api | ip123in | luminati，luminati为Luminati专用
    'ipCheckService': 'ip-api',
    'abortImage': False,  # 是否禁止图片加载
    'abortMedia': False,  # 是否禁止媒体加载
    'stopWhileNetError': False,  # 网络错误时是否停止
    'syncTabs': False,  # 是否同步标签页
    'syncCookies': True,  # 是否同步cookie
    'syncIndexedDb': False,  # 是否同步indexedDB
    'syncBookmarks': True,  # 是否同步书签
    'syncAuthorization': False,  # 是否同步授权
    'syncHistory': True,  # 是否同步历史记录
    'isValidUsername': False,  # 是否验证用户名
    'workbench': 'localserver',
    'allowedSignin': True,  # 允许google账号登录浏览器，默认true
    'syncSessions': False,  # 同步浏览器Sessions，历史记录最近关闭的标签相关，默认false
    'clearCacheFilesBeforeLaunch': False,  # 启动前清理缓存文件，默认false
    'clearCookiesBeforeLaunch': False,  # 启动前清理cookie，默认false
    'clearHistoriesBeforeLaunch': False,  # 启动前清理历史记录，默认false
    'randomFingerprint': False,  # 是否启用随机指纹，默认false
    'disableGpu': False,  # 是否禁用GPU，默认false
    'enableBackgroundMode': False,  # 是否启用后台模式，默认false
    'muteAudio': True,  # 是否静音，默认True
    'coreVersion': '126', # 内核版本，126
    'coreProduct': 'chrome', #内核，chrome
}


class BitBrowser:

    def __init__(self, website):
        self.website = website  # 网站，用于浏览器窗口名称
        self.bit_port = self.get_bit_port()

    @classmethod
    def test_port(cls, port):
        url = f'http://127.0.0.1:{port}'
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                return True
        except:
            import traceback
            traceback.print_exc()
            return False

    @classmethod
    def get_bit_port(cls):
        # 获取比特浏览器的本地端口
        json_file = fr'C:\Users\{os.getlogin()}\AppData\Roaming\bitbrowser\config.json'
        if not os.path.exists(json_file):
            # 尝试枚举
            users = os.listdir('C:/Users')
            for user in users:
                x = fr'C:\Users\{user}\AppData\Roaming\bitbrowser\config.json'
                if os.path.exists(x):
                    json_file = x
                    break
            else:
                logger.error(f'请先安装比特浏览器:{json_file}')
                return False
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            bit_api = data['localServerAddress']
            cls.bit_port = bit_api.split(':')[-1]
            if cls.test_port(cls.bit_port):
                return cls.bit_port
            else:
                logger.error(f'请检查比特浏览器是否已经启动')
                return False

    def __request(self, endpoint, payload):
        """
        请求接口
        """
        endpoint = endpoint[1:] if endpoint.startswith('/') else endpoint
        api = f'http://127.0.0.1:{self.bit_port}/{endpoint}'
        res = None
        for _ in range(3):
            try:
                res = requests.post(api, json=payload, timeout=15)
                data = res.json()
                if data.get('success'):
                    return data
                else:
                    logger.error(f'endpoint: {endpoint} 请求结果: {data}')
                    time.sleep(3)
            except:
                if res:
                    logger.error(f'endpoint: {endpoint} 请求结果: {res.text}')
                else:
                    logger.error(
                        f'endpoint: {endpoint} 请求超时')
                time.sleep(3)
        return {}

    ##############################################浏览器接口#########################################################
    def create_driver(self, username='', password='', proxyType='noproxy', proxyIp='', proxyPort='', proxyUser='', proxyPassword='', **kwargs):
        """
        创建浏览器
        仅传入用户名、密码、代理
        """
        logger.info(f'创建/更新浏览器: username:{username}; password:{password}')
        # 浏览器对象
        remark = f'{username}----{password}'
        payload = payload_config.copy()
        payload['name'] = f'{self.website}:{username}'
        payload['remark'] = remark
        payload['proxyType'] = proxyType
        payload['host'] = proxyIp
        payload['port'] = proxyPort
        payload['proxyUserName'] = proxyUser
        payload['proxyPassword'] = proxyPassword
        if proxyType not in ['noproxy', 'http', 'https', 'socks5']:
            if 'rola' in proxyIp:
                ProxyType = 'rola'
            elif 'doveip' in proxyIp:
                ProxyType = 'doveip'
            elif 'cloudam' in proxyIp:
                ProxyType = 'cloudam'
            else:
                ProxyType = 'common'
            # 自定义提取代理
            payload['proxyType'] = 'socks5'
            payload['host'] = ''
            payload['port'] = ''
            payload['proxyMethod'] = 3
            payload['dynamicIpChannel'] = ProxyType
            payload['dynamicIpUrl'] = proxyIp
        # 指纹对象随机生成

        # 从kwargs更新参数
        for k, v in kwargs.items():
            if payload.get(k, None) != None:
                payload[k] = v
        payload['browserFingerPrint'] = {
            'displayLanguages': 'en-US',
            'languages': 'en-US',
            'isIpCreateLanguage': False,
            'isIpCreateDisplayLanguage': False,
        }

        # 查询是否已经创建过，如果已经创建过则保留原来的指纹
        driver = self.browser_list(username=username)
        if driver:
            payload['id'] = driver[0]['id']
            # 保留原来的分组
            if driver[0].get('groupId'):
                payload['groupId'] = driver[0]['groupId']
            # 保留原来的指纹
            browser_detail = self.browser_detail(driver[0]['id'])
            payload['browserFingerPrint'] = browser_detail['data']['browserFingerPrint']

        if proxyType not in ['noproxy', 'http', 'https', 'socks5']:
            if 'rola' in proxyIp:
                ProxyType = 'rola'
            elif 'doveip' in proxyIp:
                ProxyType = 'doveip'
            elif 'cloudam' in proxyIp:
                ProxyType = 'cloudam'
            else:
                ProxyType = 'common'
            # 自定义提取代理
            payload['proxyType'] = 'socks5'
            payload['host'] = ''
            payload['port'] = ''
            payload['proxyUserName'] = ''
            payload['proxyPassword'] = ''
            payload['proxyMethod'] = 3
            payload['dynamicIpChannel'] = ProxyType
            payload['dynamicIpUrl'] = proxyIp
        data = self.__request('browser/update', payload)
        if data.get('success'):
            logger.info(f'创建浏览器成功，{username}')
            return data['data']['id']
        else:
            logger.error(f'创建浏览器失败，{username}')
            return False

    def open_browser(self, browser_id, loadExtensions=True, args=[], extractIp=True):
        """
        打开窗口
        """
        logger.info(f'打开窗口: {browser_id}')
        payload = {
            'id': browser_id,
            'loadExtensions': loadExtensions,
            'args': args,
            'extractIp': extractIp
        }
        data = self.__request('browser/open', payload)
        if data.get('success'):
            options = webdriver.ChromeOptions()
            ws_url = data['data']['http']
            options.add_experimental_option(
                'debuggerAddress', ws_url)
            options.arguments.extend(
                ["--no-default-browser-check", "--no-first-run"])
            options.arguments.extend(["--no-sandbox", "--test-type"])
            driver = webdriver.Chrome( options=options)
            # 随机位置
            x = random.randint(0, 500)
            y = random.randint(10, 200)
            driver.set_window_position(x, y)
            # 新开标签页
            driver.execute_script("window.open('about:blank','_blank');")
            # 切换到新标签页
            driver.switch_to.window(driver.window_handles[-1])
            # 关闭原标签页
            for i in range(len(driver.window_handles)-1):
                driver.switch_to.window(driver.window_handles[i])
                driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            return driver
        else:
            logger.error(f'打开窗口失败: {browser_id}')
            return False

    def close_browser(self, browser_id):
        """
        关闭窗口
        """
        logger.info(f'关闭窗口{browser_id}')
        payload = {'id': browser_id}
        data = self.__request('browser/close', payload)
        if data.get('success'):
            logger.info(f'关闭窗口成功: {browser_id}')
            return True
        else:
            logger.error(f'关闭窗口失败: {browser_id}')
            return False

    def del_browser(self, browser_id):
        """
        删除窗口
        """
        logger.info(f'删除窗口{browser_id}')
        bit_api = f'http://127.0.0.1:{self.bit_port}'
        payload = {'id': browser_id}
        data = self.__request('browser/delete', payload)
        if data.get('success'):
            logger.info(f'删除窗口成功: {browser_id}')
            return True
        else:
            logger.error(f'删除窗口失败: {browser_id}')
            return False

    def browser_detail(self, browser_id):
        """
        获取窗口详情
        """
        # logger.info(f'获取窗口详情{browser_id}')
        payload = {'id': browser_id}
        data = self.__request('browser/detail', payload)
        if data.get('success'):
            # logger.info(f'获取窗口详情成功: {browser_id}')
            return data
        else:
            logger.error(f'获取窗口详情失败: {browser_id}')
            return False

    def browser_list(self, page=0, pageSize=100, username: str = '', groupId=''):
        """
        查询窗口
        """
        logger.info(f'查询窗口: {username}')
        payload = {
            "page": page,
            "pageSize": pageSize,
        }
        if username != '':
            payload['name'] = f'{self.website}:{username}'
        if groupId != '':
            payload['groupId'] = groupId
        return self.__request('browser/list', payload).get('data', {'list': []}).get('list', [])

    def windowbounds(self, type: str = 'box', startX: int = 0, startY: int = 0, width: int = 500, height: int = 500, col: int = 3, spaceX: int = 0, spaceY: int = 0, offsetX: int = 0, offsetY: int = 0):
        """
        窗口排列
        : params:type: *排列方式，宫格 box ，对角线 diagonal
        : params:startX: *Int起始X位置，默认0
        : params:startY: *Int起始Y位置，默认0
        : params:width: *Int宽度，最小500
        : params:height: *Int高度，最小200
        : params:col: *Int宫格排列时，每行列数
        : params:spaceX: *Int宫格横向间距，默认0
        : params:spaceYInt宫格纵向间距，默认0:
        : params:offsetX: *Int对角线横向偏移量
        : params:offsetY: *Int对角线纵向偏移量
        """
        if type not in ['box', 'diagonal']:
            logger.error('排列方式错误,自动选用box')
            type = 'box'
        if width < 500:
            logger.error('宽度最小500,自动设置为500')
            width = 500
        if height < 200:
            logger.error('高度最小200,自动设置为200')
            height = 200
        payload = {
            'type': type,
            'startX': startX,
            'startY': startY,
            'width': width,
            'height': height,
            'col': col,
            'spaceX': spaceX,
            'spaceY': spaceY,
            'offsetX': offsetX,
            'offsetY': offsetY
        }
        data = self.__request('windowbounds', payload)
        if data.get('success'):
            logger.info(f'窗口排列成功')
            return True
        else:
            logger.error(f'窗口排列失败')
            return False

    def update_browser_group_api(self, group_id, browser_ids):
        """
        更新窗口分组
        """
        logger.info(f'更新窗口分组{group_id}')
        payload = {
            'groupId': group_id,
            'browserIds': browser_ids
        }
        data = self.__request('browser/group/update', payload)
        if data.get('success'):
            logger.info(f'更新窗口分组成功: {group_id}')
            return True
        else:
            logger.error(f'更新窗口分组失败: {group_id}')
            return False

    def update_browser_proxy(self, browser_id, proxyType, proxyIp, proxyPort, proxyUser, proxyPass):
        """
        更新浏览器代理
        """
        logger.info(f'更新浏览器代理{browser_id}')
        payload = {
            "ids": [browser_id],
            "ipCheckService": "ip123",
            "proxyMethod": 2,
            "proxyType": proxyType,
            "host": proxyIp,
            "port": int(proxyPort) if proxyPort else "",
            "proxyUserName": proxyUser,
            "proxyPassword": proxyPass,
        }
        # 如果需要更新的代理为提取链接，那设置proxyType不在['noproxy', 'http', 'https', 'socks5']之中，proxyIp为提取链接
        if proxyType not in ['noproxy', 'http', 'https', 'socks5']:
            if 'rola' in proxyIp:
                ProxyType = 'rola'
            elif 'doveip' in proxyIp:
                ProxyType = 'doveip'
            elif 'cloudam' in proxyIp:
                ProxyType = 'cloudam'
            else:
                ProxyType = 'common'
            # 自定义提取代理
            payload['proxyType'] = 'socks5'
            payload['host'] = ''
            payload['port'] = ''
            payload['proxyUserName'] = ''
            payload['proxyPassword'] = ''
            payload['proxyMethod'] = 3
            payload['dynamicIpChannel'] = ProxyType
            payload['dynamicIpUrl'] = proxyIp
        data = self.__request('browser/proxy/update', payload)

        if data.get('success'):
            logger.info(f'更新浏览器代理成功: {browser_id}')
            return True
        else:
            logger.error(f'更新浏览器代理失败: {browser_id}')
            return False

    def update_browser_remark(self, browser_id: str, remark: str):
        """
        批量更新浏览器的备注
        """
        logger.info(f'更新浏览器的备注:{browser_id}->{remark}')
        payload = {
            'browserIds': [browser_id],
            'remark': remark
        }
        data = self.__request('browser/remark/update', payload)
        if data.get('success'):
            logger.info(f'批量更新浏览器的备注成功')
            return True
        else:
            logger.error(f'批量更新浏览器的备注失败')
            return False

    def batch_close_browser_by_seq(self, seqs: list):
        """
        批量通过序号关闭窗口
        """
        logger.info(f'批量通过序号关闭窗口')
        payload = {
            'seqs': seqs
        }
        data = self.__request('browser/close/byseqs', payload)
        if data.get('success'):
            logger.info(f'批量通过序号关闭窗口成功')
            return True
        else:
            logger.error(f'批量通过序号关闭窗口失败')
            return False

    ###################################################分组接口########################################################
    def add_group(self, group_name):
        """
        添加分组
        """
        logger.info(f'添加分组{group_name}')
        payload = {'groupName': group_name, 'sortNum': 1}
        data = self.__request('group/add', payload)
        if data.get('success'):
            logger.info(f'添加分组成功: {group_name}')
            return data['data']['id']
        else:
            logger.error(f'添加分组失败: {group_name}')
            return False

    def edit_group(self, group_id, group_name):
        """
        编辑分组
        """
        logger.info(f'编辑分组:{group_name}')
        payload = {'id': group_id, 'groupName': group_name, 'sortNum': 1}
        data = self.__request('group/edit', payload)
        if data.get('success'):
            logger.info(f'编辑分组成功: {group_name}')
            return True
        else:
            logger.error(f'编辑分组失败: {group_name}')
            return False

    def del_group(self, group_id):
        """
        删除分组
        """
        logger.info(f'删除分组:{group_id}')
        payload = {'id': group_id}
        data = self.__request('group/delete', payload)
        if data.get('success'):
            logger.info(f'删除分组成功: {group_id}')
            return True
        else:
            logger.error(f'删除分组失败: {group_id}')
            return False

    def group_list(self, page=0, pageSize=100):
        """
        查询分组列表，传入group_name则查询指定的分组
        """
        logger.info(f'查询分组列表')
        payload = {
            'page': page,
            'pageSize': pageSize
        }
        data = self.__request('group/list', payload)
        if data.get('success'):
            logger.info(f'查询分组列表成功')
            return data['data']['list']
        else:
            logger.error(f'查询分组列表失败')
            return []

    def group_detail(self, group_id):
        """
        查询分组详情
        """
        logger.info(f'查询分组详情')
        payload = {'id': group_id}
        data = self.__request('group/detail', payload)
        if data.get('success'):
            logger.info(f'查询分组详情成功')
            return data
        else:
            logger.error(f'查询分组详情失败')
            return False

    ###################################################自定义的一些方法########################################################
    def get_driver(self, username='', password='', proxyType='noproxy', proxyIp='', proxyPort='', proxyUsername='', proxyPassword='', **kwargs):
        """
        便捷创建并打开浏览器，返回driver对象和浏览器id
        """
        browser_id = self.create_driver(
            username, password, proxyType, proxyIp, proxyPort, proxyUsername, proxyPassword, **kwargs)
        if browser_id:
            driver = self.open_browser(browser_id)
            if driver:
                return driver, browser_id
            else:
                return False, browser_id
        else:
            return False, False

    def get_browser_info(self, browser_id, cols=['name']):
        """
        获取窗口信息
        :param browser_id: 窗口id
        :param cols: 需要获取的字段: name,remark,platform,platformIcon,proxyType,host,port,proxyUserName,proxyPassword,proxyMethod,agentId,cookie,userName,password,url,groupId,seq
        """
        logger.info(f'获取窗口信息:{browser_id}')
        detail = self.browser_detail(browser_id)
        if detail.get('success'):
            return {col: detail['data'].get(col, '') for col in cols}
        else:
            return {col: '' for col in cols}

    def update_browser_group(self, browser_id, group_name):
        """
        快速更新浏览器分组
        """
        logger.info(f'更新浏览器分组:{browser_id}->{group_name}')
        group_id = self.get_or_add_group(group_name)
        # 获取信息
        browser = self.browser_detail(browser_id)
        if browser.get('success'):
            detail = browser['data']
            detail['groupId'] = group_id
            res = self.__request('browser/update', detail)
            if res.get('success'):
                logger.info(f'更新浏览器分组成功:{browser_id}->{group_name}')
                return True
            else:
                logger.error(f'更新浏览器分组失败:{browser_id}->{group_name}:{res}')
                return False
        else:
            logger.error(f'更新浏览器分组失败:{browser_id}->{group_name}:获取浏览器信息失败')
            return False

    def query_group_id(self, group_name):
        """
        查询指定分组存在不存在，如果存在，返回分组id
        """
        logger.info(f'查询指定分组:{group_name}')
        group_list = self.group_list()
        for group in group_list:
            if group['groupName'] == group_name:
                group_id = group['id']
                logger.info(f'查询指定分组成功:{group_name}')
                return group_id
        logger.error(f'查询指定分组失败:{group_name}')
        return False

    def get_or_add_group(self, group_name):
        """
        获取或添加分组
        """
        logger.info(f'获取或添加分组:{group_name}')
        group_name = group_name.lower()
        group_id = self.query_group_id(group_name)
        if group_id:
            return group_id
        else:
            return self.add_group(group_name)

    def query_browser_group_name(self, browser_id):
        """
        查询浏览器分组名称
        """
        brow_detail = self.browser_detail(browser_id)
        group_id = brow_detail['data'].get('groupId', None)
        if group_id:
            group_detail = self.group_detail(group_id)
            group_name = group_detail['data']['groupName']
            return group_name
        else:
            return ''
