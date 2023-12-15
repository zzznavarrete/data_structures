"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindrome (word that is the same in backwards) in a given input string.

        Args.
        s: str = String of characters.

        Returns.
        result: str =  Longest found palindrome.
        """
        # Edge case: No input
        if len(s) == 0:
            return ''
        
        # Edge case: 1 letter
        if len(s) == 1:
            return s

        result:str = ''

        for i, char in enumerate(s):
            
            last_char_point:int = len(s) 
            while last_char_point > i:
                complement:str = char + s[i+1:last_char_point]
                if complement == complement[::-1]:
                    if len(complement) > len(result):
                        result = complement
                    break
        
                last_char_point -= 1

            if len(result) > len(s[i+1: len(s)-1]):
                break
        
        return result