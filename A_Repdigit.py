n=int(input())
s=str(n)
se=set()
for j in s:
    se.add(j)
if len(se)==1:
    print("Yes")
else:
    print("No")