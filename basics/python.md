## Basic usages
### sorting
```python
    #less is more
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            first, second = intervals[i]
            if first >= end:
                end = second
                count += 1
        return len(intervals) - count

```

```python
# intervals: List[List[int]], first sort based on the first element on assending order, if equal, then sort on second element by descending order
intervals.sort(key=lambda x: (x[0], -x[1]))
```
