#if判斷句
hungry=True
if hungry:
    print("吃飯")

score=100
if score==100:
    print("吃饗食天堂")
elif score>=80:
    print("吃陶板屋")
else:
    print("吃咖哩")

score=100
rainy=True
if score==100 and rainy==True:
    print("給你1000元")
elif score==80 or rainy==False:
    print("給你100元")
elif score!=60 and not(rainy):
    print("給你60元") 
else:
    print("給你1元")


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return 2
    else:
        return num3

print(max_num(2,3,5))
