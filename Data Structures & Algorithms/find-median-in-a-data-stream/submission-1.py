class MedianFinder:

    def __init__(self):
        self.left= [] # top of stack is closest to median
        self.right=[]
        self.even = True # if even, add to right.
        # so lengths either (n,n) or (n,n+1), never (n+1,n)

    def addNum(self, num: int) -> None:
        # add to right heap if:
            # even & num>= right[0]
            # odd & num>right[0]
        if (not self.right) or num>self.right[0] or (self.even and num == self.right[0]):
            if self.even: #(n,n) => (n,n+1)
                heapq.heappush(self.right,num)
            else: # (n,n+1) => (n,n+2) => (n+1,n+1)
                temp = heapq.heappushpop(self.right,num)
                heapq.heappush(self.left,-temp)
        else:
            if self.even: # (n,n) => (n+1,n) => (n,n+1)
                temp = -heapq.heappushpop(self.left,-num)
                heapq.heappush(self.right,temp)
            else: # (n,n+1) => (n+1,n+1)
                heapq.heappush(self.left,-num)
        self.even = not self.even

    def findMedian(self) -> float:
        if self.even:
            return (self.right[0]-self.left[0])/2
        else:
            return self.right[0]
        