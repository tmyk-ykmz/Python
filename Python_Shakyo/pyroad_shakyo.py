import os
import datetime


def allFileListGet():
    path = "."
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root,file))

    return file_list


def pyFileListGet(allFileList):
    pyFileList = []
    for file_name in allFileList:
        if file_name[-3:] == ".py":
            pyFileList.append(file_name)

    return pyFileList


def returnLines(pyList):
    line_sum = 0
    for file_name in pyList:
        lines_count = sum(1 for line in open(f"{file_name}"))
        line_sum += lines_count

    return line_sum


def fileWrite(data):
    f = open("pyroad.txt","a")
    now = datetime.datetime.now()
    f.write(f"{data},{now.year},{now.month},{now.day},{now.hour},{now.minute},{now.second}\n")
    f.close()


pyroadCount = sum(1 for line in open("pyroad.py")) #pyroad.pyの行数は除外
allLines = returnLines(pyFileListGet(allFileListGet())) - pyroadCount

rankList = ["二等兵","一等兵","上等兵","伍長","軍曹","曹長","准尉",
            "少尉","中尉","大尉","少佐","中佐","大佐","准将",
            "少将","中将","大将","元帥"]
levelLinesList = [1000,2000,3000,5000,6000,7000,8000,9000,10000,
                  12000,14000,16000,18000,20000,25000,30000,50000]
                
if allLines < levelLinesList[0]:
    print(f"{allLines}行Pythonを書いているぞ！")
    print(f"お前は{rankList[0]}でまだ新米パイソニスタだ。\n書け！書けば分かる！")
    print("ごちゃごちゃ考えるな。１行でもコードを書け！")
elif allLines > levelLinesList[-1] - 1:
    print(f"{allLines}行もPythonを書いているとは・・・")
    print(f"あなた様は{rankList[-1]}です。")
    print("その調子でがんばってください。")
else:
    for i, _ in enumerate(levelLinesList): #小さい方から総当りの方法
        if allLines > levelLinesList[i] - 1 and allLines < levelLinesList[i+1]:
            print(f"{allLines}行Pythonを書いているぞ！")
            print(f"お前は{rankList[i+1]}パイソニスタだ！")
            print("ごちゃごちゃ考えるな。１行でもコードを書け！")
            break

#データの書き込み
fileWrite(allLines)