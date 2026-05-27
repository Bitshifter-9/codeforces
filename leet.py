s=input()
x=""
for i in range(len(s)):
    for j in range(len(s)+1):
        q=s[i:j]
        w=q[::-1]
        
        if q==w:
            if len(q)>len(x):
                x=q
print(x)