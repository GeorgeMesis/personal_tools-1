import requests
from bs4 import BeautifulSoup as bs
import time
import  os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,QGridLayout,QLineEdit,QMainWindow,QMessageBox,
    QComboBox, QApplication)
from PyQt5.QtCore import QThread, QSize
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Connection":"keep-alive",
"Host":"www.23txt.com",
"Referer":"https://www.so.com/s?ie=utf-8&src=hao_360so_suggest_b&shb=1&hsid=7e23b92ac894af70&eci=undefined&nlpv=&q=%E6%88%98%E7%A5%9E%E7%8B%82%E9%A3%99",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
def get_page(book,bookname,path):  
      for i in book:
        try:
          url = "https://www.23txt.com%s"%i[1]
          r = requests.get(url,headers=headers)
          r.encoding="GB2312"
          soup = bs(r.text,"lxml")
          soup1 = soup.select("div #content")
          title = soup.select("h1")[0].text
          text = title+"\n\n"+soup1[0].text
          with open("%s\%s.txt"%(path,bookname),mode='a', encoding='utf-8') as f:
            f.write(text+"\n\n")
          time.sleep(0.1)
          print("%s下载完成"%title)
        except:
          pass
def get_url(url):
          book=[]
          r = requests.get(url,headers=headers)
          r.encoding="GB2312"
          soup = bs(r.text,"lxml")
          soup1 = soup.select("div #list")[0].select("dd")
          for i in soup1:
            title=i.text
            url=i.select("a")[0].attrs["href"]
            book.append([title,url])
          return book
def get_book(bookname1):
    books = []
    url = "https://www.23txt.com/search.php?keyword=%s"%bookname1
    r = requests.get(url,headers=headers)
    r.encoding = "utf-8"
    soup = bs(r.text,"lxml")
    html = soup.select("h3")
    for i in html:
      html1 = i.select("a")
      ture_url = html1[0].attrs["href"]
      bookname = html1[0].text.strip()
      books.append([bookname,ture_url])
    for i in books:
      if i[0] == bookname1:
        return i[1]
      else:
        continue
    print("未能寻找到此书")
path = os.getcwd()#获取当前文件路径
bookname1 = "帝霸"  #书名  
url = get_book(bookname1)
book=get_url(url)
get_page(book,bookname1,path)
'''class Window(QWidget):
    def __init__(self):
      super().__init__()
      self.setupUi(self)
    def setupUi(self,Form):
      Form.setObjectName("Form")
      Form.resize(447,250)
      self.label_1 = QtWidgets.QLabel(Form)
      self.label_1.setGeometry(QtCore.QRect(40, 20, 80,20))
      self.label_1.setObjectName("label_1")
      self.lineEdit = QtWidgets.QLineEdit(Form)
      self.lineEdit.setGeometry(QtCore.QRect(120, 20, 171, 20))
      self.lineEdit.setObjectName("lineEdit")
      self.textEdit = QtWidgets.QTextEdit(Form)
      self.textEdit.setGeometry(QtCore.QRect(0, 50, 447, 200))
      self.textEdit.setObjectName("textEdit")
      self.pushButton = QtWidgets.QPushButton(Form)
      self.pushButton.setGeometry(QtCore.QRect(320, 20, 75, 23))
      self.pushButton.clicked.connect(self.finall)
      self.retranslateUi(Form)
      QtCore.QMetaObject.connectSlotsByName(Form)
      Form.show()
    def finall(self,Form):
      path = os.getcwd()#获取当前文件路径
      bookname1 = self.lineEdit.text()
      books = []
      url = "https://www.23txt.com/search.php?keyword=%s"%bookname1
      r = requests.get(url,headers=headers)
      r.encoding = "utf-8"
      soup = bs(r.text,"lxml")
      html = soup.select("h3")
      for i in html:
        html1 = i.select("a")
        ture_url = html1[0].attrs["href"]
        bookname = html1[0].text.strip()
        books.append([bookname,ture_url]) 
      for i in books:
        if i[0] == bookname1:
          url1=i[1]
        else:
          continue
      book=[]
      r = requests.get(url1,headers=headers)
      r.encoding="GB2312"
      soup = bs(r.text,"lxml")
      soup1 = soup.select("div #list")[0].select("dd")
      for i in soup1:
        title=i.text
        url=i.select("a")[0].attrs["href"]
        book.append([title,url])
      for i in book:
        try:
          url = "https://www.23txt.com%s"%i[1]
          r = requests.get(url,headers=headers)
          r.encoding="GB2312"
          soup = bs(r.text,"lxml")
          soup1 = soup.select("div #content")
          title = soup.select("h1")[0].text
          text = title+"\n\n"+soup1[0].text
          with open("%s\%s.txt"%(path,bookname1),mode='a', encoding='utf-8') as f:
            f.write(text+"\n\n")
          time.sleep(0.1)
          print("%s下载完成"%title)
        except:
          pass

      
      
  
    def retranslateUi(self,Form):
      _translate = QtCore.QCoreApplication.translate
      Form.setWindowTitle(_translate("Form","TXT小说下载工具"))
      self.label_1.setText(_translate("Form","小说书名:"))
      self.pushButton.setText(_translate("Form", "下载"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())'''


