#coding=utf-8

import tkinter as tk

#円の座標と半径
x=400
y=300
#移動量
dx=1
dy=1

def move():
    global x,y,dx,dy
    #今の円を消す
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="white",width=0)
    #xの座標を動かす
    x=x+dx
    #yの座標を動かす
    y=y+dy
    #次の位置に円を描く
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red",width=0)
    #端を超えていたら反対向きにする
    if x >=canvas.winfo_width():#右辺を越えたとき
        dx=-1#左に移動
    if x <=0:
        dx=+1#右に移動

    #高さを超えたら反対にする
    if y >=canvas.winfo_height():#下辺を越えたとき
        dy=-1#上に移動
    if y <=0:
        dy=+1#下に移動

    #再びタイマー
    root.after(10,move)

#ウィンドウを描く
root=tk.Tk()
root.geometry("600x400")

#キャンバスを置く
canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

#タイマーを設定する
root.after(10,move)

root.mainloop()
