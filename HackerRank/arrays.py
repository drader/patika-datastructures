"""
The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.

Task:
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input Format:
A single line of input containing space separated numbers.

Output Format:
Print the reverse NumPy array with type float.

Sample Input:
1 2 3 4 -8 -10

Sample Output:
[-10.  -8.   4.   3.   2.   1.]

"""
import numpy as np

def arrays(arr):
    return np.array(arr[::-1], dtype='<f8')

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


"""import numpy as np

a = [x for x in input().split()][::-1]
#b = np.array(a[::-1], dtype='<f8')
b = np.array(a, dtype='<f8')
print(a, type(a[0]))
print(b, type(b[0]))"""