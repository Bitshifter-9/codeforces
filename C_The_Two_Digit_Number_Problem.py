def solve(n):
  s=str(n)
  def ct(al):
    al=set(al)
    if not al or (len(al)==1 and 0 in al):
      return 0
    mm={}
    def dp(ps,tg,st):
      if ps==len(s):
        return 1 if st else 0
      sc=(ps,tg,st)
      if sc in mm:
        return mm[sc]
      lm=int(s[ps]) if tg else 9
      rs=0
      for d in range(10):
        if d not in al:
          continue
        if d>lm:
          continue
        if not st and d==0:
          rs+=dp(ps+1,False,False)
        else:
          rs+=dp(ps+1,tg and (d==lm),True)
      mm[sc]=rs
      return rs
    return dp(0,True,False)
  tt=0
  for d in range(10):
    tt+=ct([d])
  for x in range(10):
    for y in range(x+1,10):
      cn=ct([x,y])
      cn-=ct([x])
      cn-=ct([y])
      tt+=cn
  return tt
n=int(input())
print(solve(n))