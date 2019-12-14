#coding=utf-8

import tkinter as tk

#円の座標
x=0
y=0

def click(event):
    global x,y
    #今の円を消す
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="white",width=0)
    x=event.x
    y=event.y
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red",width=0)

#ウィンドウの描く
root=tk.Tk()
root.geometry("600x400")

#キャンバスを置く
canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

#イベントを設定する
canvas.bind("<Button-1>",click)

root.mainloop()
