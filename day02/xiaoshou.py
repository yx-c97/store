print("----------------------------------------欢迎光临海澜之家-----------------------------------------------")
print("====================================================================================================")
print("衣服类别          衣服款式           衣服码数             衣服颜色              衣服价格           衣服数量 ")
print(" 半袖              男款               s                  白色                  90               100")
print(" 半袖              男款               L                  黑色                  50                80")
print(" 半袖              男款               XL                 黑色                  30                70")
print(" 半袖              女款               M                  黄色                  20                10")
print(" 衬衣              女款               S                  白色                  50                20")
print(" 西服              男款               L                  蓝色                  800                5")
print(" 西服              女款               s                  褐色                  1000               3")
print(" 西服              男款               XL                 黑色                  3000               1")
print(" 裙子              女款               s                  白色                  500               20")
print(" 裙子              女款               M                  黑色                  500               30")
print(" 帽衫              男款               S                  灰色                  100               400")
print(" 帽衫              男款               M                  黑色                  200               500")
print(" 帽衫              男款               XL                 黑色                  300                40")
print(" 帽衫              男款               L                  白色                  300                30")
print("======================================================================================================")
print("总金额为：",90*100+50*80+30*70+20*10+50*20+800*5+1000*3+3000*1+500*20+500*30+100*400+200*500+300*40+300*30,"RMB")

clothing="衣服类别"
style="衣服款式"
size="衣服码数"
color="衣服颜色"
pric="衣服价格"
number="衣服数量"

print("----------------------------------------欢迎光临海澜之家-----------------------------------------------")
print("=====================================================================================================")
print("衣服类别","\t\t","衣服款式","\t\t","衣服码数","\t\t","衣服颜色","\t\t","衣服价格","\t\t","衣服数量")

info='''
 {clothing}              {style}             {size}               {color}              {pric}              {number}
'''
a="半袖"
b="男款"
c="s"
d="白色"
e="90"
f="100"

q1="半袖"
q2="男款"
q3="L"
q4="黑色"
q5="50"
q6="100"

w1="半袖"
w2="男款"
w3="L"
w4="黄色"
w5="30"
w6="70"

e1="半袖"
e2="女款"
e3="M"
e4="黄色"
e5="20"
e6="10"

r1="衬衣"
r2="女款"
r3="S"
r4="白色"
r5="20"
r6="10"

t1="西服"
t2="男款"
t3="L"
t4="蓝色"
t5="800"
t6="5"

y1="西服"
y2="女款"
y3="S"
y4="褐色"
y5="1000"
y6="3"

u1="西服"
u2="男款"
u3="L"
u4="黑色"
u5="3000"
u6="1"

i1="裙子"
i2="女款"
i3="S"
i4="白色"
i5="500"
i6="20"


o1="裙子"
o2="女款"
o3="M"
o4="黑色"
o5="500"
o6="30"

a1="帽衫"
a2="男款"
a3="S"
a4="灰色"
a5="100"
a6="400"

s1="帽衫"
s2="男款"
s3="M"
s4="黑色"
s5="200"
s6="500"

d1="帽衫"
d2="男款"
d3="XL"
d4="黑色"
d5="300"
d6="40"

z1="帽衫"
z2="男款"
z3="L"
z4="白色"
z5="300"
z6="30"
print(info.format(clothing=a,style=b,size=c,color=d,pric=e,number=f))
print(info.format(clothing=q1,style=q2,size=q3,color=q4,pric=q5,number=q6))
print(info.format(clothing=w1,style=w2,size=w3,color=w4,pric=w5,number=w6))
print(info.format(clothing=e1,style=e2,size=e3,color=e4,pric=e5,number=e6))
print(info.format(clothing=r1,style=r2,size=r3,color=r4,pric=r5,number=r6))
print(info.format(clothing=t1,style=t2,size=t3,color=t4,pric=t5,number=t6))
print(info.format(clothing=y1,style=y2,size=y3,color=y4,pric=y5,number=y6))
print(info.format(clothing=u1,style=u2,size=u3,color=u4,pric=u5,number=u6))
print(info.format(clothing=i1,style=i2,size=i3,color=i4,pric=i5,number=i6))
print(info.format(clothing=o1,style=o2,size=o3,color=o4,pric=o5,number=o6))
print(info.format(clothing=a1,style=a2,size=a3,color=a4,pric=a5,number=a6))
print(info.format(clothing=s1,style=s2,size=s3,color=s4,pric=s5,number=s6))
print(info.format(clothing=d1,style=d2,size=d3,color=d4,pric=d5,number=d6))
print(info.format(clothing=z1,style=z2,size=z3,color=z4,pric=z5,number=z6))
print("===================================================================")
