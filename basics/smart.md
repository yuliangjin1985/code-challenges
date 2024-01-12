# Smart algorithms

## Examples

There are some simple but very smart ideas when dealing with these issues, which should be revisited and reused always.

### 128. Longest Consecutive Sequence

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
