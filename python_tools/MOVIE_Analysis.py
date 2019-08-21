#Author:Kare-chen   微信搜索关注：爱上资讯吧  解读感情 爱上资讯
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,QGridLayout,QLineEdit,QMainWindow,QMessageBox,
    QComboBox, QApplication)
import sys
import webbrowser
class VIPVideo(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(447, 250)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 60, 170, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("路线1")
        self.comboBox_2.addItem("路线2")
        self.comboBox_2.addItem("路线3")
        self.comboBox_2.addItem("路线4")
        self.comboBox_2.addItem("路线5")
        self.comboBox_2.addItem("路线6")
        self.comboBox_2.addItem("路线7")
        self.comboBox_2.addItem("路线8")
        self.comboBox_2.addItem("路线9")
        self.comboBox_2.addItem("路线10")
        self.comboBox_2.setEditable(False)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(70, 60, 121, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 121, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 190, 300, 40))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(False)


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 75, 23))
        self.pushButton.clicked.connect(self.OpenUrl)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setFixedSize(Form.width(),Form.height())


        Form.show()
    def OpenUrl(self,Form):
        str=""
        str1=self.lineEdit.text()
        str2=self.comboBox_2.currentText()
        if str2=="路线1":
            str="http://www.82190555.com/video.php?url="
        elif str2=="路线2":
            str="http://jx.aeidu.cn/index.php?url="
        elif str2 == "路线3":
            str="http://www.sonimei.cn/?url="
        elif str2 == "路线4":
            str="http://www.a305.org/weixin.php?url="
        elif str2=="路线5":
            str="http://www.vipjiexi.com/tong.php?url="
        elif str2 == "路线6":
            str="http://jx.aeidu.cn/index.php?url="
        elif str2 == "路线7":
            str="http://www.sonimei.cn/?url="
        elif str2=="路线8":
            str="https://api.vparse.org/?url="
        elif str2 == "路线9":
            str="https://jx.maoyun.tv/index.php?id="
        elif str2 == "路线10":
            str="http://pupudy.com/play?make=url&id="
        else:
            str="http://www.82190555.com/video.php?url="
        if str1=="":
            reply = QMessageBox.question(self, '提醒',
                                         "请输入有效视频链接 !",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
        else:
            webbrowser.open(str+str1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "视频解析器—爱上资讯吧"))
        self.label_1.setText(_translate("Form", "观看路线:"))
        self.label_2.setText(_translate("Form", "视频链接:"))
        self.textEdit.setHtml(_translate("Form", "仅供学习参考，请勿涉嫌商业犯罪 微信搜索：爱上资讯吧 分享感情 爱上资讯"))
        self.pushButton.setText(_translate("Form", "观看"))
        self.pushButton_2.setText(_translate("Form", "退出"))
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = VIPVideo()
    sys.exit(app.exec_())
