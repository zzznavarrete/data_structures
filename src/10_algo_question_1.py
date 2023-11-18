"""
Interview question:
- Given 2 different python lists, program an algorithm to identify if there is a repeated number.

Answer:
- There are 2 ways of answer this question, a O(n^2) and O(n).
The O(n^2) solution implies to do two for loops, one inside of another to iterate each position over the entire other list and check.

The O(n) solution implies to create a dictionary of the first list and then check (because checking a dictionary is O(n)) if in the other list is any existent key.

"""

# O(n^2) - un-efficient way
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


# O(n) - efficient method
def item_in_common_efficient(list1: list, list2: list) -> bool:
    """ Returns a boolean flag to indicate if there are repeated elements in 2 different lists.

    Args:
        list1 (list): _description_
        list2 (list): _description_

    Returns:
        bool: _description_
    """
    my_dict: dict = {}
    for i in list1:
        my_dict[i] = True


    for j in list2:
        if j in my_dict:
            return True

    return False





if __name__ == "__main__":
    list1, list2 = [1,2,3], [4,5,1]
    print(item_in_common(list1, list2))
    
    print("*"*20)

    print(item_in_common_efficient(list1, list2))


