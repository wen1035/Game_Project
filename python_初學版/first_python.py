# 基本資料型態 & 變數
print("小黑")
print(" /|")
print("/_|")
print(87)
print(8+7)
print(1.0/3)#這樣就會有小數點

#字串
#"小黑" or '小黑'

#數字
87
-87
160.5

#布林值
True
False

name="我"
agd=87
zxc=True
print(name+"就是我")

#在終端機打cls可清除紀錄

abc="Hello worlds"
print("Hello worlds")
print("Hello \nworlds")
print("hello \" "+"worlds")

#函式
print(abc.lower())#全變小寫字母
print(abc.upper())#全變大寫字母
print(abc.isupper())#回傳布林值，判斷abc的字串裡的字母是否全大寫
print(abc.islower())#回傳布林值，判斷abc的字串裡的字母是否全小寫
print(abc.lower().isupper())
print(abc[0])
print(abc.index("h"))#找"H"在abc字串裡的位置
print(abc.replace("h","H"))#前是要替換的值，後是要替換成什麼，它會全換
number=8
print(str(number))#從數字8變字串8
#數字跟字串不能疊加  ex. (8+"djofk")
print(abs(number))#絕對值
print(pow(2,4))#2的4次方
print(max(2,3,46,488,6,100))#最大值
print(min(2,3,46,488,6,100))#最小值
print(round(5.6))#四捨五入

from math import *#引入數學函式模板
print(floor(5.1))#無條件捨去
print(ceil(5.1))#無條件進位
print(sqrt(4))#開根號


