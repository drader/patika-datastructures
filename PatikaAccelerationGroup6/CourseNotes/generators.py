def square(l):
    res = []

    for e in l:
        res.append(e*e)
    return res

l = [1, 2, 3]
print(square(l))


def square_generator(l):
    for e in l:
        yield e*e

l = [3, 5, 8]

g = square_generator(l)                     #   Generator created with list
print(next(g))                              #   calculates result for the next element of the list
print(next(g))                              #   gives exception error after all elements were calculated
print(next(g))

g = square_generator(l)                     #   Generator created with list
for res in g:                               #   calculates result for the rest of list elements
    print(res)

g = (x*x for x in l)                        #   Generator created with list comprehension
print(next(g))                              #   calculates result for the next element of the list
#print(next(g))
#print(next(g))

for e in g:                                 #   calculates result for the rest of list elements
    print("e : ",e)                         


l = [1, 2, 3, 4, 5]
g = (x*x for x in l)                        #   generator created with list comprehension
print(list(g))                              #   print all elements of the generator as a list

l = [1, 2, 3, 4, 5]
g = square_generator(l)                     #   generator created
print(list(g))                              #   print all elements of the generator as a list


def range_generator(start, end, step):      #   Generator function created
    current = start
    while current < end:
        yield current                       #   The stack stops at the end of here after next() execution
        print("current : ",current)         #   Following next() execution continues from here
        current += step

r = range_generator(1, 20, 3)

print(next(r))
print(next(r))
print(next(r))

print("Hello")

print(next(r))
print(next(r))
print(next(r))
