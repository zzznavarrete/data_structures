"""
8. String to Integer (atoi)
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution:

    def clamp_to_32_bit_signed_integer(self, value):
        # Convert the string to an integer
        try:
            integer_value = int(value)
        except ValueError:
            # Handle the case where the conversion fails
            print(f"Error: Unable to convert '{value}' to an integer.")
            return None

        # Clamp the integer to the 32-bit signed integer range
        clamped_value = max(min(integer_value, 2**31 - 1), -2**31)

        return clamped_value

    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        valid_chars:list = [str(x) for x in range(0,10)]
        if 0 <= len(s) <= 200:
            s = s.strip()
            s_list = [x for x in s]


            if s_list[0].__contains__("-"): # negative
                #s_list = [x for x in s_list if x in valid_chars]

                s_list_formated:list = []
                for cur_char in s_list[1:]:
                    if cur_char in valid_chars:
                        s_list_formated.extend([cur_char])
                    else: 
                        break
                
                if len(s_list_formated) > 0:
                    s = "".join(s_list_formated)
                    
                    s = int(s)
                    s = s * -1
                else:
                    return 0
                
            elif s_list[0].__contains__("+") or s_list[0] in valid_chars: # positive

                if s_list[0].__contains__("+"):
                    s_list = s_list[1:]
                
                s_list_formated:list = []
                for cur_char in s_list[0:]:
                    if cur_char in valid_chars:
                        s_list_formated.extend([cur_char])
                    else: 
                        break
                
                if len(s_list_formated) > 0:

                    s = "".join(s_list_formated)
                    s = int(s)
                else:
                    return 0
            else: return 0

            return self.clamp_to_32_bit_signed_integer(s)

        else:
            return 0

        


if __name__ == "__main__":
    sol = Solution()
    s = "-3.14159"
    #s="-91283472332"
    #s = "+-12"
    print(sol.myAtoi(s=s))
