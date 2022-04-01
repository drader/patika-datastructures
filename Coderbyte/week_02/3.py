"""Step Walking
Have the function StepWalking(num) take the num parameter being passed 
which will be an integer between 1 and 1,000 that represents the number 
of stairs you will have to climb. You can climb the set of stairs by 
taking either 1 step or 2 steps, and you can combine these in any order. 

So for example, to climb 3 steps you can either do: 

(1 step, 1 step, 1 step) or (2, 1) or (1, 2). 

So for 3 steps we have 3 different ways to climb them, 
so your program should return 3. Your program should 
return the number of combinations of climbing num steps.

Examples
Input: 1
Output: 1
Input: 3
Output: 3 """

"""
5*1
3*1   +   1*2
1*1   +   2*2

################################# 5
1   1   1   1   1
1   1   1   2
1   1   2   1
1   2   1   1
2   1   1   1
1   2   2
2   1   2
2   2   1

################################# 6
1   1   1   1   1   1
1   1   1   1   2
1   1   1   2   1
1   1   2   1   1
1   2   1   1   1
2   1   1   1   1
1   1   2   2
1   2   1   2
1   2   2   1
2   1   1   2
2   1   2   1
2   2   1   1

################################# 7
1   1   1   1   1   1   1
1   1   1   1   1   2
1   1   1   1   2   1
1   1   1   2   1   1
1   1   2   1   1   1
1   2   1   1   1   1
2   1   1   1   1   1


"""

"""
    x * 1   +   y * 2               i = c(x+y, y)
--------------------------------------------------
    n * 1   +   0 * 2       -->     c(n+0, 0)
  n-2 * 1   +   1 * 2       -->     c(n-2+1, 1)
  n-4 * 1   +   2 * 2       -->     c(n-4+1, 2)
--------------------------------------------------


"""
# Fibonacci ile çöz!


def f(n):
    if n>=0:
        return 1 if (n == 1 or n == 0) else n * f(n-1)

def c(n, r):
    return 1 if r == 0 else int(f(n) / (f(n-r) * f(r)))

def foo(num):

    h = num+1 // 2 if num%2 else (num//2)+1
    res = 0
    
    for i in range(h):
        x = num - (2*i)
        if x<0:
            return res
        y = 0 + i        
        res += c(x+y,y)

    return res

print(foo(5))