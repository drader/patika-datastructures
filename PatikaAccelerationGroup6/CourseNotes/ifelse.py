"""
# Task
Given an integer n perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 print Not Weird
If n is even and in the inclusive range of 6 to 20 print Weird
If n is even and greater than 20, print Not Weird

# Input Format
A single line containing a positive integer, n

# Constraints
1 <= n <= 100

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0
3

Sample Output 0
weird

Explanation 0
n = 3
n is odd and odd numbers are weird, so print Weird.

"""

n = int(input("Sayi : "))

if (n%2==0) and (n<6 or n>20):
    print("Not Weird")
else:
    print("Weird")
    
