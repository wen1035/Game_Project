#列表list
scores=[50,80,50,60,100]
friends=["小黑","小白"]
things=[100,"小黑",True]
print(scores)
print(friends)
print(things)
print(scores[0])#[-1]尾數
print(scores[0:2])#切片，從0取到第2位前，不包含第2位
print(scores[1:])#從1到尾
print(scores[:4])#從投到4前

scores[0]=30
print(scores.count(100))#100有幾個
print(scores.index(100))#100在哪個位子

scores.append(50)#增加值到尾
scores.insert(2,30)#插入，把30放到第2位
scores.remove(60)#刪除
scores.pop()#移除列表最後一位
scores.sort()#排列，小到大
scores.reverse()#相反排
scores.extend(friends)#擴充到尾巴
scores.clear()#全清空

