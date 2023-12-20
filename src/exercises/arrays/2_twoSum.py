class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        Return the indexes of two elements that sums together gives the target.

        Args.
            nums: List of integers.
            target: Number to find the two indices that sum together gives this.

        Returns.
            list: List of two indices.
        """
        n = len(nums)
        mp: dict = {}

        ans:int = 0
        
        # Space complexity: O(n) / Time complexity: O(n).
        for i in range(n):
            ans = target - nums[i]
            if ans in mp.keys():
                return i, mp[ans]
            mp[nums[i]] = i


        return []
