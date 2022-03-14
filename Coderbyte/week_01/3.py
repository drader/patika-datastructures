a = ["(1,2,3)","(4,5,6)","(7,8,9)"]
result = []
for i in n:
    result.append(list(map(int,i[1:][:-1].split(","))))
   # brd[9*row + col]
print(result)