"""
[9, 5, 3, 1, 6, 3] , 2

Expected
[9, 5, 3, 6, 6]
"""


def maxNumbersInWindow(nums:list, window:int) -> list:
    """
    Returns a list of max numbers given a moving window of 'window' size of elements.
    i.e: input (list and window) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 3 -> result = [3, 4, 5, 6, 7, 8, 9, 10].
    """

    # Border cases handling 
    if not nums or window < 2:
        return []
    
    if window > len(nums):
        return max(nums)
    
    # Initializing the pointers
    left, right = 0, window

    # Initializing the result variable
    result:list = []

    while right <= len(nums):
        numWindow:list = nums[left:right]
        result.append(max(numWindow))
        left += 1
        right += 1


    return result 


def optimizedMaxNumbersInWindow(nums:list, window:int) -> list:
    """
    Returns a list of max numbers given a moving window of 'window' size of elements.
    i.e: input (list and window) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 3 -> result = [3, 4, 5, 6, 7, 8, 9, 10].
    """
    from collections import deque

    # Border cases handling 
    if not nums or window < 2:
        return []
    
    if window > len(nums):
        return max(nums)

    # Initializing the data structure
    queue:deque = deque()
    result:list = []
    
    for i, n in enumerate(nums):
        while queue and nums[queue[-1]] < n:
            queue.pop()
        
        queue.append(i)
        if queue[0] == i - window:
            queue.popleft()
        if i >= window - 1:
            result.append(nums[queue[0]])

    return result 





if __name__ == "__main__":
    nums:list = [9, 5, 3, 1, 6, 3]
    w: int = 2

    print(maxNumbersInWindow(nums, w))
    print(optimizedMaxNumbersInWindow(nums, w))