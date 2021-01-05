a=[1,2,3,4,5,6,7,8,9]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j] > a[i]:
            c = a[j]
            a[j] = a[i]
            a[i] = c
print("list=",a)