#!/home/ty/.pyenv/versions/3.8.0/bin/python

# ↑↑シバン指定（一行目）

# 文字化け対策
import html
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ヘッダ情報を出力
print("Content-Type: text/html; charset=utf-8")

# ヘッダと本体データを区切る空行
print("")

# 本体データを出力
print("<html><head><meta charset='utf-8'></head><body>")
print("聞くことに速く語ることに遅くあるべき")
print("</body></html>")