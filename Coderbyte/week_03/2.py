"""
Letter Count
Have the function LetterCount(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces. 
"""

"""
Input: "Hello appppple pie"
Output: Hello
Input: "No words"
Output: -1 
"""

"""
def LetterCount(strParam):

  # code goes here
  return strParam

# keep this function call here 
print(LetterCount(input()))
"""

def LetterCount(strParam):

    txt = strParam.split()
    res = []
    c = 0

    for i in range(len(txt)):
        for j in txt[i]:
            x = txt[i].lower().count(j)
            #print(x, j)
            if x>1 and x>c:
                c = x
                res = txt[i] 
            #print(x, j, res)
    return res if len(res)>0 else -1

# keep this function call here 
print(LetterCount(input()))