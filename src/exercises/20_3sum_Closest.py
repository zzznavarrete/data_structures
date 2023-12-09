class Solution:

    def threeSumClosest(self, nums:list, target: int) -> int:
        """
        Return the sum of the 3 elements that sum together are the most close to a given target than any other combination.
        """
        nums.sort() # First, sort the input array so I can use the low/high pointers logic.
        diff: int = float('inf') # This is the temporary variable that I'm going to use for store the minor difference.

        # INIT: FOR LOOP
        for i, num in enumerate(nums):
            # Given that the array is sorted from smallest to largest, the following logic is feasible:
            low = i + 1 # Getting the 1st pointer, 1 element after my current position.
            high = len(nums) - 1 # Getting the 2nd pointer, the last element of the list.

            while low < high: # Doing the following while looping my entire remaining array
                sum_ = num + nums[low] + nums[high] # Performing the triplet sum
                
                if abs(target - sum_) < abs(diff): # If the current difference is lesser than the absolute diff of the target - sum_, store it 
                    diff = target - sum_
                
                if sum_ < target: # If my current triplet sum is greater than my target, then I need to move 1 element to the right in my left/low pointer
                    low += 1
                else: # In the other case, it means that my sum is greater than the target, so I need to move 1 element to the left of the right/high pointer
                    high -= 1 
                
            if diff == 0: # In case I found a difference that is equal to my result, then it means that I found the perfect triplet
                break

        # END: FOR LOOP.
        # Return the difference between target - diff, that is the result of the triplet which difference respect of the target is smaller among all the options.
        return target - diff 



if __name__ == "__main__":
    solution_ = Solution()
    #list_:list = [-1,2,1,-4] target_ = 1
    #list_:list = [1, 1, 1, 0] #t = -100
    list_= [4,0,5,-5,3,3,0,-4,-5]
    target_ = -2
    
    print(solution_.threeSumClosest(nums=list_, target=target_))

