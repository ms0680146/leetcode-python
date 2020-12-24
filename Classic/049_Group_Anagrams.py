'''
Solution: Hash Map

sort each variable
eat -> aet, check hash map, {'aet': ['eat']}
tea -> aet, check hash map, {'aet': ['eat','tea']}
tan -> ant, check hash map, {'aet': ['eat','tea'], 'ant': ['tan']}

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
----------

'''
def groupAnagrams(strs):
    anagram_dict = {}
    for var in strs:
        var_sorted = ''.join(sorted(var))
        if var_sorted in anagram_dict:
            anagram_dict[var_sorted].append(var)
        else:
            anagram_dict[var_sorted] = [var]
    print(anagram_dict)

    results = []
    for result in anagram_dict.values():
        results.append(result)
    return results
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]