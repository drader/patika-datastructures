def ConsonantCount(strParam):

  # code goes here
  s = list("".join(strParam.split(" ")))
  w = ["a","i","e","o","u","A","I","E","O","U"]

  for i in s:
      for j in w: 
          if i == j:
              s.remove(i)

  return len(s)

"""Test Cases - False returned
1. For input "Hewlett-Packard" the output was incorrect. The correct output is 10

2. For input "aaaaaaaa" the output was incorrect. The correct output is 0

3. For input "zz*" the output was incorrect. The correct output is 2
"""