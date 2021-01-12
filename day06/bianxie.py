lj=input("请输入证件路径：")
read = open(lj,"rb")
write = open("c:\\景甜1.jpg","wb")
data = read.read()
write.write(data)

read.close()
write.close()
