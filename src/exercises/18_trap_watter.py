
def trap( height):
    """
    :type height: List[int]
    :rtype: int
    """
    areas = 0
    max_l = max_r = 0
    l = 0
    r = len(height)-1
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                areas += max_l - height[l]
            l +=1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                areas += max_r - height[r]
            r -=1
    return areas

op1 = [4,2,3]
op2 = [0, 1, 0, 2, 1 , 0 , 1, 3 , 2 , 1 , 2, 1]

print(trap(height=op2))