s1 = [[1, 2], [3, 4], [5, 6, 7]]
s2 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

final = []
reversed = []

def flat(k):
  """
  Flatten the given input list
  """
    sublist = []
    for i in k:
        flat(i) if type(i)==list else final.append(i)
    return sublist

def reverse(k):
  """
  Flatten and reverse the given input list
  """
    sublist = []
    for i in k:
        reverse(i) if type(i)==list else reversed.insert(0,i)
    return sublist

# Choose the input  
a = s1
#a = s2
  
flat(a)
reverse(a)

print(final)
print(reversed)  
