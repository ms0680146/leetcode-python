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