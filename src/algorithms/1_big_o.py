

# O(n)
def print_items(n):
    """
    Example of a function that is Big O(n)
    It mean is linear according the number of the operations. 

    It is called 'Proportional'. 
    Proportional -> O(n).
    """
    for i in range(n):
        print(i)


# O(n^2)
def print_items_o_pow_2(n):
    """
    We have a loop inside of a loop. 
    Then, the notation triggers to: O(n^2).

    We have n*n times items worked out. 
    """
    for i in range(n):
        for j in range(n):
            print(i,j)



# O(1)
def print_items_o1(n):
    return print(n+n+n)



if __name__ == "__main__":
    #print_items(10)
    #print_items_o_pow_2(10)
    print_items_o1(2)
