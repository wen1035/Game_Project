#for 迴圈

#for 變數 in 字串 or 列表:
#    要重複執行的程式碼 

for num in [0,1,2,3,4]:
    print(num)

#印出2到6
for num_2 in range(2,7):
    print(num_2)

#pow 次方，2的6次方
print(pow(2,6))

def power(base_num,pow_num):
    abc=base_num
    for i in range(pow_num-1):
        abc*=base_num
    return abc

print(power(2,5))
