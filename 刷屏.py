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

    print("由东经雨编写，更新:1055411737@qq.com.")
    choice = input(
        "\033[4m\033[36m东经雨\033[0m-\033[34m请选择要执行的轰炸-\033[4m\033[36m东经雨\033[0m(1-信息，2-倒计时):"
    )

    if choice == "1":
        messages = input("\033[33m请输入你要轰炸的信息:\033[0m")

        times = input("(\033[31m注意:中途无法暂停!!!\033[0m)\033[33m请输入你要轰炸的次数:\033[0m")
        while not times.isdigit() or int(times) <= 0:
            print("\033[31m请输入数字并大于零!\033[0m")
            times = input("(\033[31m注意:中途无法暂停!!!\033[0m)\033[33m请输入你要轰炸的次数:\033[0m")
        times = int(times)

        speed = eval(input("\033[33m速度/秒:\033[0m"))
        while not speed.isdigit():
            speed = input("\033[33m请输入数字!:\033[0m")
        speed = int(speed)

        print("请将光标移动至会话框,你只有5秒时间")
        for i in range(5):
            print("\033[34m距离信息轰炸还需要\033[32m%d\033[0m秒" % (5 - i))
            time.sleep(1)
        print("开始轰炸")
        for i in range(times):
            keyboard.type(messages)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            times -= 1  # 更新剩余次数
            print("\033[34m距离结束还有\033[32m%d\033[0m次" % times)
            time.sleep(speed)

        print(
            "\033[1m\033[31m感谢使用\033[4m\033[36m东经雨\033[0m\033[1m\033[31m编写的简易脚本，再见\033[0m"
        )
        time.sleep(4)
    if choice == "2":
        ft = input(
            "\033[4m\033[36m东经雨\033[0m-\033[34m请选择要执行的轰炸-\033[4m\033[36m东经雨\033[0m(1-倒数，2-正数):"
        )

        Qmessages = input("\033[33m请输入你要轰炸的信息(数字前半部分):\033[0m")
        Hmessages = input("\033[33m请输入你要轰炸的信息(数字后半部分):\033[0m")
        times = eval(
            input("(\033[31m注意:中途无法暂停!!!\033[0m)\033[33m请输入你要轰炸的次数(注意是从0开始或结束):\033[0m")
        )
        while not times.isdigit or int(times) <= 0():
            print("\033[31m请输入数字并大于零!\033[0m")
            times = input(
                "(\033[31m注意:中途无法暂停!!!\033[0m)\033[33m请输入你要轰炸的次数(注意是从0开始或结束):\033[0m"
            )
        times = int(times)
        speed = eval(input("\033[33m速度/秒:\033[0m"))
        while not speed.isdigit():
            speed = input("\033[33m请输入数字!:\033[0m")
        speed = int(speed)
        print("请将光标移动至会话框,你只有5秒时间")
        for i in range(5):
            print("\033[34m距离信息轰炸还需要\033[32m%d\033[0m秒" % (5 - i))
            time.sleep(1)
        print("\033[1m\033[31m开始轰炸\033[0m")

        if ft == "1":
            for i in range(times):
                messages = "{}{}{}".format(Qmessages, times - 1, Hmessages)
                keyboard.type(messages)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                times -= 1  # 更新剩余次数
                print("\033[34m距离结束还有\033[32m%d\033[0m次" % times)
                time.sleep(speed)

        if ft == "2":
            for i in range(times):
                messages = "{}{}{}".format(Qmessages, i, Hmessages)
                keyboard.type(messages)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                times -= 1  # 更新剩余次数
                print("\033[34m距离结束还有\033[32m%d\033[0m次" % times)
                time.sleep(speed)

        print(
            "\033[1m\033[31m感谢使用\033[4m\033[36m东经雨\033[0m\033[1m\033[31m编写的简易脚本，再见\033[0m"
        )
        time.sleep(4)

    if choice == "520":
        print("竟然被你发现了")
        time.sleep(8)
        print("那就浪费一分钟吧")
        time.sleep(8)
        times = 520
        for i in range(times):
            messages = "{}{}{}".format(" 我 爱 你 ", times - 1, " I love you ")
            print(messages)
            times -= 1  # 更新剩余次数
            time.sleep(0.1)
