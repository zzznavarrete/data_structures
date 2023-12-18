"""
Merge-operations-to-turn-array-into-a-palindrome


You are given an array nums consisting of positive integers.

You can perform the following operation on the array any number of times:

Choose any two adjacent elements and replace them with their sum.
For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
Return the minimum number of operations needed to turn the array into a palindrome.

 

Example 1:

Input: nums = [4,3,2,1,2,3,1]
Output: 2
Explanation: We can turn the array into a palindrome in 2 operations as follows:
- Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
- Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
The array [4,3,2,3,4] is a palindrome.
It can be shown that 2 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.
"""

class Solution:
    def minimumOperations(self, nums: list) -> int:
    
        # Border case, empty list
        if len(nums) == 0:
            return 0
        
        # Border case, if len(list) < 3
        if len(nums) < 3:
            return sum(nums)


        left, right = 0, len(nums) - 1

        # Variable to count performed operations
        ops_counter:int = 0

        palindrome_found:bool = False
        try:
            while not palindrome_found:
                
                l_value:int = nums[left]
                r_value:int = nums[right]
                aux_value:int = 0
                if r_value < l_value:
                    # Sum and delete at the right of the array
                    aux_value = nums[right - 1]
                    upd_right = r_value + aux_value

                    # Update the array with the updated value
                    nums[right] = upd_right

                    # delete the aux position
                    del nums[right - 1]

                    # Update right pointer to -1 position given the new array shape
                    right -= 1

                    # Sum 1 to performed operations
                    ops_counter += 1

                elif r_value > l_value:
                    # Sum and delete at the left of the array
                    aux_value = nums[left + 1]
                    upd_left = l_value + aux_value

                    #Update the array with the updated value
                    nums[left] = upd_left

                    # delete the aux position
                    del nums[left + 1]

                    # Update rigth pointer to -1 position given the new array shape
                    right -= 1

                    # Sum 1 to performed operations
                    ops_counter += 1

                else:
                    # left and right are equal, check if palindrome, if not, move the pointers

                    # Check if the array has a middle value
                    
                    if (len(nums) - 1) % 2 == 0:
                        middle = int(len(nums) / 2)
                        #print('middle= ', middle)
                        left_part = nums[:middle]
                        right_part = nums[middle+1:][::-1]

                        # If this enters, then BAM, it is a palindrome
                        if left_part == right_part:
                            palindrome_found = True
                            #print('pal found= ', palindrome_found)
                            break

            
                    left += 1
                    right -= 1
        except:
            return 0

        

        return ops_counter
        


        