# coding=utf-8

import tkinter as tk

root=tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム")

label1=tk.Label(root,text="数を入力してね")
label1.place(x=20,y=20)

editbox1=tk.Entry(width=4)
editbox1.place(x=120,y=20)

root.mainloop()
