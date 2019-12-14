#coding=utf-8

import tkinter as tk#tkinter をインポート、tkに代入

class Ball:#Ballクラスの定義
    def __init__(S,x,y,dx,dy,color):
        S.x=x
        S.y=y
        S.dx=dx
        S.dy=dy
        S.color=color

#moveメソッドーーここからーー
    def move(S,canvas):#図形を動かすためのメソッド
        #いまの図形を消す
        S.erase(canvas)
        #x座標、y座標を動かす
        S.x=S.x+S.dx
        S.y=S.y+S.dy
        #次の位置に図形を描画する
        S.draw(canvas)
        #端を超えていたら反対向きにする
        if S.x >= canvas.winfo_width():
           S.dx = -1
        if S.x <= 0:
           S.dx = +1
        if S.y >= canvas.winfo_height():
           S.dy = -1
        if S.y <= 0:
           S.dy = +1
#moveメソッドーーここまでーー
#円を消すメソッド
    def erase(S,canvas):
        canvas.create_oval(S.x-20,S.y-20,S.x+20,S.y+20,fill="white",width=0)
#次の位置に円を描くメソッド
    def draw(S,canvas):
        canvas.create_oval(S.x-20,S.y-20,S.x+20,S.y+20,fill=S.color,width=0)

#rectangleクラスの定義、Ballクラスの継承
class Rectangle(Ball):
    def erase(S,canvas):
        canvas.create_rectangle(S.x-20,S.y-20,S.x+20,S.y+20,fill="white",width=0)
    def draw(S,canvas):
        canvas.create_rectangle(S.x-20,S.y-20,S.x+20,S.y+20,fill=S.color,width=0)

#triangleクラスの定義、Ballクラスの継承
class Triangle(Ball):
    def erase(S,canvas):
        canvas.create_polygon(S.x,S.y-20,S.x+20,S.y+20,S.x-20,S.y+20,fill="white",width=0)
    def draw(S,canvas):
        canvas.create_polygon(S.x,S.y-20,S.x+20,S.y+20,S.x-20,S.y+20,fill=S.color,width=0)

#図形をまとめて用意する
balls=[
    Ball(400,300,1,1,"red"),
    Rectangle(100,500,1,-1,"green"),
    Triangle(600,100,1,-1,"blue")
]

def loop():#loop関数の定義
    for b in balls:
        b.move(canvas)#動かす命令
    #もう一度繰り返す
    root.after(10,loop)

#ウィンドウを描く
root=tk.Tk()
root.geometry("800x600")

#キャンバスを置く
canvas=tk.Canvas(root,width=800,height=600,bg="white")
canvas.place(x=0,y=0)

#タイマーをセット
root.after(10,loop)

root.mainloop()
