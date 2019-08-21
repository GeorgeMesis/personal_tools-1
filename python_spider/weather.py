import requests
import time
from bs4 import BeautifulSoup as bs
def get_thing():
  r=requests.get("http://www.weather.com.cn/textFC/beijing.shtml")
  r.encoding=r.apparent_encoding
  html=bs(r.text,"lxml")
  htmls=html.select("li")[6:22]
  return htmls

def get_weather(shengfen,link):
  r=requests.get(link)
  r.encoding="utf-8"
  html=bs(r.text,"lxml")
  htmls=html.select("tr")[2:3]
  weather=shengfen+htmls[0].text.replace("\n",",")
  return weather
def get_link(weather1,htmls):
  for i in htmls:
    html=i.select("a")
    for f in range(len(html)):
      link="http://www.weather.com.cn"+html[f]["href"]
      shengfen=html[f].text
      weather=get_weather(shengfen,link)
      weather1+=weather+"\n"
  print(type(weather1))
  return weather1
def save_excel(data):
    time1=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    with open("%s.csv"%time1,'a+',encoding='utf-8') as f:
      f.write(data)
      f.close()

def pass0():
  weather1=""
  htmls=get_thing()
  l=get_link(weather1,htmls)
  return l
