'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}
        len_s1 = len(s1)
        for c in s1:
            if c in s1_hash:
                s1_hash[c] += 1
            else:
                s1_hash[c] = 1
        print(s1_hash)

        s2_hash = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] in s2_hash:
                s2_hash[s2[r]] += 1
            else:
                s2_hash[s2[r]] = 1
            print(s2_hash)
            if r-l + 1 >= len_s1:
                if s2_hash == s1_hash:
                    return True
                if s2_hash[s2[l]] > 1:
                    s2_hash[s2[l]] -= 1
                else:
                    del s2_hash[s2[l]]
                l += 1
