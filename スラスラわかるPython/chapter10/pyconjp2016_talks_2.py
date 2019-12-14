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


with open("pyconjp-2016-talks.txt","w") as f:

    f.write("{0:<10}| {1}\n".format("language","title"))
    f.write("{0:<10}| {0}\n".format("--------"))

    for presentation_html in presentation_html_list:
        presentation_title_text = presentation_html.h3.get_text()

        #presentation_htmlから更に<h3>タグで絞り込み
        if "(en)" in presentation_title_text:
            language = "English"
            title = presentation_title_text.replace("\xa0(en)","")
        elif "(ja)" in presentation_title_text:
            language = "Japanese"
            title = presentation_title_text.replace("\xa0(ja)","")

        f.write("{0:<10}| {1}\n".format(language,title))