# -*- coding: utf-8 -*-
#使用者に名前と年齢を聞き、100歳になる年を伝えるプログラム
import datetime

your_name = input("あなたの名前は？:")
your_age = input("年齢を入力して:")

years = datetime.date.today().year
hundred_years_after = int(years) - int(your_age) + 100

print("あなたの名前は" + your_name + "で、年齢は" + str(your_age) + "歳ですね")
print("今年は" + str(years) + "年です")
print(your_name + "が100歳になる年は" + str(hundred_years_after) + "年です。")

