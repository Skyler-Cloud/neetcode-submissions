class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        curr_dict = self.words
        for char in word:
            if char not in curr_dict:
                curr_dict[char] = {}
            curr_dict = curr_dict[char]
        curr_dict['#']=True

    def search(self, word: str) -> bool:
        def search_in_dict(curr_dict, i):
            while i<len(word):
                char = word[i]
                if char in curr_dict:
                    curr_dict = curr_dict[char]
                    i+=1
                    continue
                if char == '.':
                    for sub_char, sub_dict in curr_dict.items():
                        if sub_char != '#' and search_in_dict(sub_dict,i+1):
                            return True
                return False
            return '#' in curr_dict
        return search_in_dict(self.words,0)
            
        
