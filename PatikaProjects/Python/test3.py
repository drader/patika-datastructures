"""
Have the function DifferentCases(str) take the str parameter being 
passed and return it in upper camel case format where the first letter 
of each word is capitalized. The string will only contain letters and 
some combination of delimiter punctuation characters separating each word.

For example: if str is "Daniel LikeS-coding" then your program should 
return the string DanielLikesCoding.
"""

"""
Input: "cats AND*Dogs-are Awesome"
Output: CatsAndDogsAreAwesome
Input: "a b c d-e-f%g"
Output: ABCDEFG 
"""

def DifferentCases(strParam):
    r = ""
    s = strParam.lower()
    c = False
    for i in range(len(s)):

        if (s[i]>='a' and s[i]<='z'):
            if c or i==0:
                r+=s[i].upper()
                c = False
            else:
                r+=s[i]
        else:
            r+=''
            c = True 
    return r


m = "cats AND*Dogs-are Awesome"
k = "a b c d-e-f%g"

print(m)
# keep this function call here 
print(DifferentCases(m))