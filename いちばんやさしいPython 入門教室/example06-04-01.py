# coding=utf-8


#GUIツールインポート、ｔｋに置き換え
import tkinter as tk


#ｔｋでウィンドウ作成
root=tk.Tk()
#geometryメソッドでウィンドウサイズ変更
root.geometry("400x150")
root.title("数当てゲーム")

#labellメソッドでメッセージ配置
labell=tk.Label(root,text="数を入力してね",font=("Helvetica",14))
labell.place(x=20,y=20)

#Entryメソッドで入力欄を配置
editbox1=tk.Entry(width=4,font=("Helvetica",28))
editbox1.place(x=120,y=60)


button=tk.Button(root,text="チェック",font=("Helvetica",14))
button.place(x=250,y=60)

root.mainloop()
