#AUTHOT:微信公众号：爱上资讯吧
from selenium import webdriver
import time
import re
import random
import requests
from urllib import parse
import pymongo


#全局变量
qq = ''#你的QQ
passwod = ''#你的密码
host = 'localhost'
port = 27107
db = 'QQ'
class Spider(object):
  #打开QQ空间页面
    def __init__(self):
        self.driver = webdriver.Ie()
        self.driver.get('https://qzone.qq.com/')
        self.__username = qq
        self.__password = password
        self.headers = {
            'host': 'h5.qzone.qq.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'connection': 'keep-alive'
        }
        self.req = requests.Session()
        self.cookies = {}
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[db]
#登陆QQ空间 获取相应参数
    def login(self):
        self.driver.set_window_position(20, 40)
        self.driver.set_window_size(1100, 700)
        self.driver.switch_to.frame('login_frame')
        self.driver.execute_script("var a = document.getElementById('qlogin_list');a.removeChild(a.firstElementChild);")
        self.driver.find_element_by_id('switcher_plogin').click()
        self.driver.find_element_by_id('u').clear()
        self.driver.find_element_by_id('u').send_keys(self.__username)
        time.sleep(2)
        self.driver.find_element_by_id('p').clear()
        self.driver.find_element_by_id('p').send_keys(self.__password)
        time.sleep(2)
        self.driver.find_element_by_id('login_button').click()
        time.sleep(3)
        self.driver.get('http://user.qzone.qq.com/{}'.format(self.__username))
        cookie = ''
        for item in self.driver.get_cookies():
            cookie += item["name"] + '=' + item['value'] + ';'
        self.cookies = cookie
        self.get_g_tk()
        self.headers['Cookie'] = self.cookies
        self.driver.quit()
    #根据解码方式获取g_tk
    def get_g_tk(self):
      
        p_skey = self.cookies[self.cookies.find('p_skey=') + 7: self.cookies.find(';', self.cookies.find('p_skey='))]
        h = 5381
        for i in p_skey:
            h += (h << 5) + ord(i)
        self.g_tk = h & 2147483647

     def get_g_tk(self):
        p_skey = self.cookies[self.cookies.find('p_skey=') + 7: self.cookies.find(';', self.cookies.find('p_skey='))]
        h = 5381
        for i in p_skey:
            h += (h << 5) + ord(i)
        print('g_tk', h & 2147483647)
        self.g_tk = h & 2147483647
    #获取所有留言好友ID UIN
  def get_ids(self):
        url = 'https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?'
        params = {
            'uin': self.__username,
            'hostUin': self.__username,
            'inCharset': 'utf-8',
            'outCharset': 'utf-8',
            'sort': 0,
            'num': 10,
            'format': 'jsonp',
            'g_tk': self.g_tk
        }
        url = url + parse.urlencode(params)
        t = True
        start = 0
        while t:
            url_ = url + '&start=' + str(start)
            board = self.req.get(url_, headers=self.headers)
            time.sleep(1)
            if '\"commentList\":[]' in board.text:
                t = False
            else:
                ids = re.findall('"id":".*?"', board.text)
                uins = re.findall('"uin":\d+', str(re.findall('type.*\n"uin":\d+', board.text)))
                for id, uin in zip(ids, uins):
                    print(id, uin)
                    self.ids += id.replace('"id":', '').replace('"', '') + ","
                    self.uins += uin.replace('"uin":', '') + ','
                start += 10

    def del_board(self):
        print(self.ids, self.uins)
        url = 'https://h5.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/del_msgb?' + '&g_tk=' + str(self.g_tk)
        data = {
            'hostUin': self.__username,
            'idList': self.ids,
            'uinList': self.uins,
            'iNotice': 1,
            'inCharset': 'utf-8',
            'outCharset': 'utf-8',
            'ref': 'qzone',
            'json': 1,
            'g_tk': self.g_tk,
            'format': 'fs',
            'qzreferrer': 'https://qzs.qq.com/qzone/msgboard/msgbcanvas.html'
        }
        response = self.req.post(url, data=data, headers=self.headers).text
        if '"message":"成功删除' in response:
            print(response["message"])
        else:
            pass

 



if __name__ == '__main__':
    sp = Spider()
    sp.login()
    get_ids()
    del_board()

