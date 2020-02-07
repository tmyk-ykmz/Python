# tkinterを取り込む
from tkinter import *
import tkinter.messagebox as mb

# ボタンが押下されたときの動作を関数として定義
def say_hello():
    mb.showinfo("挨拶", "おはようございます") # OKボタンのみのダイアログ

# メインウィンドウを作成
root = Tk()
root.title("挨拶") # メインウィンドウのタイトル設定

# ラベルを作成
desc_label = Label(text="以下のボタンを押してください")
desc_label.pack()

# 挨拶ボタンを作成
hello_button = Button(
    text="挨拶", # ボタンのテキスト
    width=10, height=3, # 文字数でボタンのサイズを指定
    command=say_hello # ボタンクリック時の動作
)
hello_button.pack()

# メインループを開始
root.mainloop()