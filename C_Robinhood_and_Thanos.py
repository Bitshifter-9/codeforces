a,b,c,d=map(int,input().split())
p=a/b
q=c/d
print(round(p/(p+q-(p*q)),12))

# 1-(1-p)(1-q)
# 1-(1-q-p+pq)
# =q+p-pq