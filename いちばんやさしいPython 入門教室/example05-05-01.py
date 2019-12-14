# coding=utf-8



import random

#ランダムな数字を生成
a=[random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9)]

#テストのため答えを表示
#print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))


#数値判定（Flag）
#↓while構文の永久ループ
while True:
    #4桁の数字かどうかの判定
    isok=False        #4桁の数字か判定する変数
    while isok==False:
        b=input("数を入力してください＞")#ユーザーが入力した数字＝ｂ
        if len(b)!=4: #何桁か調べる
            print("４桁の数字を入力してください")
        else:
            kazuok=True        #各桁が数字かどうかの判定
            for i in range(4):
                if (b[i]<"0") or (b[i]>"9"):
                    print("数字ではありません")
                    kazuok=False
                    break
                if kazuok:
                    isok=True


    #４桁の数字であった場合
    #ヒットの判定
    hit=0
    for i in range(4):
        if a[i]==int(b[i]):
            hit=hit+1

    #ブローの判定
    blow=0
    for j in range(4):
        for i in range(4):
            if (int(b[j])==a[i]) and (a[i]!=int(b[i])) and (a[j]!=int(b[j])):
                blow=blow+1
                break

    #ヒット数とブロー数を表示
    print("ヒット"+str(hit))
    print("ブロー"+str(blow))


    #ヒット数が４ならば当たりで終了
    if hit==4:
        print("当たり！")
        break      #当たりの場合breakでループ処理終了
    
