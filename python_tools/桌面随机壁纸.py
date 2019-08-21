import ctypes
import random
'''from tkinter import *
import os
top=Tk()
top.wm_iconbitmap('123.ico')'''
filepath = r'C:\Users\Administrator\Desktop\工具\桌面壁纸' # 需要桌面更换的图片文件路径
ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath+'\RR'+str(random.randint(1,20))+'.jpg', 0)
