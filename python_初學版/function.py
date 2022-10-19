#函式 function

#自訂函式
def hello(name,age):
    print("Hello,"+name+"你今年幾歲"+str(age)+"歲")


def hello_2():
    print("Hello")

#呼叫函式
hello("小黑",19)
hello_2()

def add(number1,number2):
    sum=float(number1)+float(number2)
    print(sum)

n1=input("第一個數字")
n2=input("第二個數字")
add  (n1,n2)

def add_2(num1,num2):
    return float(num1)+float(num2)

n3=input("第一個數字")
n4=input("第二個數字")
print(add_2(n3,n4))
