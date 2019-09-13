import requests
import os
from urllib import parse
from bs4 import BeautifulSoup
import json

'''def gethtml_imgkey(key):
  img = []
  url = "http://image.so.com/i?q=%s&src=srp#/"%key
  r = requests.get(url)
  bs = BeautifulSoup(r.text,"lxml")
  imgkey = bs.select("script[id=initData]")
  text = imgkey[0].text
  dictinfo = json.loads(text)
  #print(dictinfo["list"][1]["imgkey"])
  for i in range(98):
    imgkey=dictinfo["list"][i]["imgkey"]
    img.append(imgkey)
  return img'''

def gethtml_downurl(name,i):
  img = []
  url = "http://image.so.com/i?q=%s&src=srp#/"%name
  r = requests.get(url)
  bs = BeautifulSoup(r.text,"lxml")
  imgkey = bs.select("script[id=initData]")
  text = imgkey[0].text
  dictinfo = json.loads(text)
  for i in range(i):
    text=dictinfo["list"][i]["downurl_true"]
    img.append(text[33:text.find("&purl")])
  return img

def ascll_unquote(rawurl):
  pic=[]
  for i in rawurl:
    url=parse.unquote(i)
    pic.append(url)
  return pic

def mkdir(path):
  folder = os.path.exists(path)
  if not folder:
    os.makedirs(path)
    
def down_img(url,name):
  x=0
  for i in url:
    #print(i)
    size = len(url)
    r=requests.get(i)
    mkdir("E:\美女壁纸\%s"%name)
    x=x+1
    with open("E:\美女壁纸\%s\RR%s.jpg"%(name,x),"wb") as f:
      f.write(r.content)
      f.close()
      print("\r [%s%s] %d/%d " % (x * '█', ' ' * (size - 1 - x),x,size),end='')
def get_img(name,i):
  url=gethtml_downurl(name,i)
  ture_url=ascll_unquote(url)
  down_img(ture_url,name)




if __name__=='__main__':
  name = input('输入所要下载明星的名字：')
  if(name==''):{
    print("oh my god ,have it ? fuck you script wrong ")
    }
  i = int(input('你要下载的数量：'))
  get_img(name,i)



