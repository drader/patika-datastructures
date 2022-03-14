def PalindromeTwo(strParam):
  s = strParam.lower()
  r = ""
  # Check if is between a-z
  for i in range(len(s)):
    if (s[i]>='a' and s[i]<='z'):
      r += s[i]

  # mid point
  h = len(r)//2 
  
  if len(r)%2:
    h = (len(r)-1)//2
    rRev = r[h+1:][::-1]
  else:
    rRev = r[h:][::-1]

  return True if r[:h] == rRev else False

# keep this function call here 
print(PalindromeTwo(input()))