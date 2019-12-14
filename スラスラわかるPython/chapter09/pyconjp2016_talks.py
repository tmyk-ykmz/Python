#coding=utf-8
 
import requests
# Webサイトから情報を取得するPythonライブラリ
from bs4 import BeautifulSoup
# HTML解析ライブラリ（外部ライブラリ）


result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")
# resultにリンク先のHTMLを格納

soup = BeautifulSoup(result.text,"html.parser")
# 解析したい文字列、処理方法を指定し返された値をsoupへ格納

presentation_html_list = soup.find_all("div",class_="presentation")
# <div>タグでclassにpresentationという文字が含まれるものをpresentation_html_listに格納
# BeautifulSoupオブジェクト　find_allメソッド（条件に該当するものをすべてを含んだリスト形式で返す）


for presentation_html in presentation_html_list:
    print(presentation_html.h3.get_text())
# presentation_html_listから更に<h3>タグで絞り込み
# get_text()でHTMLタグを取り除き、printで表示させる