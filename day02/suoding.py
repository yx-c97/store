

i=0
while i<3:
     name = "jason"
     mm = "admin"
     a=input("请输入用户名：")
     b=input("请输入密码：")
     if a==name and b==mm :
         print("登录成功")
         break
     elif a!=name and b!=mm :
         print("登录失败")
         i+=1






