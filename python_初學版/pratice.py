# 問答程式

#只引入question.py的Q函式
from question import Q
test =[
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "秋天的楓葉是什麼顏色?\n(a) 綠色\n(b) 紅色\n(c) 黑色\n\n"
]

#把題目和答案分別放
abc =  [
            Q(test[0],"c"),
            Q(test[1],"b"),
            Q(test[2],"b")
        ]


def run_test(number):
    #一開始分數
    score = 0
    #跑題目
    for n1 in number:
        #輸入自己的答案
        ans=input(n1.des)
        if ans==n1.ans:
            score+=1
    print("你得到" +str(score)+"分，共"+str(len(number))+"題")

run_test(abc)       
