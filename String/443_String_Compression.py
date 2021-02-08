'''
Two Pointers

Begin with an empty string s. 
For each group of consecutive repeating characters in chars:

1. If the group's length is 1, append the character to s.
2. Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, 
but instead be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

Ex: 
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''

def compress(chars):
    i, count = 0, 1
    for j in range(1, len(chars)): # 1,2,3,4,5,6
        if chars[j] == chars[j-1]:
            count += 1
        else:
            chars[i] = chars[j-1]
            i += 1
            if count > 1:
                for m in str(count):
                    chars[i] = m
                    i += 1
            count = 1
    
    chars[i] = chars[-1]
    i += 1
    if count > 1:
        for m in str(count):
            chars[i] = m
            i += 1
    
    return i