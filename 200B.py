n=int(input())
lis=list(map(int,input().split()))
cou=0
for i in lis:
    cou+=(i/100)
print(f'{cou/n*100:.14}')