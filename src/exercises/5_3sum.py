"""
Given an integer array nums, return all the triplets: 
    - [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

class Solution:

    def threeSum(self, nums: list) -> list:
        dict_nums:dict = {} #nums.copy()
        result_:list = []

        for index, value in enumerate(nums):
            if value in dict_nums:
                dict_nums[value].append(index)
            else:
                dict_nums[value] = [index]
        
        
        for idx, i in enumerate(nums):
            dyn_dict = dict_nums.copy()
            

            del dyn_dict[i][dyn_dict[i].index(idx)]

            if len(dyn_dict[i]) == 0:
                    del dyn_dict[i]

            
            for jdx, j in enumerate(nums[idx+1:]):
                
                nums_j_index:int = (idx+1)+jdx
                del dyn_dict[j][dyn_dict[j].index(nums_j_index)]

                if len(dyn_dict[j]) == 0:
                    del dyn_dict[j]

                k:int = i + j + 0
                if k*-1 in dyn_dict.keys():
                    result_.append([i, j, k*-1])
                else:
                    continue
                    
            return result_
                            
       
    def threeSum_SOLVED(self, nums: list) -> list:
        res = set()
        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res



if __name__ == "__main__":
    #input_:list = [-1,0,1,2,-1,-4] # should return [[-1,-1,2],[-1,0,1]]\
    input_ =[-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(input_))
    print(sol.threeSum_SOLVED(input_))
