
a=int(input("请输入第一条边"))
b=int(input("请输入第二条边"))
c=int(input("请输入第三条边"))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c and a==c:
        print("构成等边三角形")

    elif a==b or b==c or a==c:
        print("构成等腰三角形")

    else:
            print("构成普通三角形")

else:
         print("无法构成三角形")
