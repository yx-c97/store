username="于锌"
age="25"
sex="男"
high="1.80"
weight="65"


print("我叫:",username,"我今年:",age,"岁,","我是:",sex,"性,","我身高:",high,"m,","我体重:",weight,"kg.")


info='''
-----------个人展示-----------------
姓名:{username}
年龄:{age}岁
身高：{high}m
体重:{weight}kg
-----------------------------------

'''
print(info.format(username=username,age=age,high=high,weight=weight))




score=input("请输入您的分数")
score=int(score)

if score>=90 and score<=100:
    print("优秀，very good")
elif score>=80 and score<90:
    print("良，GOOd")
elif score>=70 and score<80:
    print("及格，不错")
elif score>=60 and score<70:
    print("及格，不错")
elif score>=0 and score<60:
    print("不及格，试卷正在路上")
else:
    print("成绩不合法")



import prictice
num=int(prictice.random() * 100)
i=0
while True:
    a=int(input("请输入您猜的数"))
    i =i +1
    if a>num :
        print("大了")
