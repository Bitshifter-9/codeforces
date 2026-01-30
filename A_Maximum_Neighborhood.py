t = int(input())
for _ in range(t):
    n = int(input())
    x = []
    co = 1
    for o in range(n):
        arr = []
        for j in range(n):
            arr.append(co)
            co += 1
        x.append(arr)
    
    max_cost = 0
    for p in range(n):
        for q in range(n):
            val = x[p][q]
            cost = val
            if p > 0:
                cost += x[p-1][q]
            if p < n-1:
                cost += x[p+1][q]
            if q > 0:
                cost += x[p][q-1]
            if q < n-1:
                cost += x[p][q+1]
            max_cost = max(max_cost, cost)
    
    print(max_cost)
