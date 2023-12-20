"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


"""

class Solution:
    def isValid(self, s: str) -> bool:
        opposite_open: dict = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        open_queue: list = []
        close_queue: list = []

        for char in list(s):

            if char in ["[", "{", "("]:  # if is opening char
                open_queue.append(char)
            elif char in ["]", "}", ")"]:
                if len(open_queue) > 0:
                    if opposite_open[open_queue[-1]] != char:
                        return False
                    else:
                        open_queue.pop()
                else:  # Border case: if is closing without having anything opened
                    return False
            else:  # Border case: bad input string
                return False
        
        if len(open_queue) > 0:
            return False
        
        return True
