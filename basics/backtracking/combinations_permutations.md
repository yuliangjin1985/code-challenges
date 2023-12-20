# Combinations and Permutations

Think about these questions when facing similar problems.

1. Should it be Combination or Permutation problem?

2. Are original numbers unique or not?

3. Can the same element only be used more than once?

4. And always, there should be no duplicates from the results in any case.

How to remove duplicate? Like from the recursion perspective, each level should add the same element only once, so need to sort the nums first, and in each iteration, pass the level number.

## Combinations

Both problems can be resolved using backtracking. For combination, `[1,2,3]` and `[1,3,2]` are the same, so to avoid duplicates, need to explore the values based on a constant order (like increasing) and not add smaller numbers after bigger ones, like adding number `2` after `3`, because we know we will always have opportunity to add `3` after `2`.

And need to stop early if current combination would not possibly make a valid one, e.g: for combination sum, the current value is already bigger than target value.

```python
   for i in range(idx, len(nums)):
       # Because the same number can be used more than once, so need to recursively explore on next level starting with the same index i. 
       helper(i, temp + [nums[i]], cur + nums[i])
```

```python
   # Iterate starting with index `idx`, not indexes before that, meaning will not add smaller numbers before `idx`.
   for i in range(idx, len(nums)):
       # For the same level of iteration, same number can only be added once, otherwise there will be duplicates. e.g., `[1,1,1,1,3,4]`, when `idx = 0`, will skip the second, third, forth `1` on this level.
       if (i > idx and nums[i] == nums[i-1]):
           continue
       # added nums[i], recursively explore from index `i+1`
       helper(i + 1, temp + [nums[i]], cur + nums[i])
```

### 39 Combination Sum 1

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

```python
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        out = []
        def helper(idx, temp, cur):
            if cur == target:
                out.append(temp)
                return
            if cur > target:
                return
            for i in range(idx, len(nums)):
                helper(i, temp + [nums[i]], cur + nums[i]) # Because the same number can be used more than once, so need to recursively explore on next level starting with the same index i. 

        helper(0, [], 0)
            
        return out
```

### 40 Combination Sum 2

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

```python
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        def helper(idx, temp, cur):# Starts with idx, and now nums[idx] is not in temp yet
            if cur > target:
                return
            if cur == target:
                out.append(list(temp))
                return
            # Add next value recursively, so for the same number in this level, only add it once.
            for i in range(idx, len(nums)):
                if (i > idx and nums[i] == nums[i-1]):
                    continue
                temp.append(nums[i]) # Using mutable list, so need explicit reversion after the recursive call
                helper(i + 1, temp, cur + nums[i]) # The same number can only used once
                temp.pop()
        
        helper(0, [], 0)
        return out
```

Or can create a new list instance in each recursion, so no need to explicitly reverse the state after one recursion.

```python
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        def helper(idx, temp, cur):#Starts with idx, and now nums[idx] is not in temp yet
            if cur > target:
                return
            if cur == target:
                out.append(list(temp))
                return
            #Add next value recursively, so for the same number in this level, only add it once.
            for i in range(idx, len(nums)):
                if (i > idx and nums[i] == nums[i-1]):
                    continue
                helper(i + 1, temp + [nums[i]], cur + nums[i])
        
        helper(0, [], 0)
        return out
 ```

### 216 Combination Sum 3

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

>Only numbers 1 through 9 are used.
>Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [ i for i in range(1,10)]
        out = []
        def helper(idx, temp, cnt, sum): # current sum of cnt numbers
            if sum == n and cnt == k:
                out.append(list(temp))
                return
            if sum > n or cnt > k: # Finish early with invalid combinations
                return
            for i in range(idx, 9):
                helper(i+1, temp + [nums[i]], cnt+1, sum+nums[i])
        helper(0, [], 0, 0)
        return out
```

## 377 Combination Sum 4

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        def helper(idx, temp, cur):
            nonlocal cnt
            if cur == target:
                cnt += 1
                return
            if cur > target:
                return
            for i in range(idx, len(nums)):
                helper(idx, temp + [nums[i]], cur + nums[i])
        helper(0, [], 0)
        return cnt
```

Above code exceeded the time limit for case `nums=[4,2,1]` and `target=32`. This is bad, because the time complexity of above solution is `O(N^T)`, (Big O of N to the power of T), T is the target value divided by the smallest number in nums.

Another solution is using dynamic programming like the coin change 2. The time complexity will be reduced signifitely. The time complexity of this solution is `O(target*N)`. (Big O of target times n).

The difference with coin chagne 2 is, `[1,1,2]`, `[1,2,1]`, `[2,1,1]` are counted as different combinations. So the outer loop should be `range(1,target+1)` instead of `nums` which is `coins` in coin change 2.

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0 for _ in range(target)]
        for t in range(1,target+1):
            for num in nums:
                if t < num:
                    continue
                dp[t] += dp[t-num]
        return dp[target]
```

## Permutations
