n=int(input())
arr=["abc","bac","acb","cba"]
for i in range(n):
    s=input()
    if s in arr:
        print("YES")
    else:
        print("NO")
