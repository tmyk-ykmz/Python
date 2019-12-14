#coding=utf-8

import random

a=random.randint(0,9)
print(a)

b=int(input("数を入力＞"))
if a==b:
    print("当たり")
else:
    print("はずれ")
