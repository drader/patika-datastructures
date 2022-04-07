"""
Primes:
--------------
Have the function Primes(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16.

Examples:
--------------
Input: 4
Output: false
Input: 1709
Output: true 
"""

def Primes(num):
  n = int(num)
  i = 2
  while i < n:
    if n % i:
      i += 1
    else:
      return "false"
  return "true"

# keep this function call here 
print(Primes(input()))