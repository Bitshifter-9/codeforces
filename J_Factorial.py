n=int(input())
ans=[1]
def x(i):
    if i>n:
        return
    ans.append(ans[-1]*i)
    x(i+1)
x(1)
print(ans[-1])
    