"""
Let's use decorators to build a name directory! You are given some information about people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be: 
Mr. Henry Davids

For Mary George, the output should be:
Ms. Mary George
"""

"""
Input Format:
The first line contains the integer, the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Constraints:
1 <= N <= 10

Output Format:
Output N names on separate lines in the format described above in ascending order of age.

Sample Input:
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output:
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""

"""def getInput():
    res = []
    init = True

    while init:
        a = input()
        if a.isdigit() and 1<=int(a)<=10:
            size = int(a)
            init = False
        else:
            return "Input Error"
        
    for _ in range(size):
        line = tuple(input().split())
        if line:
            res.append(line) 
        else: 
            break        
    return res    

def sort(l):
    return sorted(l, key = lambda x: x[2])

def myOut(myList):
    
    for i in myList:
        return ("Mr. " if i[3] == "M" else "Ms. ") + i[0] + " " + i[1]

myOut(sort(getInput()))"""

import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

"""
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
------------------------
10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M
"""