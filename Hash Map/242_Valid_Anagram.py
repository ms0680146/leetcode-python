'''
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

countS: {
    a: 3
    n: 1
    g: 1
    r: 1
    m: 1
}

countT: {
    a: 3
    n: 1
    g: 1
    r: 1
    m: 1
}

Example 2:
Input: s = "rat", t = "car"
Output: false

countS: {
    r: 1
    a: 1
    t: 1
}

countT: {
    r: 1
    a: 1
    t: 1
} 

'''

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

