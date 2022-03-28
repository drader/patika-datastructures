"""Two Sum
Have the function TwoSum(arr) take the array of integers stored in arr, and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. Pairs should be separated by a space. So for the example above, your program would return: 5,2 -4,11

If there are no two numbers that sum to the first element in the array, return -1
Examples
Input: [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
Output: 6,11 10,7 15,2
Input: [7, 6, 4, 1, 7, -2, 3, 12]
Output: 6,1 4,3 
"""

"""
1. For input [6, 2] the output was incorrect. The correct output is -1

2. For input [100, 90, 90, 90, 90, 11] the output was incorrect. The correct output is -1

3. For input [4, 5, 2, 1] the output was incorrect. The correct output is -1
"""
from itertools import combinations, permutations

def TwoSum(arr):
    res = []
    for i in range(len(arr)-1):
        if arr[0]-arr[i+1] in arr[i+2:]:
            res.append([arr[i+1], arr[0]-arr[i+1]])
    k = ""
    for i in range(len(res)):
        k += f"{res[i][0]},{res[i][1]} "
    return k if len(res) != 0 else -1




def foo(arr):
    numberOfString = ""
    for index in range(1,len(arr)):
        for indexOfNumber in range(index+1, len(arr)):
            if arr[0] == arr[index] + arr[indexOfNumber]:
                line1 = str(arr[index])
                line2 = str(arr[indexOfNumber])
                numberOfString += line1 + ","+ line2 + " "

    return numberOfString if numberOfString != "" else -1


a = [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
#a = [100, 90, 90, 90, 90, 11]
#a = [6, 2]
#a = [4, 5, 2, 1]

print(TwoSum(a))
print(foo(a))

