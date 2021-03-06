'''
Solution: Sliding Window + Hash Map

Sliding Window needs two pointers: i(continue move forward), start
Hash Map: Store char counts
Global_count, Local_count: Store the length of non-repeating char
'''
def lengthOfLongestSubstring(s):
    # Edge Case
    if len(s) == 0:
        return 0
    
    local_count = 0
    global_count = 0
    char_count_mapping = {}
    start = 0

    for i in range(len(s)):
        if s[i] in char_count_mapping:
            char_count_mapping[s[i]] += 1
        else:
            char_count_mapping[s[i]] = 1

        while char_count_mapping[s[i]] > 1:
            char_count_mapping[s[start]] -= 1
            start += 1 
        local_count = i - start + 1
        global_count = max(global_count, local_count)

    return global_count

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