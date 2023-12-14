"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:
    """
    As the while loop traverses the array once, the time complexity is O(N), making this algorithm linear in terms of -
    - time complexity. The space complexity is O(1) because the algorithm uses only a constant amount of additional - 
    - space   regardless of the input size.
    """
    def twoSum(self, numbers: list, target: int) -> list:
        """
        Desc.
        Returns an array of indexes +1 wich numbers of the input array, added together, sums an specific target

        Args.
        numbers:list = Array of integers.
        target:int = Integer which value will be obtained by the sum of two indexes of the other input.

        Returns.
        List of indexes +1 which added together returns given target.
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            ans = numbers[left] + numbers[right]
            if ans < target:
                left += 1
            elif ans > target:
                right -= 1
            else:
                return left + 1, right + 1

        return []



if __name__ == "__main__":
    sol = Solution()
    numbers:list = [2,7,11,15]
    target:int = 9

    print(sol.twoSum(numbers=numbers, target=target))
        
