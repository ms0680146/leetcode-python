'''
Solution: Sliding Window + set

sliding window + set
s = 'abcbb'
     01234
當 window_end 移動到3的時候char為b，此時，set = {a, b, c}中，window_start=0，char b在set中。
所以在while loop中反覆移動 window_start，當 window_start 移動到2的位置時，此时set = {c},char b 已經不在set中。
按照這個方式移動，set的個數最多的值即為最長substring。
'''
def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring('abcabcbb')) # 3
print(lengthOfLongestSubstring('bbbbb')) # 1
print(lengthOfLongestSubstring('')) # 0