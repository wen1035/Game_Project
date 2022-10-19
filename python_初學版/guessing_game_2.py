#猜數字，只能猜三次

n=20
number=None
s=0
while s<=3:
    print("只能猜錯三次的猜數字遊戲:")
    number=int(input("請輸入數字: "))
    s+=1
    if number > n:
        print("小一點")
    elif number < n:
        print("大一點")
      
if s<=3:
        print("恭喜猜對")
else:
    print("猜錯三次了喔，你失敗了")

