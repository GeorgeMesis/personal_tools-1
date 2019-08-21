import requests
import pymysql
from bs4 import BeautifulSoup

def 获取源码(url):
  回应 = requests.get(url)
  回应.encoding = 回应.apparent_encoding
  return 回应.text

def 获取信息(源码):
  小说信息 = {}
  文档树 = BeautifulSoup(源码,'html.parser')
  小说们 = 文档树.find_all('a',class_='name')
  for 小说 in 小说们[2:]:
    小说名 = 小说.text
    小说链接 = 'https:'+小说.attrs['href']
    小说信息[小说名] = 小说链接
  return 小说信息
    


def 保存(信息):
  for 小说名,小说链接 in 信息.items():
    print(小说名,小说链接)
    db = pymysql.connect("localhost","root","123456","t" )
       
      # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
       
      # SQL 插入语句
    sql = "INSERT INTO novel values('%s','%s')"%(小说名,小说链接)
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
          
      

url = 'https://www.qidian.com/'
源码 = 获取源码(url)
信息 = 获取信息(源码)
保存(信息)
