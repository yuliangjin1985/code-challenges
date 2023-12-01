from heapq import *
class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []

    #To add a new number, we only allow the max heap (the smaller half numbers) has one more number, but the new number has to be pushed to the 
    # min heap, and pop the smallest number, then it will be pushed to the max heap, and now it's not necessarily be the biggest one in the smaller numbers.
    # min_heap holds the bigger half of numbers, max_heap holds the smaller half of the numbers.
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num)) #Push the new number to the bigger half numbers and get the smallest one to push to smaller half numbers.
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return (self.max_heap[0] - self.min_heap[0]) / 2

if __name__ == "__main__":
    finder = MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    print(finder.findMedian())
    finder.addNum(3)
    print(finder.findMedian())
  