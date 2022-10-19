#  檔案的  讀取、寫入

#open("檔案路徑", mode="開啟模式")
# 絕對路徑 ex. C:/users/123.txt
# 相對路徑 ex. 123.txt

# mode="r" 讀取
# mode="w" 覆寫，全蓋掉
# mode="a" 在原先的資料後寫東西

file_2 = open("456.txt",mode="w",encoding="utf-8")
file_2.write("hello")
file_2.close()