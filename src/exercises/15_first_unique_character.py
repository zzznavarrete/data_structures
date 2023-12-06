"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
         
        hash_map_letters: Counter = Counter(list(s))
        
        for key, val in hash_map_letters.items():
            if val == 1: 
                return list(s).index(key)
        
        return -1
       