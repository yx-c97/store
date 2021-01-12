class car :
    __num=4
    __color="宝石蓝"
    __brand="奥迪A8"
    def setunm(self,num):
        if num<1:
            print("不是有效数据")
        else:
            self.__num=num
    def getnum(self):
        return  self.__num
    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color
    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand


    def run(self):
        print(self.__color,"颜色的车，有",self.__num,"个轮子在大马路上跑来跑去！！！！")


    def push(self):
        print(self.__color,"颜色的车已经拉了50t货了")



#造车创建对象
c=car()

#添加属性  赋值
c.run()
c.push()

c.unm=5
c.run()