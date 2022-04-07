"""
Longest Word:
----------------
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

Examples:
------------
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love 
"""
import re

def LongestWord(sen):
    res = 0
    words = sen.split()
    k = 0
    res = words[0]
    for i in range(len(words)):
        c = len(re.sub(r'[\W+]', '', words[i]))
        if c>k:
            k = c
            res = words[i]
    return res

a = "fun&!! time lovge"

#print(a.split())

print(LongestWord(a))