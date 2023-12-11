"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
class Solution:
    def groupAnagrams(self, strs:str) -> list:
        strs_sort = ["".join(sorted(x)) for x in strs]

        map:dict = {}

        for i, word in enumerate(strs_sort):
            if word not in map.keys():
                map[word] = [strs[i]]
            else:
                map[word].extend([strs[i]])


        res_ = [value for key,value in map.items()]
        return res_


if __name__ == "__main__":
    sol = Solution()
    strs:list = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs = strs))


# Runtime complexity: O(n * (n log n)),
# Space complexity: O(m * n). As for the space complexity, you’re storing each string in a dictionary.  m: number of string, n: the maximum length of the strings.

