# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
import pymysql
'''
Function:
	微博模拟登录
Detail:
	-login:
		Input:
			--username: 用户名
			--password: 密码
			--version: mobile/pc
		Return:
			--session: 登录后的requests.Session()
'''
login_headers = {
								'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
								'Accept': '*/*',
								'Accept-Encoding': 'gzip, deflate, br',
								'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
								'Connection': 'keep-alive',
								'Origin': 'https://passport.weibo.cn',
								'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='
							}
class weibo():
	def __init__(self, **kwargs):
		self.login_headers = {
								'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
								'Accept': '*/*',
								'Accept-Encoding': 'gzip, deflate, br',
								'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
								'Connection': 'keep-alive',
								'Origin': 'https://passport.weibo.cn',
								'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='
							}
		self.login_url = 'https://passport.weibo.cn/sso/login'
		#self.login_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
		self.session = requests.Session()
	'''登录函数'''
	def login(self, username, password, version='mobile'):
		if version == 'mobile':
			data = {
					'username': username,
					'password': password,
					'savestate': '1',
					'r': 'https://weibo.cn/',
					'ec': '0',
					'pagerefer': 'https://weibo.cn/pub/',
					'entry': 'mweibo',
					'wentry': '',
					'loginfrom': '',
					'client_id': '',
					'code': '',
					'qq': '',
					'mainpageflag': '1',
					'hff': '',
					'hfp': ''
					}
			res = self.session.post(self.login_url, headers=self.login_headers, data=data)
			if res.json()['retcode'] == 20000000:
				print('[INFO]: Account -> %s, login successfully...' % username)
				return self.session
			else:
				raise RuntimeError('Account -> %s, fail to login, username or password error...' % username)
		elif version == 'pc':
			return None
		else:
			raise ValueError('Unsupport argument in weibo.login -> version %s, expect <mobile> or <pc>...' % version)

def get_comment(c,name,page):
            text=[]
            for t in range(1,page):   
              url = "https://weibo.cn/comment/%s?&page=%i"%(name,t)
              r = c.get(url,headers=login_headers)
              soup = bs(r.text,"lxml")
              soup = soup.select(".c")[4:-1]
              for i in soup:
                try:
                  comment_id=i.select("a")[0].string
                  comment_say=i.select("span")[0].text
                  text.append([comment_id,comment_say])
                except:
                  pass
            return text
def baocunmysql(text):
  for i in text:
        # 打开数据库连接
      db = pymysql.connect("localhost","root","123456","test" )
      print(i[0],i[1])
      # 使用 cursor() 方法创建一个游标对象 cursor
      cursor = db.cursor()
      sql = """INSERT INTO liyundi(id,say)
               VALUES ("%s","%s")"""%(i[0],i[1])
      try:
         # 执行sql语句
         cursor.execute(sql)
         # 提交到数据库执行
         db.commit()
      except:
         # 如果发生错误则回滚
         db.rollback()       
      # 关闭数据库连接
      db.close()

if __name__ == '__main__':
  c=weibo().login("xxxxxxxxxxxx","xxxxxxxxxx") #你微博的id 密码
  q=get_comment(c,"Hpt1g0mEf",5) # 你需要爬去博主特有标识
  baocunmysql(q)
  
