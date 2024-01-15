def is_happy_number(n) -> bool:
    """
    Returns a boolean flag to indicates if 'n' input number is a 'happy number'.
    """

    if not n:
        return False


    slowPointer = n
    fastPointer = sumSquareDigits(n)

    while fastPointer != 1 and slowPointer != fastPointer:
        slowPointer = sumSquareDigits(slowPointer)
        fastPointer = sumSquareDigits(sumSquareDigits(fastPointer))

    if fastPointer == 1:
        return True
    else: return False

def sumSquareDigits(num:int) -> int:
    if not num:
        return 0

    return sum([int(x)**2 for x in str(num)])
