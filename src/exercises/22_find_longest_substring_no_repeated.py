class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring with unique characters.
        """
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
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s='abcabcabc'))