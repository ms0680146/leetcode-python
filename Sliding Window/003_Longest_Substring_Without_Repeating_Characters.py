'''
Solution: Sliding Window + set

sliding window + set
s = 'abcbb'
     01234

暴力法:
a
ab
abc
abcb --> 不用考慮
abcbb --> 不用考慮
b
bc
bcb --> 不用考慮
bcbb --> 不用考慮
c
cb
cbb --> 不用考慮
b
bb --> 不用考慮
b

當 window_end 移動到 3 的時候 char 為 b
此時 set = {a, b, c} 中 window_start = 0 char b在 set 中
所以在 while loop 中反覆移動 window_start
當 window_start 移動到2的位置時
此时 set = {c}, char b 已經不在 set 中
按照這個方式移動
set 的個數最多的值即為最長 substring
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