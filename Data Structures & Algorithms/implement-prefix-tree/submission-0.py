class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.wordSet = set()

    def insert(self, word: str) -> None:
        curr_dict = self.trie
        self.wordSet.add(word)
        for char in word:
            if char not in curr_dict:
                curr_dict[char]={}
            curr_dict = curr_dict[char]

    def search(self, word: str) -> bool:
        return word in self.wordSet

    def startsWith(self, prefix: str) -> bool:
        curr_dict = self.trie
        for char in prefix:
            if char in curr_dict:
                curr_dict = curr_dict[char]
            else:
                return False
        return True
        