"""
Given an integer array nums, return all the triplets: 
    - [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

class Solution:

    def threeSum(self, nums: list) -> list:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums:list, i:int, res:list) -> list:
        left, right = i + 1, len(nums) - 1
        while(left < right):
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

if __name__ == "__main__":
    #input_:list = [-1,0,1,2,-1,-4] # should return [[-1,-1,2],[-1,0,1]]\
    input_ =[-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(input_))
