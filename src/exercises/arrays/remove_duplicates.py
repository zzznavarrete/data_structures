class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right =0, 1
        while right < len(nums):
            if nums[right] == nums[left]:
                # are equal
                del nums[right]
                right = left
                right += 1
            else:
                #not equal
                left += 1
                right += 1
        
        return len(nums)
        