class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_min, num_max = min(nums), max(nums)
        perfect_mirror:list = [x for x in range(num_min, num_max+1)]
        
        for i in perfect_mirror:
            if i not in nums:
                return i
        
        if num_min != 0:
            return 0
        else:
            return num_max+1
        