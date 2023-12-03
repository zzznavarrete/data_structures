
class Solution:


    def compareVersion(self, version1: str, version2: str) -> int:
        
        # Border case: If any or both of the lists are empty
        if len(version1) == 0 or len(version2) == 0:
            return 0
        
        version1_list:list = version1.split('.')
        version2_list:list = version2.split('.')

        # Border case: If there are characters that are not numbers, must be clean
        valid_chars:list = [str(x) for x in range(0,9+1)]
        valid_chars.append('.')
        version1_list = [x for x in version1 if x in valid_chars]
        version2_list = [x for x in version2 if x in valid_chars]

        version1_list = [int(item) for item in ''.join(version1_list).split('.') if len(item) > 0 and item != '.']
        version2_list = [int(item) for item in ''.join(version2_list).split('.') if len(item) > 0 and item != '.']

        # Cleaning the zeros from right to left
        max_non_zero_index:int = 0
        for idx, num_ in enumerate(version1_list):
            if num_ != 0:
                max_non_zero_index = idx
        version1_list = version1_list[:max_non_zero_index+1]

        max_non_zero_index= 0
        for idx, num_ in enumerate(version2_list):
            if num_ != 0:
                max_non_zero_index = idx
        version2_list = version2_list[:max_non_zero_index+1]

        result_:int = 0


        for index, left_number in enumerate(version1_list):
            if len(version2_list) - 1 >= index:
                if left_number > version2_list[index]:
                    return 1
                elif left_number < version2_list[index]:
                    return -1

        if result_ == 0 and len(version2_list) > len(version1_list):
            return -1
        
        if result_ == 0 and len(version1_list) > len(version2_list):
            return 1

        return result_



if __name__ == '__main__':
    sol = Solution()

    version1:str = '4.9'
    version2:str = '4.5'
    print(sol.compareVersion(version1=version1, version2=version2))


"""

"7.5.2.4"
"7.5.3"
"""