'''
Solution: Sliding Window + Hash Map

Sliding Window needs two pointers: i(continue move forward), start
Hash Map: Store char counts
Global_count, Local_count: Store the length of non-repeating char
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

'''
sliding window + set
s = 'abcbb'
     01234
當 window_end 移動到3的時候char為b，此時，set = {a, b, c}中，window_start=0，char b在set中。
所以在while loop中反覆移動 window_start，當 window_start 移動到2的位置時，此时set = {c},char b 已經不在set中。
按照這個方式移動，set的個數最多的值即為最長substring。
'''
def lengthOfLongestSubstringSolutionSet(s):
    local_count = 0
    global_count = 0
    non_repeating_chars = set()
    window_start = 0
    window_end = 0
    
    while window_end < len(s):
        if s[window_end] not in non_repeating_chars:
            non_repeating_chars.add(s[window_end])
            local_count = window_end - window_start + 1
            global_count = max(global_count, local_count)
            window_end += 1
        else:
            non_repeating_chars.remove(s[window_start])
            window_start += 1
    return global_count