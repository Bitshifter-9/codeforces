spf=[0]*(1001)
primes=[]
for i in range(2,1001):
    if spf[i]==0:
        spf[i]=i
        primes.append(i)
    for p in primes:
        if p>spf[i] or i*p>1000:
            break
        spf[i*p]=p
print(primes)
# def linear_sieve(n):
#     spf = [0] * (n + 1)
#     primes = []

#     for i in range(2, n + 1):
#         if spf[i] == 0:
#             spf[i] = i
#             primes.append(i)

#         for p in primes:
#             if p > spf[i] or i * p > n:
#                 break
#             spf[i * p] = p

#     return primes, spf
