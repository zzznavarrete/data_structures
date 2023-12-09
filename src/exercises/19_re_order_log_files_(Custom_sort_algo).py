"""

"""

class Solution:
    def reorderLogFiles(self, logs:str) -> str:
        """
        Returns a sorted logs list within the given rules.
        """
        def custom_sort_alg(log:str):
            # Splits the left and right side of the log content for further usage.
            left_, right_ = log.split(' ', 1)

            if right_[0].isalpha():
                # then, it is a letter-type log.
                return (0, right_, left_) # Priority of sort: Letter type, Content, Key.
            else:
                return(1,) # Priority: Numerical logs has lower priority then letter-type.
            
        # Return the sorted log list with the custom algorithm implementation.
        return sorted(logs, key=custom_sort_alg)


if __name__ == "__main__":
    solution_ = Solution()
    logs_list:list = ["dig1 8 1 5 1","let1 bart can","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(solution_.reorderLogFiles(logs=logs_list))


