"""
Array Couples
Have the function ArrayCouples(arr) take the arr parameter being passed which will be an array of an even number of positive integers, and determine if each pair of integers, [k, k+1], [k+2, k+3], etc. in the array has a corresponding reversed pair somewhere else in the array. For example: if arr is [4, 5, 1, 4, 5, 4, 4, 1] then your program should output the string yes because the first pair 4, 5 has the reversed pair 5, 4 in the array, and the next pair, 1, 4 has the reversed pair 4, 1 in the array as well. But if the array doesn't contain all pairs with their reversed pairs, then your program should output a string of the integer pairs that are incorrect, in the order that they appear in the array.
For example: if arr is [6, 2, 2, 6, 5, 14, 14, 1] then your program should output the string 5,14,14,1 with only a comma separating the integers.
Examples
Input: [2,1,1,2,3,3]
Output: 3,3
Input: [5,4,6,7,7,6,4,5]
Output: yes 
"""

def ArrayCouples(arr):
    s = len(arr)
    res = []

    #   mylist takes and store the element pairs of the given array
    mylist = [arr[i:i+2] for i in range(0, s, 2)]

    #   Main processes for contidional check
    for j in range(len(mylist)):
        #   A and B  <-->  A' or B'
        if (mylist[j][0] == mylist[j][1]) or (mylist[j][::-1] not in mylist):
            #   The pairs that satisfied the conditions, appended to the result
            res.append(mylist[j])
    
    if len(res) == 0:                                               #   If result list is empty, all pairs has its reverse
        return "Yes"    
    else:
        return str(sum(res, []))[1:-1]                              #   flatten the result list

""" 
    ### An alternative way to flatten result ###
    flat_res = [num for sublist in res for num in sublist]     
    return str(flat_res)[1:-1]
"""

print(ArrayCouples(input()))
