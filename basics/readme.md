# Blind 75 leetcode questions

## 128 Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example 1:**

>Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.  
**Example 2:**

>Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

**Constraints**:

$0 <= nums.length <= 10^5$

$-10^9 <= nums[i] <= 10^9$

### Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 0
        for num in nums:
            if num - 1 not in nums:
                next = num + 1
                while next in nums:
                    next += 1
                ret = max(ret, next - num)
        return ret
 
```

## 295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for `arr = [2,3,4]`, the median is 3.
For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within $10^5$ of the actual answer will be accepted.

```python

from heapq import *
class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []

    #To add a new number, we only allow the max heap has more one, but the new number has to be pushed to the 
    #min heap, and pop the biggest number, then it will be push to the max heap.
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return (self.max_heap[0] - self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
