
read = open("景甜.jpg","rb")
write = open("景甜1.jpg","wb")
data = read.read()
write.write(data)
read.close()
write.close()


