#coding=utf-8

import tkinter as tk

def click(event):#関数の定義、click関数の作成、引数の設定(event)
    #クリックされたときそこに描画する
    canvas.create_oval(event.x-20,event.y-20,event.x+20,event.y+20, fill="red",width=0)
    
#ウィンドウを描く
root=tk.Tk()
root.geometry("600x400")

#Canvas を置く
canvas=tk.Canvas(root,width=600,height=400,bg="white")#bgはバックグランド？背景色のこと
canvas.place(x=0,y=0)

#イベントを設定する
canvas.bind("<Button-1>",click)

root.mainloop()
