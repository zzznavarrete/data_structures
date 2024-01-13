
def getRepeatedElements(s:str, k:int) -> set:
    if not s or len(s) < 10:
        return set([])
    
    # HashMap
    hashMp:dict = {}

    # Sliding window
    left, right = 0, k

    # Result var to post/process after
    sequences:list = []

    # Loop to iterate over
    while right < len(s):
        sequence:str = s[left:right]
        if sequence in hashMp.keys():
            hashMp[sequence] += 1
            sequences.append(sequence)
        else:
            hashMp[sequence] = 1
        
        left += 1
        right += 1


    return set(sequences)


if __name__ == "__main__":
    DNA_CODE:str = "AAAAAACCCCCCCAAAAAAAACCCCCCCTG"
    k:int = 10

    print(getRepeatedElements(DNA_CODE, k))