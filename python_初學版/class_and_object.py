# 類別class，物件object

class Phone:
    #一開始初始函式，self是物件本身
    def __init__(self,os,number,is_waterproof):
        self.os=os
        self.number=number
        self.is_waterproof=is_waterproof
    
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
    
    def add(self,n1,n2):
        return n1+n2


phone1=Phone("ios",123,True)
print(phone1.number)
print(phone1.is_ios())







# 汽車類別
class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性
    # 方法(Method)
    def drive(self):
        # f是format-string(字串格式化)用法
        print(f"My car is {self.color} and {self.seat} seats.")
        #等於print("My car is " +str(self.color)+" and "+str(self.seat)+" seats.")  

mazda = Cars("blue", 4)
#執行結果：My car is blue and has 4 seats.
mazda.drive()  

'''

物件導向程式設計:
1.類別(Class)
2.物件(Object)
3.屬性(Attribute)
4.建構式(Constructor)
5.方法(Method)

-------------------------------------------------------------------------

1.類別(Class):
-->物件(Object)的藍圖(blueprint)
   ex.就像要生產一部汽車時，都會有設計圖

# 類別名稱的命名原則習慣上使用Pascal命名法，
# 也就是每個單字字首大寫，
# 不得使用空白或底線分隔單字

class MyCars:

-------------------------------------------------------------------------

2.物件(Object):
-->透過類別(Class)實際建立的實體
   ex.就像實際生產出來的汽車

#語法:
# object_name = classname()

abc = Car()

ex.Python也提供了一個函式isinstance()
   來判斷類別(Class)與物件(Object)的關係，
   語法如下：
# isinstance(object_name, class_name)

範例
# 汽車類別
class Cars:
    pass

# 摩托車類別
class Motorcycle:
    pass

# 建立Cars類別的物件
mazda = Cars()

# 執行結果：True
print(isinstance(mazda, Cars)) 
# 執行結果：False
print(isinstance(mazda, Motorcycle)) 

-------------------------------------------------------------------------

3.屬性(Attribute):
-->負責存放物件(Object)的資料

#語法
# object_name.attribute_name = value

範例
print(mazda.color)  # 執行結果：blue
print(mazda.seat)  # 執行結果：4

-------------------------------------------------------------------------

4.建構式(Constructor):
-->建立物件(Object)的同時，會自動執行的方法(Method)

# 在建構式(Constructor)中，
# 初始化物件(Object)的屬性值(Attribute)。
# 至少要有一個self參數，
# 之後利用逗號區隔其他屬性

def __init__(self, color, seat):
　　self.color = color  # 顏色屬性
　　self.seat = seat  # 座位屬性 

-------------------------------------------------------------------------

5.方法(Method):
-->物件(Object)的行為

# 定義方法(Method)和函式(Function)的語法很像，
# 都是def關鍵字開頭，接著自訂名稱，
# 但是方法(Method)和建構式(Constructor)一樣，
# 至少要有一個self參數

def method_name(self):
　　statement

# 方法(Method)
    def drive(self):
        print(f "My car is {self.color} and {self.seat} seats.")

ex. self參數同樣是代表目前的物件

'''
