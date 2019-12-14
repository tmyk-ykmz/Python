# coding:utf-8
a=1
for a in range(11):
    if (a % 2 == 0):
        print("○")
    if (a % 3 == 0):
        print("✖")
    if (a % 2 == 0) and (a % 3 == 0):
        print("△")

