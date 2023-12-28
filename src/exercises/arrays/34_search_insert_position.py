class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        # Aux variables
        middle:int = len(nums) // 2
        prev_state:int = 0
        counter = 0
        # Main loop to look up
        while not nums[middle] == target:
            counter +=1
            if counter > 10:
                break 

            print('middle = ', middle)
            print('nums[middle] == ', nums[middle])

            if target > nums[middle]:
                # bigger than the middle of the array
                if prev_state == 2:
                    middle += 1
                    break
                 
                middle += len(nums[middle:]) // 2
                prev_state = 1 

            elif target < nums[middle]:
                # lower than the middle of the array
                if prev_state == 1:
                    #middle -= 1
                    break 

                middle //= 2
                prev_state = 2

            
        return middle



if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert(nums=[1,3,5,6], target=2))