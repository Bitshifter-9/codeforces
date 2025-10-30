import math

n, q = map(int, input().split())
lis = list(map(int, input().split()))
root = int(math.sqrt(n)) + 1
a = [-1] * root  
for i in range(n):
    if a[i // root]==-1:
        a[i // root] = lis[i]
    else:
        a[i // root]=min(a[i // root],lis[i])
print(a)

for _ in range(q):
    num, k, u = input().split()
    k = int(k)
    u = int(u)
    if num == "1":  
        idx = k - 1
        block_idx = idx // root
        lis[idx] = u
        a[i // root]=-1
        print(lis,a)
        for i in range(((k//root)*root),((k//root)*root)+root):
            if i%root==0:
                break
            if a[i // root]==-1:
                a[i // root] =lis[i]
            else:
                a[i // root]=min(a[i // root],lis[i])
        print(lis,a)

        # for j in range(k,(k//root)*root):
        #     a[i // root]=min(a[i // root],lis[i])

            
        

    else: 
        l = k - 1
        r = u - 1
        mi = lis[l]
        while l <= r and l % root != 0:
            if mi==-1:
                mi=lis[l]
            else:
                mi= min(mi,lis[l])
            l += 1
        while l + root - 1 <= r:
            mi = min(mi,a[l//root])
            l += root
        while l <= r:
            mi=min(mi,lis[l])
            l += 1
        print(mi)
print(lis,a)



