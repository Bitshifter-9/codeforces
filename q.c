lis=list(map(int,input().split()))
a=lis[0]
for i in range(1,len(lis)):
    a=a^lis[i]
print(a)