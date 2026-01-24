t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    
    if lis[0]==0 and lis[-1]==0:
        print("Bob")
    else:
        print("Alice")