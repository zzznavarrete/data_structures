"""
4 Sum.

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        i:int = 0
        res:list = []
        while i < len(nums):
            indexes = self.threeSum(currI = i, nums=nums, target=target, res = res)
            i += 1
        return res


    def threeSum(self, currI:int, nums:list, target: int, res:list) -> list:
        currJ = currI + 1
        while currJ < len(nums):        
            left, right = currJ + 1, len(nums) - 1
            while left < right:
                num:int = nums[currI] + nums[currJ] + nums[left] + nums[right]
                if num > target:
                    right -= 1
                elif num < target:
                    left += 1
                else:
                    if not [nums[currI], nums[currJ], nums[left], nums[right]] in res:
                        res.append([nums[currI], nums[currJ], nums[left], nums[right]])
                    left += 1
            currJ+=1

    
