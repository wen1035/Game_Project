#建立一個計算機

def add(n1,n2):
    sum=float(n1+n2)
    print(str(n1)+" + "+str(n2)+" = "+str(sum))


def minus(n1,n2):
    sum=float(n1-n2)
    print(str(n1)+" - "+str(n2)+" = "+str(sum))


def multiplied(n1,n2):
    sum=float(n1*n2)
    print(str(n1)+" * "+str(n2)+" = "+str(sum))


def divided(n1,n2):
    sum=float(n1/n2)
    print(str(n1)+" / "+str(n2)+" = "+str(sum))

#多個註解'''   '''

'''
number=float(input("請輸入第一個數字:"))
number2=float(input("請輸入第二個數字:"))
choice=input("1.加(+)\n2.減(-)\n3.乘(*)\n4.除(/)\n?")

if choice=="1":
    add(number,number2)
elif choice=="2":
    minus(number,number2)
elif choice=="3":
    multiplied(number,number2)
elif choice=="4":
    divided(number,number2)
else:
    print("不支援的運算")
'''