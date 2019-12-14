# coding=utf-8

import tkinter as tk

for f in tk.Tk().call("font","families"): #PC内のフォント取得
    print(f)
