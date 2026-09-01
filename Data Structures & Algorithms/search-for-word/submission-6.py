class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def neighbors(i,j, word_i, visited):
            if board[i][j] != word[word_i]:
                return False
            if word_i == len(word)-1:
                return True
            # print(i,j,board[i][j],word_i,visited)
            
            # up:
            if i-1>=0 and (i-1,j) not in visited and neighbors(i-1,j,word_i+1,visited+[(i,j)]):
                return True
            # down:
            if i+1<len(board) and (i+1,j) not in visited and neighbors(i+1,j,word_i+1,visited+[(i,j)]):
                return True
            # left:
            if j-1>=0 and (i,j-1) not in visited and neighbors(i,j-1,word_i+1,visited+[(i,j)]):
                return True
            # right:
            if j+1<len(board[i]) and (i,j+1) not in visited and neighbors(i,j+1,word_i+1,visited+[(i,j)]):
                return True
            return False
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if neighbors(i,j,0,[]):
                    return True
        return False
                    



