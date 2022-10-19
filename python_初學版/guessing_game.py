#猜數字遊戲
s=0
n=20
print("歡迎來到猜數字遊戲")

while s==0:
    number=input("請輸入數字:")
    if number==str(n):
        print("恭喜您猜對了!")
        s=1
    else:
        if number>str(n):
            print("猜錯了，小一點")
        else:  
            print("猜錯了，大一點")
    
