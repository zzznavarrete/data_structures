"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

"""
class Solution:
    def strStr(self, haystack:str, needle:str) -> int:

        words_list:list = [x for x in haystack]
        

        counter:int = 0
    

        for index, _ in enumerate(words_list):
            
            if index + len(needle) <= len(words_list):
                if "".join(words_list[index: index + len(needle)]) == needle:
                    return counter
            counter += 1
        
        return -1
        
    

if __name__ == '__main__':
    haystack = 'hello'
    needle = 'll'
    
    sol = Solution()
    print(sol.strStr(haystack=haystack, needle=needle))
    