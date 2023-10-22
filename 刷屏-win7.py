import os
from tkinter import N
from pynput.keyboard import Key, Controller
import time
import tkinter as tk


keyboard = Controller()

# 设置终端高度和宽度
os.system("mode con cols=60 lines=40")

while True:
  # 清空屏幕
 os.system("cls")  # Windows系统

 print("由东经雨编写(win7定制版本完结)，bug反馈1055411737@qq.com.")
 choice = input("东经雨请选择要执行的轰炸-东经雨(1-信息，2-倒计时):")

 if choice == "1":
     messages = input("请输入你要轰炸的信息:")
     times = eval(input("(注意:中途无法暂停!!!)请输入你要轰炸的次数:"))
     speed = eval(input("速度/秒:"))
     print("请将光标移动至会话框,你只有5秒时间")
     for i in range(5):
         print("距离信息轰炸还需要%d" % (5 - i))
         time.sleep(1)
     print("开始轰炸")
     for i in range(times):
         keyboard.type(messages)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)
         times -= 1  # 更新剩余次数
         print("距离结束还有%d次" % times)
         time.sleep(speed)
     os.system("cls")
     print("感谢使用东经雨编写的简易脚本，再见")
     time.sleep(4)
 if choice == "2":

     ft = input("东经雨-请选择要执行的轰炸-东经雨(1-倒数，2-正数):")

     Qmessages = input("请输入你要轰炸的信息(数字前半部分):")
     Hmessages = input("请输入你要轰炸的信息(数字后半部分):")
     times = eval(input("(注意:中途无法暂停!!!)请输入你要轰炸的次数(注意是从0开始或结束):"))
     speed = eval(input("速度/秒:"))
     print("请将光标移动至会话框,你只有5秒时间")
     for i in range(5):
         print("距离轰炸还需要%d秒" % (5 - i))
         time.sleep(1)
     print("开始轰炸")
     
     if ft == "1":
      for i in range(times):
         messages = "{}{}{}".format(Qmessages, times-1, Hmessages)
         keyboard.type(messages)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)
         times -= 1  # 更新剩余次数
         print("距离结束还有%d次" % times)
         time.sleep(speed)
        
 
     if ft == "2":
      for i in range(times):
         messages = "{}{}{}".format(Qmessages, i, Hmessages)
         keyboard.type(messages)
         keyboard.press(Key.enter)
         keyboard.release(Key.enter)
         times -= 1  # 更新剩余次数
         print("距离结束还有%d次" % times)
         time.sleep(speed)
     os.system("cls")
     print("感谢使用东经雨编写的简易脚本，再见")
     time.sleep(4)


 if choice == "520":
   print("竟然被你发现了")
   time.sleep(8)
   print("那就浪费一分钟吧")
   time.sleep(8)
   times = 520
   for i in range(times):
     messages = "{}{}{}".format(" 我 爱 你 ", times-1,  " I love you ")
     print(messages)
     times -= 1  # 更新剩余次数
     time.sleep(0.1)