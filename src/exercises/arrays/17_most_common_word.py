"""

"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Returns the most common word in a given paragraph without - 
        - taken into account the banned words.
        """
        paragraph = paragraph.lower()
        re_para:str = ''   
        special_banned:list = ['!', '?', '.', ';', ',', ]
        
        # Border case: In case the special characters are without blank space after
        for idx, word in enumerate(paragraph):
            if idx > 0:
                if last_word in special_banned and word != ' ':
                    re_para += (' ' + word)
                else:
                    re_para += word
            else:
                re_para += word
                
            last_word = word
            
        paragraph_filtered:list = re_para.split(' ')
        
        # Border case: In case the banned words has non-alphanumeric elements inside of them
        banned = [''.join(char for char in word if char.isalpha()) for word in banned]
        
        # Border case: In case the paragraph has non-alphanumeric elements inside of them
        paragraph_filtered =  [''.join(char for char in word if char.isalpha()) for word in paragraph_filtered]
        paragraph_filtered = [x for x in paragraph_filtered if not x in banned and x != '']
        
        # Border case: Handle in case the list is empty
        if len(paragraph_filtered) > 0:
            
            dict_counter:dict = {}
            
            # Counting all the repeated occurences
            for word in paragraph_filtered:
                if word not in dict_counter.keys():
                    dict_counter[word] = 1
                else:
                    dict_counter[word] += 1
            
            # Returning the key with greater value among the others, thus, the most common word
            return max(dict_counter, key=lambda k: dict_counter[k])
            
            
        else:
            return ""
        