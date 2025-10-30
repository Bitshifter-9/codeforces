n=int(input())
n+=1
while True:
    s=str(n)
    se=set()
    for i in s:
        se.add(i)
    
    if len(se)==len(s):
        print(n)
        break
    n+=1
