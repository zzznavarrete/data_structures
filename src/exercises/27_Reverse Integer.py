"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""

class Solution:
    def is_in_32bit_range(self, num:int) -> int:
        high_limit:int = 2**31 - 1
        low_limit:int = -2**31

        if low_limit <= num <= high_limit:
            return num
        else:
            return 0


    def reverse(self, x: int) -> int:
        """
        Reverse an integer number and return it only if it is in the range of 32 bit.
        """
        x_string:str = str(x)
        is_negative:bool = False

        # Checking if has some sign at the beginning
        if x_string[0] not in [str(num) for num in range(0,9+1)]:
            if x_string[0] == '-':
                is_negative = True
            
            x_string = x_string[1:]
        
        x_string = int(x_string[::-1])

        if is_negative:
            x_string *= -1


        return self.is_in_32bit_range(x_string)
        



        


        

        