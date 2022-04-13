# -*- codeing = utf-8 -*-
# -*- Time : 2022/4/12 11:04
# -@Author：王伟
# @file:.PY
# @Software: PyCharm
#条件格式 如果真假
'''
if True:
    print("True")
else:
    print("False")
'''
#这三个是可以一起使用的
'''
score = 78
if score >= 90 and score <= 100:
    print("A")
elif score >=80 and score <90:
        print("B")
elif score >=70 and score <80:
        print("C")
else:
    print("E")
'''
'''
xingBie = 1 #1=男，0等于女
danShen = 1 #1=单身 ，0等于有对象

if xingBie == 1:
    print("男")
    if danShen == 1:
        print("单身")
    else:
        print("电脑给我一个吧")
else:
    print("女生")
    print("....")
'''
'''
import random #引入随机库
x = random.randint(0,2)  #生成0-2的随机数
print(x)
'''

'''
print("欢迎来到剪刀石头布游戏")
print("0代表剪刀，1代表石头，2代表布")
# 获取你出的随机值
import random
b = random.randint(0,2)

a = input("电脑出什么呢？请输入：")
a = int(a)
print("电脑出的是：%s， 你出的是：%s"%(b,a))
if  a==0 and b==1:
    print("电脑获胜")
elif a==1 and b==1:
    print("你电脑平局")
elif a==2 and b==1:
    print("你获胜")
elif a==0 and b==0:
    print("你电脑平局")
elif  a==1 and b==0:
    print("你获胜")
elif a==2 and b==0:
    print("电脑获胜")
elif a==0 and b==2:
    print("你获胜")
elif  a==1 and b==2:
    print("电脑获胜")
elif a==2 and b==2:
    print("你电脑平局")
'''
