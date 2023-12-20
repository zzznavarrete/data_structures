class Solution:
    def maximumSubarraySum(self, nums: list, k: int) -> int:
        """
        Returns the sum of the max subarray in which none of the elements of the subarray are repeated and - 
        - are conform by k elements.
        """
        # Border case, if nums list is empty or k == 0
        if len(nums) == 0 or k == 0:
            return 0
        
        # Border case, array and k are equal
        if len(nums) == k:
            if len(set(nums)) == k:
                return sum(nums)
            else:
                return 0

        if len(nums) < k:
            return 0

        left, right = 0, k
        aux_pointer = 0

        result:list = []
        potential_subs:list = []
        
        max_sub:int = 0

        while right <= len(nums):
            if len(potential_subs) < k:
                if nums[aux_pointer] not in potential_subs:
                    potential_subs.append(nums[aux_pointer])
                    aux_pointer += 1
                else:
                    left = aux_pointer
                    right= left + k
                    aux_pointer = left 
                    potential_subs = []
            else:
                max_sub = max(max_sub, sum(potential_subs))
                left += 1
                right +=1
                aux_pointer = left
                potential_subs = []

        return max_sub




if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSubarraySum(nums=[1,5,4,2,9,9,9], k=3))
    print(sol.maximumSubarraySum(nums=[9,9,9,1,2,3], k=3))