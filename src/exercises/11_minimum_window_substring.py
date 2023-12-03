"""
Input: s = "ADOBECODEBANC", t = "ABC"
>> "BANC"
"""
from collections import Counter


class Solution:

    def minWindow(self, s:str, t:str) -> str:

        

        # Border case: If 's' is greater than 't'
        if len(t) > len(s):
            return ""

        s_list: list = [x for x in s]
        t_list: list = [x for x in t]

        # Border case: If 's' is not in 't'
        flag_exist_s:bool = False
        nums_found: int = 0
        t_list_check:list = []
        for letter in s_list:
            if (letter in t_list) and (letter not in t_list_check):
                nums_found += 1
                t_list_check.append(t_list_check)

        flag_exist_s = nums_found >= len(t_list)
        
        if not flag_exist_s:
            return ""
        
        if s == t:
            return t

        # dynamic variables
        result_:list = []
        nums_found: int = 0
        
        # found substr results variable
        results_:list = []
        
        for index, letter in enumerate(s_list):
            nums_found = 0
            t_list_dyn = t_list.copy()
            if letter in t_list:
                nums_found += 1
                t_list_dyn.remove(letter)
                result_.append(letter)
                for next_letter in s_list[index+1:]:
                    if nums_found == len(t_list):
                        break
                    if (next_letter in t_list_dyn): 
                        t_list_dyn.remove(next_letter)
                        nums_found += 1
                    result_.append(next_letter)
                    

                if nums_found == len(t_list): results_.extend([result_])
                    
                result_ = []

        shortest_:int = 0
        shortest_index:int = 0


        for idx, result in enumerate(results_):
            if idx == 0:
                shortest_ = len(result)
                shortest_index = idx
            else:
                if len(result) < shortest_: 
                    shortest_ = len(result)
                    shortest_index = idx
        
        #print('final results = ', results_)
        if len(results_) == 0:
            return ""
        return "".join(results_[shortest_index])
    



    def optimized_minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        
        need, match, l, start, windowLen = Counter(t), 0, 0, 0, len(s) + 1
        
        for r, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                match += need[ch] == 0

            while match == len(need):
                if windowLen > r - l + 1:
                    start, windowLen = l, r - l + 1
                
                removeCh = s[l]
                l += 1 
                if removeCh in need:
                    match -= need[removeCh] == 0
                    need[removeCh] += 1

        return s[start:start + windowLen] if windowLen <= len(s) else ''

if __name__ == "__main__":
    sol = Solution()

    s:str = 'bbaa'
    t:str = 'aba'

    print(sol.minWindow(s=s, t=t))
    print(sol.optimized_minWindow(s=s, t=t))


        