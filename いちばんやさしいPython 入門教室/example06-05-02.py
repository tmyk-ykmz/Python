#coding=utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg


#ボタンがクリックされたときの処理
def ButtonClick():
    #テキスト入力欄に入力された文字列を取得
    b=editbox1.get()

#Lesson 5-4のプログラムから判定部分を拝借
#4桁の数字かどうかの判定
    isok=False
    if len(b)!=4:
        tmsg.showerror("エラー","４桁の数字を入力してください")
    else:
        kazuok=True
        for i in range(4):
            if (b[i]<"0") or (b[i]>"9"):
                tmsg.showerror("エラー","数字ではありません")
                kazuok=False
                break
        if kazuok:
            isok=True

    if isok:
        #４桁の数字であったとき
        #ヒットを判定
        hit=0
        for i in range(4):
            if a[i]==int(b[i]):
                hit=hit+1

        #ブローを判定
        blow=0
        for j in range(4):
          for i in range(4):
             if(int(b[j])==a[i])and(a[i]!=int(b[i]))and(a[j]!=int(b[j])):
              blow=blow+1
              break

        #ヒットが４なら当たりで終了
        if hit==4:
            tmsg.showinfo("当たり","おめでとうございます。当たりです")
            #終了
            root.destroy()
        else:
            #ヒット数とブロー数を表示
            tmsg.showinfo("ヒント","ヒット"+str(hit)+"/"+"ブロー"+str(blow))
            

#メインのプログラム
#最初にランダムな４つの数字を作成しておく
a=[random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),]

            
#ウィンドウを作る
root=tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

#ラベルを作る
labell=tk.Label(root,text="数を入力してね",font=("Hevetica",14))
labell.place(x=20,y=20)

#テキストボックスを作る
editbox1=tk.Entry(width=4,font=("Hevetica",28))
editbox1.place(x=120,y=60)

#ボタンを作る
button1=tk.Button(root,text="チェック",font=("Hevetica",14),command=ButtonClick)
button1.place(x=220,y=60)

#ウィンドウを表示する
root.mainloop()
