# 2維列表，巢狀迴圈
# i = 行，有4行
# j = 列，有3列

num = [
     [0,1,2],
     [3,4,5],
     [6,7,8],
     [9] 
]

print(num[3][0])

for i in num:
    for j in i:
        print(j)

#3維
abc=[ 
        [
         
         [0,5,6]
    ]
]
print(abc[0][0][2])