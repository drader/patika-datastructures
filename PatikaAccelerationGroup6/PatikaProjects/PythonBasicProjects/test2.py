def EquivalentKeypresses(strArr):
  
  print(strArr, strArr[0], strArr[1])
  if strArr[0] in strArr[1]:
      return True
  return False

# keep this function call here 

s = ["a,b,c,d", "a,b,c,d,-B,d"]
k = ["c,a,r,d", "c,a,-B,r,d"]
n = ["q,w,e,r,t,y", "-B,-B,q,w,w,-B,e,r,t,y"]

print(EquivalentKeypresses(n))

""" False Tests
1. For input ["q,w,e,r,t,y", "-B,-B,q,w,w,-B,e,r,t,y"] the output was incorrect. The correct output is true

2. For input ["p,o,i,n,-B,t", "-B,p,o,i,t"] the output was incorrect. The correct output is true

3. For input ["u,m,b,r,r,-B,e,l,l,a", "u,m,b,b,-B,r,e,l,l,a"] the output was incorrect. The correct output is true

4. For input ["c,o,o,-B,o,l", "c,o,o,k,-B,l"] the output was incorrect. The correct output is true

5. For input ["s,t,r,e,e,t", "-B,s,s,-B,t,r,e,e,t"] the output was incorrect. The correct output is true

"""