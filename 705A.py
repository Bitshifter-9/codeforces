n=int(input())
s=""
for i in range(n):
    if i%2==0 and i!=n-1:
        s=s+"I hate that "
    elif i%2!=0 and i!=n-1:
        s=s+"I love that "
    elif i%2==0:
        s=s+"I hate it"
    else:
        s=s+"I love it"
print(s)