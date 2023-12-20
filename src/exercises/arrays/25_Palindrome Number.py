"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

"""


class Solution:
    def check_if_int32(self, x:int) -> bool:
        high_limit:int = 2**31 - 1
        low_limit:int = -2**31

        if low_limit <= x <= high_limit:
            return True
        else:
            return False

    def isPalindrome(self, x: int) -> bool:
        
        if self.check_if_int32(x):

            if str(x) == str(x)[::-1]:
                return True
            else:
                return False

        else:
            return False
        