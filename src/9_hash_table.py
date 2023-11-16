"""
Hash Tables
Hash tables are essential data structures designed to map elements with corresponding keys efficiently. 
The fundamental principle underlying hash tables involves the use of a hash function to convert a key into an address, 
facilitating the storage of associated data. This one-way conversion by the hash function is deterministic, ensuring consistent results for the same input.

Collision Handling
Hash tables encounter collisions when multiple key-value pairs map to the same address. Two commonly employed techniques for collision resolution are:

Separate Chaining:
This method involves creating a "parent" list at each address to manage multiple values that map to the same location.
Multiple values are encapsulated within a single list, streamlining access and storage.
Linear Probing:

Linear probing resolves collisions by iteratively searching for the next available address.
If the desired address is occupied, the algorithm traverses to the next available slot until an empty space is found for data storage.

Addressing Multiple Values
Linked Lists:
Implementing linked lists at each address allows for the accommodation of multiple values at the same location.
This approach enhances the flexibility of hash tables in handling collisions and organizing data.

By understanding and leveraging these collision resolution techniques, hash tables efficiently manage key-value pairs, ensuring data integrity and retrieval accuracy.
-----------------------------

Constructor building
-----------------
Ideally, I should always point to have a prime number of addresses. That's because a prime number icnrease the number of randomess in which the key values will -
be stored, so it reduce the collisions. 

Set
-----------------
The set function is going to use the hash method on the key to create the address, and also is going to create a key/value pair in a list, and then -
it will going to create a parent list that will comprehen the converted one in the indicated address. 



"""
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23 )  % len(self.data_map)
        return my_hash 
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])


if __name__ == "__main__":

    my_hash_table = HashTable()
    my_hash_table.set_item('bols', 1400)
    my_hash_table.set_item('bolsu', 1401)
    my_hash_table.set_item('lumber', 70)
    my_hash_table.print_table()
    