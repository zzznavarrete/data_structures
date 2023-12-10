class Solution:
    """
    #Returns the length of the longest substring with unique characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) 
        persist_subs:str = ''

        # Iterates in O(n^2) complexity looking for substrings without any repeated characters.
        for i in range(n):
            dyn_sub:str = ''
            dyn_sub += str(s[i])
            for j in range(i+1, n):
                # It will iterate the sub_list in i+1 position storing the one-by-one the characters - 
                # - only if that character is not presented in the list, it is stored.
                # - In the other case (meaning, the character is in the dynamic list) the loop breaks.
                if str(s[j]) in dyn_sub:
                    break
                else:
                    dyn_sub += str(s[j])
            # If the dynamic list length is greater than the persisted list length, then it got replaced.
            if len(dyn_sub) > len(persist_subs):
                persist_subs = dyn_sub
        # Returns the length of the longest list found in the algorithm.
        return len(persist_subs)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring with unique characters.
        """
        n = len(s)
        # Variable that will store the current difference between the - 
        # - longest substr without repeat chars.
        ans: int = 0

        # Variable that will map the latest seen index (+1) of the iterated char.
        mp: dict = {}

        # Pointer that will stick the latest unseen char meanwhile the j pointer advances. 
        i:int = 0

        for j in range(n): # loop that will iterate the pointer j 
            if s[j] in mp: 
                # In case the current char is already mapped, then the pointer i -
                # - gets updated until the latest char s[j] position.
                i = max(mp[s[j]], i) 

            # Will store the max difference of pointers, meaning - 
            # - the max difference without repeat chars.
            ans = max(ans, j - i + 1) 

            # Updated the hash-map of the latest seen position of char s[j]
            mp[s[j]] = j + 1

        # Given that 'ans' only keep the max difference, it will return the length of the largest
        # - substring without repetition.
        return ans 



if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s='abcabcabc'))