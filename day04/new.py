import random
shop=[
    ["iphone 8p",1000],
    ["mac loptop",12000],
    ["twatch",500],
    ["lenovo pc",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]

for item ,value in enumerate(shop):
    print(item,value)




while True:
    salary =input("请初始化您的薪资")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        print("请输入合法的薪资！")



mycart=[]



shop=[
    ["iphone 8p",1000],
    ["mac loptop",12000],
    ["twatch",500],
    ["lenovo pc",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]
sum=0
while True:
    print("--------------------欢迎来到艾冬雪购物商城-------------------")
    for item, value in enumerate(shop):
        print(item, value)
    chose = input("请输入您要买的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop):
            print("\033[41;20;1m输入商品不存在！\033[0m")
        else:
            if salary < shop[chose][1]:
                print("\033[41;20;1m，您的余额不足！\033[0m")
            else:
                mycart.append(shop[chose])
                salary = salary - shop[chose][1]
                print("\033[32;20;1m购买成功！余额为：",salary,"\033[0m")
                sum = sum + shop[chose][1]
    elif chose == 'Q' or chose == 'q':
        break
    else:
        print("您的输入不合法！请重新输入！")
choice=["man1000减200","满4000减800","满10000减2000"]
print("------------------------欢迎下次光临！----------------------------")
for item in mycart:
    print(item)
print("您的余额为：",salary)
if sum>0 and sum<5000 :
        print("赠送200积分")
else:
        print("赠送400积分")
print("以下是您的购物车信息：")

print("您的优惠券为：",random.choice(choice))
dis=0
if random.choice(choice)=="满1000减200":
    dis=200
elif random.choice(choice)=="满4000减800":
    dis=800
elif random.choice(choice)=="满10000减1800":
    dis=1800
print("您本次消费金额为：",sum)
if sum>=dis:
    money=sum-dis
else:
    money=sum
    print("您的应付金额为：",money)














