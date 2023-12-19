
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Border case, len(height) <= 1
        if len(height) <= 1:
            return 0
        
        left, right = 0, len(height) - 1
        cur_max:int = 0
        while left < right:
            cur_max = max(cur_max, min(height[left], height[right]) * (right - left))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return cur_max
            
        
        