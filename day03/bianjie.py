for i in range(0,5) :
    for j in range(0,i+1):
        print("*",end="")
    print()







for i in range(1,10)  :
    for j in range(1,i+1):
        print(j,"x",i,"=",(j*i),"\t",end="")
    print()




a=[1,5,8,3,4,9]

sum=0
for i in range(len(a)):
    sum=(sum+a[i])
print("总和为",sum)




a=[1,5,8,3,4,9]
sum1=0
for i in range(len(a)):
    if a[i]%2==0 :
      sum1=sum1+a[i]
print("偶数和为",sum1)




a=[1,5,8,3,4,9]
i=0

for k in range(0,len(a)):
    if a[k]>i :
        i=a[k]
print("最大值为",i)







a=[2,4,5,7,8,9,6,3,1,10,11]


for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            c=a[j]
            a[j]=a[i]
            a[i]= c
print(a)
























