t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    se=set()
    cou=0
    for j in range(n):
        if s[j]!=s[(j+1)%n]:
            cou+=1
    ans=False
    for k in range(n):
        if s[k]==s[(k+1)%n]:
            ans=True
            break
    if ans:
        cou+=1
    print(cou)
# t=int(input())
# for i in range(t):
#     n=int(input())
#     s=input()
#     se=set()
#     for j in s:
#         se.add(j)
#     ans=False
#     cou=len(se)
#     for k in range(n):
#         if s[k]==s[(k+1)%n]:
#             ans=True
#             break
#     if ans:
#         cou+=1
#     print(cou)