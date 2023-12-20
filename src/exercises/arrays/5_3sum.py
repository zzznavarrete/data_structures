"""
Given an integer array nums, return all the triplets: 
    - [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

class Solution:

    def threeSum(self, nums: list) -> list:
        """
        Returns all the non-repeated triplets that sum togethers results 0.

        Args.
        nums: list = List of integers.

        Returns.
        List[int] = List of triplets. 
        """
        # Variable in which the triplets will be stored.
        res: list = []
        
        # Given that this solution is through sort, I proceed to sort the array.
        nums.sort()

        for i in range(len(nums)):
            
            # Given that this solution sorts the array, then any non-negative number will be followed by -
            # - another non-negative numbers an so on. And with non-negative is impossible to sum up to 0, then 
            # - we must break the loop.
            if nums[i] > 0: 
                break

            # We will only look for triplets if we do not have repeated numbers.
            if i == 0 or nums[i - 1] != nums[i]:
                # Now we call the O(n) function twoSumII to check triplets in my current 'i' position
                self.twoSumII(i, nums, res)
            
        return res


    def twoSumII(self, i:int, nums:list , res:list) -> None:
        """
        Append to the variable 'res' the found triplets.

        Args.
        i:int = Current position of the main function which calls this secondary function.
        nums:list = Array of numbers to look for triplets.
        res:list = Array in which the found triplets will be stored.

        Returns.
        None.
        """

        # Pointers, left is from the next number of my 'i' element and right from the last element of the array.
        left, right = i + 1, len(nums) - 1 

        while left < right:
            sum_:list = nums[i] + nums[left] + nums[right] # Potential triplet

            if sum_ > 0: # If if is greater than Zero then I need to decrease my highest number
                right -= 1
            elif sum_ < 0: # If it is lower than Zero, then I need to increase the lower number
                left += 1
            else: # If is else is because the 'sum_' variable is equal to Zero, which is what we're looking into
                res.append([nums[i] , nums[left] , nums[right]])
                left += 1
                right -= 1

                # For the sake of avoid repeated numbers, we implement the following for loop.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1





if __name__ == "__main__":
    #input_:list = [-1,0,1,2,-1,-4] # should return [[-1,-1,2],[-1,0,1]]\
    input_ =[-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(input_))
