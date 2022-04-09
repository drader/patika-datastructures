x = [[1, 2], [3, 4], [5, 6, 7]]
s = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

final = []
reversed = []

def flat(k):
    sublist = []
    for i in k:
        flat(i) if type(i)==list else final.append(i)
    return sublist

def reverse(k):
    sublist = []
    for i in k:
        reverse(i) if type(i)==list else reversed.insert(0,i)
    return sublist

a = x

flat(a)
reverse(a)

print(final)
print(reversed)























"""def getlist(l):
    excluded = [","," ","[","]","'"]
    res = []
    for i in l:
        if i not in excluded:
            res.append(i)
    return res"""