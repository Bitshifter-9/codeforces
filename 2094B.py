# t=int(input())
# for i in range(t):
#     n,m,l,r=map(int,input().split())
#     a=n/m
#     print(round(l/a),round(r/a))

q = int(input())
for i in range(q):
    n,m,l,r = map(int , input().split())
    a = n/m
    print(round(l/a),round(r/a))