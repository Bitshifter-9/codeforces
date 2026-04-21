t=int(input())
n=5000001
spf = list(range(n + 1))
for i in range(2, int(n ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, n + 1, i):
            if spf[j] == j:
                spf[j] = i
cnt = [0] * (n + 1)
for i in range(2, n + 1):
    cnt[i] = cnt[i // spf[i]] + 1
x = [0] * (n + 1)
for i in range(2, n+ 1):
    x[i] = x[i - 1] + cnt[i]

# x=[0,0]
# ans_2=0
# for k in range(2,n+1):
#     z=factor(k)
#     ans_2 += z   
#     x.append(ans_2)
for op in range(t):
    a,b=map(int,input().split())
    print(x[a]-x[b])


    




