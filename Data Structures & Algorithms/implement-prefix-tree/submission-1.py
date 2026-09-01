class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr_dict = self.trie
        for char in word:
            if char not in curr_dict:
                curr_dict[char]={}
            curr_dict = curr_dict[char]
        curr_dict['#']=True # if '#' is in the ending dict, we've reached the end of a word.

    def search(self, word: str) -> bool:
        curr_dict = self.trie
        for char in word:
            if char in curr_dict:
                curr_dict = curr_dict[char]
            else:
                return False
        return '#' in curr_dict

    def startsWith(self, prefix: str) -> bool:
        curr_dict = self.trie
        for char in prefix:
            if char in curr_dict:
                curr_dict = curr_dict[char]
            else:
                return False
        return True
        