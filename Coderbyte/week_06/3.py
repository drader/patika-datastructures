"""
Gas Station:
--------------
Have the function GasStation(strArr) take strArr which will be an an array consisting of the following elements: N which will be the number of gas stations in a circular route and each subsequent element will be the string g:c where g is the amount of gas in gallons at that gas station and c will be the amount of gallons of gas needed to get to the following gas station.

For example strArr may be: ["4","3:1","2:2","1:2","0:1"]. Your goal is to return the index of the starting gas station that will allow you to travel around the whole route once, otherwise return the string impossible. For the example above, there are 4 gas stations, and your program should return the string 1 because starting at station 1 you receive 3 gallons of gas and spend 1 getting to the next station. Then you have 2 gallons + 2 more at the next station and you spend 2 so you have 2 gallons when you get to the 3rd station. You then have 3 but you spend 2 getting to the final station, and at the final station you receive 0 gallons and you spend your final gallon getting to your starting point. Starting at any other gas station would make getting around the route impossible, so the answer is 1. If there are multiple gas stations that are possible to start at, return the smallest index (of the gas station). N will be >= 2.

Examples:
------------
Input: ["4","1:1","2:2","1:2","0:1"]
Output: impossible
Input: ["4","0:1","2:2","1:2","3:1"]
Output: 4 
"""

def shiftArr(arr):
    arr.append(arr.pop(0))
    return arr

def GasStation(strArr):
    sNum = int(strArr[0])
    val = strArr[1:]

    for k in range(sNum):
        val[k] = list(map(int, val[k].split(":")))

    for i in range(sNum):
        total = 0
        for j in range(sNum):
            total += val[j][0] - val[j][1]
            if total < 0:
                val = shiftArr(val)
                break
            elif j+1 == sNum:
                return i+1
    return "impossible"    



a = ["4","1:1","2:2","1:2","0:1"]
b = ["4","0:1","2:2","1:2","3:1"]
c = ["4","1:1","2:2","1:2","0:1"]
d = ["4","0:1","2:2","1:2","1:1"]
e = ["5","3:3","1:2","2:2","3:2","4:3"]
f = ["5","0:1","2:1","3:2","4:6","4:3"]
g = ["2","1:2","1:2"]
h = ["6","3:2","2:2","10:6","0:4","1:1","30:10"]


print("imp : ", GasStation(a))    #imp
print(" 4  : ", GasStation(b))    #4
print("imp : ", GasStation(c))    #imp
print("imp : ", GasStation(d))    #imp
print(" 3  : ", GasStation(e))    #3
print(" 2  : ", GasStation(f))    #2
print("imp : ", GasStation(g))    #imp
print(" 1  : ", GasStation(h))    #1