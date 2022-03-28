"""
Parallel Sums
Have the function ParallelSums(arr) take the array of integers stored in arr which will always contain an even amount of integers, and determine how they can be split into two even sets of integers each so that both sets add up to the same number. If this is impossible return -1. If it's possible to split the array into two sets, then return a string representation of the first set followed by the second set with each integer separated by a comma and both sets sorted in ascending order. The set that goes first is the set with the smallest first integer.

For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11], then your program should output 1,11,20,35,8,16,21,22
Examples
Input: [1,2,3,4]
Output: 1,4,2,3
Input: [1,2,1,5]
Output: -1 
"""
from itertools import combinations

def foo(arr):
    total = sum(arr)
    if total%2: return -1

    arr.sort()

    comb = combinations(arr, len(arr)//2)

    result = [list(i) for i in comb if sum(i)==total//2]

    r = [result[len(result)//2-1], result[len(result)//2]]

    return ",".join(map(str, sum(r, [])))


def ParallelSums(arr):
    arr = sorted(arr)
    sum_arr = sum(arr)
    l_arr = len(arr)
    h_arr = l_arr/2
    t1 = []
    t2 = []

    if sum_arr%2:
        return -1

    for i in range(len(arr)):
        
#        l_t1 = len(t1)
#        l_t2 = len(t2)
        s_t1 = sum(t1)
        s_t2 = sum(t2)
        s_arr = sum_arr - (s_t1 + s_t2)

        print(arr[i], s_arr/(len(arr)-i))

        if (arr[i] < (s_arr/(len(arr)-i))) and (len(t1)<=len(t2)):
            t1.append(arr[i])
        else:
            t2.append(arr[i])
        print(t1, t2)
        
    return t1 + t2



a = [16, 22, 35, 8, 20, 1, 21, 11]

# keep this function call here 
print(ParallelSums(a))



