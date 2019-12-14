# coding=utf-8

# ブロック崩し
from tkinter import *
import random

# ゲーム中で使う変数の一覧
blocks = []
block_size = {"x": 75, "y": 30}
ball = {"dirx": 15, "diry": -15, "x": 350, "y": 300, "w": 10}
bar = {"x": 0, "w": 100}
is_gameover = False
point = 0

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

# ゲームの初期化
def init_game():
    global is_gameover, point
    is_gameover = False
    ball["y"] = 250
    ball["diry"] = -10
    point = 0
    # ブロックを配置する
    for iy in range(0, 5):
        for ix in range(0, 8):
            color = "purple"
            if (iy + ix) % 2 == 1: color = "red"
            x1 = 4 + ix * block_size["x"]
            x2 = x1 + block_size["x"]
            y1 = 4 + iy * block_size["y"]
            y2 = y1 + block_size["y"]
            blocks.append([x1, y1, x2, y2, color])
    win.title("START")

# オブジェクトを描画する
def draw_objects():
    cv.delete("all") # 既存の描画を破棄
    cv.create_rectangle(0, 0, 600, 400, fill = "black", width = 0)
    # ブロックをひとつずつ描画
    for w in blocks:
        x1, y1, x2, y2, c = w
        cv.create_rectangle(x1, y1, x2, y2, fill = c, width = 0)
    # ボールを描画
    cv.create_oval(ball["x"] - ball["w"], ball["y"]- ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"], fill = "green")
