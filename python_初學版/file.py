#  檔案的  讀取、寫入

#open("檔案路徑", mode="開啟模式")
# 絕對路徑 ex. C:/users/123.txt
# 相對路徑 ex. 123.txt

# mode="r" 讀取
# mode="w" 覆寫，全蓋掉
# mode="a" 在原先的資料後寫東西

file = open("123.txt",mode="r",encoding="utf-8")
#一次全讀檔
#print(file.read())
#把每一行的資料都放到列表裡面
#print(file.readlines())
print("一行一行讀檔:")
for line in file:
    print(line)
file.close()


