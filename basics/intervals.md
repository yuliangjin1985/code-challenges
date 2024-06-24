# Interval problems

How to check if two intervals `[a,b]`, `[c,d]`overlap?

To overlap each other, both begin values should be small or equal to the other end values.

```python
a <= d and c <= b
```

Or an easier way to understand:

```python
not (c > b or a > d)
```

Merge Intervals
Insert Interfal
Meeting rooms, Meeting rooms II, Meeting rooms III
Interval List Intersections

## 56 Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

>To start from the left, it's better to sort by `start` of intervals, this way always the left most was added to the final list, and there will be other intervals potentially be merged to the previous one only. If sorting based on the `end` of the intervals first, there could be later intervals merged with multiple previous final outputs. Meeting rooms II should also sort by `start` because should always satisfy the requirements by starting time.

This is different than [435 Non-overlaping Intervals](https://leetcode.com/problems/non-overlapping-intervals/description/), which is not merging but finding out how many non-overlaping ones, so can use `less is more` theory to solve the issue by sorting based on the `end` of the intervals (and on `start` decreasing when `end` is equal). Also for [452 Minimum Number of Arrows To Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/), we also can use `later is better` to burst more balloons.

```python
class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort(key = lambda x:x[0])
        ret, pre = [A[0]], A[0]
        for i in range(1, len(A)):
            l, r = A[i]
            if l <= pre[1]:
                ret[-1] = [min(l, pre[0]), max(r, pre[1])]
            else:
                ret.append(A[i])
            pre = ret[-1]
        return ret
```

## 57 Insert interval

You are given an array of non-overlapping intervals intervals where `intervals[i] = [starti, endi]` represent the `start` and the `end` of the `ith` interval and intervals is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

```python
class Solution:
    def insert(self, A: List[List[int]], b: List[int]) -> List[List[int]]:
        l, r = b
        left, right = [], []
        for i in A:
            if i[1] < l:
                left.append(i)
            elif i[0] > r:
                right.append(i)
            else:
                l = min(i[0], l)
                r = max(i[1], r)
        return left + [[l,r]] + right
```

## Interval List Intersections

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        la, lb = len(A), len(B)
        i, j = 0, 0
        out = []
        while i < la and j < lb:
            al, ar = A[i]
            bl, br = B[j]
            if ar >= bl and br >= al:
                out.append([max(al, bl), min(ar, br)])
            if ar <= br:
                i += 1
            else:
                j += 1

        return out
```

## Meeting rooms

There is LC 252 to check if a person can attend all the meetings. LC 253 is to check how many meeting rooms are needed to satisfy all the meetings. Both of these two we need to sort by the starting time, because it's natural we always check how the current earliest meeting can be attened or satisfied. For LC 2402 Meeting rooms III, because of prioritizing empty rooms with lowest id, we need to maintain two min heaps: empty_room and current used min heap, and always when processing one meeting, check the current used min heap and pop all the released rooms to empty rooms. 

## 