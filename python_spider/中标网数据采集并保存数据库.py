import requests
import pymysql
from bs4 import BeautifulSoup

def gethtml(url):
  kv = {'user-agent':'Mozilla/5.0'}
  r = requests.get(url,headers=kv)
  return r.text
  
def rshtml(html):
  ulist=[]
  x = BeautifulSoup(html,'html.parser')
  y = x.find('table',width="95%")
  z = y.find_all('tr')
  for tr in z[1:]:
    tds=tr('a')
    ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

  return ulist
def dshtml(List):
  for i in range(15):
    u=List[i]
    p='https://cpcb.cqggzy.com/PlatPart.aspx/Detail?Part=Zbgs_Detail&FTNO='+u[0].strip()
    print(u[1].strip())
    db = pymysql.connect("localhost","root","123456","t" )
       
      # 使用cursor()方法获取操作游 
    cursor = db.cursor()
       
      # SQL 插入语句
    sql = "INSERT INTO project values('%s','%s','%s','%s','%s')"%(u[0].strip(),u[1].strip(),u[2].strip(),u[3].strip(),p)
    try:
         # 执行sql语句
         cursor.execute(sql)
         # 提交到数据库执行
         db.commit()
         print(i)
    except:
         # 如果发生错误则回滚
         db.rollback()
    db.close()
def main():
  for i in range(138):
    
    url = 'https://cpcb.cqggzy.com/Front.aspx/Zbgs/%s'%(i+1)
    html = gethtml(url)
    List = rshtml(html)
    dshtml(List)

  
main()



  
