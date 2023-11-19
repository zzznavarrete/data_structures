
def pointer_dict():
    
    dict_dummy1 = {'value': 11} 
    dict_dummy2 = dict_dummy1

    print(f"dict_dummy1['value'] = {dict_dummy1}")
    print(f"dict_dummy2['value'] = {dict_dummy2}")

    print(f'memory dict1: {id(dict_dummy1)}')
    print(f'memory dict1: {id(dict_dummy2)}')

    # Changing the dict2 value
    dict_dummy2['value'] = 22

    print('\n -- Post change -- ')

    print(f"dict_dummy1['value'] = {dict_dummy1}")
    print(f"dict_dummy2['value'] = {dict_dummy2}")

    print(f'memory dict1: {id(dict_dummy1)}')
    print(f'memory dict1: {id(dict_dummy2)}')


if __name__ == "__main__":
    pointer_dict()