"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
"""



class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Return the k factor of an n number.
        """

        # Border case, n == 0
        if n == 0:
            return -1 
        
        # Border case, n is 1 
        if n == 1:
            return 1


        # Getting all the numbers from 1 to n
        numbers_to_check:list = [num for num in range(1, n+1)]



        factor_counter:int = 0
        # Checking the factor
        for num in numbers_to_check:
            if n % num == 0:
                factor_counter += 1

                if factor_counter == k:
                    return num

        
        return -1
            
        

        



    