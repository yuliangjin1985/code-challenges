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

## 33 Search in Rotated Sorted Array

Let's say `nums` looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust `nums` to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust `nums` to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at. And the adjustment is done by comparing both the target and the actual element against nums[0].

There are three key numbers, the pivot, the mid, and the target. If mid and target are on the same side of pivot, then the virtual mid value is set to be the current value. If mid and target are on the two sides of the pivot, then compare the target with pivot to set virtual mid to be -inf or inf, and last step is compare the virtual mid with target.

[12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], the pivot is 12, mid is at index 9 (0 + (19-0)//2), having 1 now. Numbers of 0, 2, ...11 are on one side of pivot, and 12,13,14,...19 are on the other side of pivot.

```python
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # num here is the virtual mid, after this step, we can assume the initial array is virtually sorted.
            num = nums[mid]
            # If nums[mid] and target are "on the same side" of nums[0], we just take nums[mid].
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            else:
                # If target is smaller than the first node, the target should be in the second half, so set the virtual mid to be '-inf', intending for the first half to be '-inf', otherwise set the virtual mid to be 'inf', intending for the second half to be 'inf'.
                num = float('-inf') if target < nums[0] else float('inf')

            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid - 1
            else:
                return mid
        return -1
```

Or a similier version:

For [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], to search 0.

p is 12

l,r=0,19
mid=9,
m=A[mid]=1
p=12,m=1,t=0 => m and t are all smaller than p, so they are on the same side of p, so m stays as 1.
m is greater or equal than the t, so we change r to be mid.

l,r=0,9
mid=4
m=A[4]=16
p=12,m=16,t=0 => m and t are on two sides of p, and t < p => m=float('-inf'), current virtual array is [-inf,-inf,-inf,-inf,-inf,17,18,19,0,1], because m (-inf) is smaller than 0, so l is updated to 5 (mid+1)

l,r=5,9, [17,18,19,0,1]
mid=7 (5+(9-5)//2)
m=A[7]=19
p=12,m=19,t=0 => m and t are on two sides of p, and t < p => m will be set to -inf, current virtual array is [-inf,-inf,-inf,0,1], because m (-inf) is smaller than 0, so l is updated to 8 (mid+1).

l,r=8,9, [0,1]
mid=8 (8+(9-8)//0)
m=A[8]=0
p=12,m=0,t=0 => m and t are on the same side of p, => m will be kept as 0, current virtual array is [0,1], because m (0) is not smaller than 0, so r is updated to 8 (mid).

l,r=8,8, [0]
l is not smaller than r, so directly check if A[r] is target 0, and it is so the index 8 is found.

```python
    def search(self, A, t):
        l,r = 0,len(A)-1
        p = A[0]
        while l<r:
            mid = l + (r-l)//2
            m = A[mid]
            # m, t are on the same side of p or not
            if ((m<p)==(t<p)):
                m = A[mid]
            else:
                m = float('inf') if t >= p else float('-inf')
            if m < t:
                l = mid + 1
            else:
                r = mid
        
        return r if A[r] == t else -1
```

## 26 Remove duplicates from sorted list

```python
    def removeDuplicates(self, A: List[int]) -> int:
        nxt = 1
        for i in range(1,len(A)):
            if A[i] != A[nxt-1]:
                A[nxt] = A[i]
                nxt += 1
        return nxt
```

## 82 Remove duplicates from sorted list II

```python
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0,head)
        cur,pre = head, out
        while cur:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            # If there is no duplicate of cur node
            if pre.next == cur:
                pre = cur
                cur = cur.next
            # If there are duplicates of cur node, and not changing the pre node in this casse
            else:
                pre.next = cur.next
                cur = cur.next
        return out.next
```

## 772 Basic calculator III

The tricky part is the recursion when '(' is met, and the recursion should return the result inside the parentathis, and the index of the matching ')'. So after the recursion, say `1+(2+5)`, the recursion returns (7, 6), 6 is the index of ')'. So the recurssion completely processed `(2+5)`, everthing inside the parenthesis and including the right parenthesis.

```python
class Solution:
    def calculate(self, s: str) -> int:
        def calculate(j):
            num, oper, stack = 0, '+', []
            def process(num, oper):
                if oper == '+':
                    stack.append(num)
                elif oper == '-':
                    stack.append(-num)
                elif oper == '*':
                    stack.append(stack.pop()*num)
                else:
                    first = stack.pop(
                    stack.append(first//num + 1 if first//num < 0 and first % num != 0 else first//num)

            i = j
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] in "+-*/":
                    process(num, oper)
                    num, oper = 0, s[i]
                elif s[i] == '(':
                    num, i = calculate(i+1)
                    # Here we can't process now like bellow, and i is the index of the matching ')'.
                    # process(num, oper)
                    # num, oper = 0, '+'
                elif s[i] == ')':
                    process(num,oper)
                    out = (sum(stack), i)
                    return out
                i += 1
            process(num, oper)
            return (sum(stack), i)
        
        num, i = calculate(0)
        return num
```
