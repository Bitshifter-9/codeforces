t=int(input())
for i in range(t):
    cou=0
    mat=[]
    
    for p in range(10):
        s=input()
        x=[]
        for q in s:
            x.append(q)
        mat.append(x)
    for j in range(10):
        for k in range(10):
           if mat[j][k] == 'X':
                if (j == 0 or j == 9) or (0 == k or k== 9):
                    cou += 1
                elif (j == 1 or j == 8) or (1 == k or k== 8):
                    cou += 2
                elif (j == 2 or j == 7) or (2== k or k== 7):
                    cou += 3
                elif (j == 3 or j == 6) or (3 == k or k== 6):
                    cou += 4
                elif (j == 4 or j == 5) or (4 == k or k== 5):
                    cou += 5
    print(cou)

    




    