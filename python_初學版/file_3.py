#  檔案的  讀取、寫入

#open("檔案路徑", mode="開啟模式")
# 絕對路徑 ex. C:/users/123.txt
# 相對路徑 ex. 123.txt

# mode="r" 讀取
# mode="w" 覆寫，全蓋掉
# mode="a" 在原先的資料後寫東西

file_3 = open("789.txt",mode="a",encoding="utf-8")
file_3.write("\nhello")
file_3.close()

# 另解
#with open("123.txt",mode="a",encoding="utf-8") as file:
    #file.write("\n哈哈") 