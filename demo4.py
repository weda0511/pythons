# -*- codeing = utf-8 -*-
# -*- Time : 2022/4/12 12:50
# -@Author：王伟
# @file:.PY
# @Software: PyCharm
'''
for i in range(5):
    print(i)
'''
'''
for i in range(0,11,2):
    print(i)
'''
'''
for i in range(-10,-100,-30):
    print(i)
'''
'''
name = "guiyang"
for x in name:
    print(x,end="\t")
'''
'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])

i = 0
while i <5:
    print("当前是第%s执行循环"%(i+1))
    print("i=%s"%i)
    i += 1

i = 0
while i <5:
    print("当前是第%s执行循环"%(i+1))
    print("i=%s"%i)
    i += 1

#1-100求和
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    print("1到%d的和为%d"%(n,sum))

count = 10
while count<5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于或等于5")

i = 1
j = 1
while j <= i < 10 and j <10:
    print("%d*%d=%d"%(i,j,i*j), end="\t")
    if i > j:
        j += 1
    else:
        i +=1
        j = 1
        print("\n")
        continue
'''
# 答案3 for+字符串转换
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")  # end=" "作用①不换行②间隔
    print()  # 换行
