# 再帰関数を定義
def say_hello(i):
    if i <= 0: # iが0になったらreturn
        return
    print("ハロー", i)
    say_hello(i-1) # say_helloを呼び出す

# 実行
say_hello(10)