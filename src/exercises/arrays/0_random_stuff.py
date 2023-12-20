
def getMinimumFruits(fruits):
    # Write your code here
    """
    Returns the minimum amount of fruits after the crush between each other.
    
    Args:
        fruits: list
    
    Returns:
        int: minimum possible number of fruits after the crushing.
    """
    dict_fruits:dict = {}
    for fruit in fruits:
        if fruit in dict_fruits:
            # the fruit is already counted
            dict_fruits[fruit] += 1
        else:
            # the fruit is new for the dictionary
            dict_fruits[fruit] = 1
    
    dict_fruits = dict(sorted(dict_fruits.items(), key=lambda item: item[1], reverse=True))
    
    iterator:iter = iter(dict_fruits.items())
    for fruit, times in iterator:
        updated_value = times 
        if times > 0:
            try:
                while(updated_value > 0):
                    next_key, next_value = next(iterator)
                    updated_value = updated_value - next_value
                    
                    dict_fruits[fruit] = updated_value
                    dict_fruits[next_key] = 0
            except StopIteration:
                print('there are no more elements in the dictionary of fruits')
    
    return sum(dict_fruits.values())
        



def calculate_review_score(review, prohibited_words):
    max_score = 0
    current_score = 0
    max_score_substring = ""

    for i in range(len(review)):
        for j in range(i + 1, len(review) + 1):
            substring = review[i:j].lower()  # Convertir a minúsculas para comparación sin distinción de mayúsculas/minúsculas
            if any(word in substring for word in prohibited_words):
                # La subcadena contiene una palabra prohibida, reiniciar puntuación
                current_score = 0
            else:
                # La subcadena no contiene palabras prohibidas, actualizar puntuación
                current_score = j - i
                if current_score > max_score:
                    max_score = current_score
                    max_score_substring = substring

    return max_score, max_score_substring

def findReviewScore(review, prohibited_words):
    iter_ = 0
    max_without_restart = 0
    for i in range(len(review)):
        iter_+=1
        word = review[0:i+iter_].lower()
        if any(subs in word for subs in prohibited_words):
            max_without_restart = iter_ - 1
            
            print(word)

        


    pass


if __name__ == "__main__":
    #print(getMinimumFruits([1,2,5,6,6]))
    
    review = 'GoodProductButScrapAfterWash'
    prohibitedWords = ['crap', 'odpro']
    #print(calculate_review_score(review, prohibitedWords))
    print(findReviewScore(review, prohibitedWords))