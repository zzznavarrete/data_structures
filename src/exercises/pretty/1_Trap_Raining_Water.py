"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
"""

class Solution:
    def trap(self, height: list) -> int:
        # 1.- Check for border cases
        if not height: return 0

        # 2.- Write the actual algorithm
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res:int = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]

            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]


        return res
    


if __name__ == "__main__":
    sol = Solution()
    height:list = [0,1,0,2,1,0,1,3,2,1,2,1]

    print(sol.trap(height=height))
