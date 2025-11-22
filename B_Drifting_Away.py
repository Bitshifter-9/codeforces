t=int(input())
for i in range(t):
    s=input()
    ans=False
    for j in range(len(s)-1):
        if s[j]=="*" and s[j+1]=="<":
            ans=True
            break
        elif s[j]==">" and s[j+1]=="*":
            ans=True
            break
        elif s[j]=="*" and s[j+1]=="*":
            ans=True
            break
        elif s[j]==">" and s[j+1]=="<":
            ans=True
            break
 
    if ans :
        print(-1)
    else:
        
        if s[0]==">":
            ind=0
            cou=0
            for k in range(len(s)):
                if s[k]==">":
                    cou+=1
                else:
                    ind=k-1
                    break
            if ind+1<len(s):
                if s[ind+1]=="*":
                    print(max(cou+1,len(s)-cou))
                else:
                    print(max(cou,len(s)-cou))
            else:
                print(cou)
        elif s[0]=="<":
            ind=0
            cou=0
            for k in range(len(s)):
                if s[k]=="<":
                    cou+=1
                else:
                    ind=k-1
                    break
            if ind+1<len(s):
                if s[ind+1]=="*":
                    print(max(cou+1,len(s)-cou))
                else:
                    print(max(cou,len(s)-cou))
            else:
                print(cou)
        else:
            print(len(s))
            

                    

      