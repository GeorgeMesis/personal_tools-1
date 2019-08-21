#注意保存文件的格式 不同格式 获取的东西可能乱码
import requests
from bs4 import BeautifulSoup as bs
from weather import pass0
import time
#获取所有卫视链接
def get_link():
  r=requests.get("https://www.tvsou.com/epg/weishi/")
  html=bs(r.text,"lxml")
  htmls=html.select("li.relative")[:55]
  p=[]
  for i in htmls:
    x=i.select("a")[0]["href"]
    y=i.select("a")[0].text.strip()
    p.append([y,x])
  return p #还回所有卫视的链接
#根据链接 得到所有卫视的节目
def get_tv(p):
  p[0][1]="/epg/weishi/"#第一个卫视的链接有变动
  q=[]#每个卫视保存点
  w=[]#所有卫视保存点
  for m in p:
      o="https://www.tvsou.com"+m[1] #每个卫视的链接地址
      r=requests.get(o)
      html=bs(r.text,"lxml")
      htmls=html.select(".relative")[61:]
      for i in htmls:
        r=i.text.strip()
        y=r.split("\n")
        q.append(y)
      a={"weishi":m[0],"jiemu":q}
      w.append(a)
      q=[]
  for i in w:
    data=""
    shijian=""
    jm=""
    pindao=i["weishi"]
    data+=pindao+"\n"
    for x in i["jiemu"]:
      if i["jiemu"]=="[]":
        continue;
      shijian+=x[0]+","
      if len(x)<=1:
        continue;
      jm+=x[1]+","
    data="\n"+pindao+"\n"+shijian+"\n"+jm #得到所有卫视频道和每天节目
    save_excel(data)
    print("##")

#获取的结果保存在excel
def save_excel(data):
    time1=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    with open("%s.csv"%time1,'a+',encoding='utf-8') as f:
      f.write(data)
      f.close()

if __name__=='__main__':
  l=pass0()
  save_excel(l)
  p=get_link()
  get_tv(p)

