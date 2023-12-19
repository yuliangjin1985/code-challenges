from typing import List

class Solution:

    # 46 Permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        visit = [0 for _ in range(0, len(nums))]
        def helper(nums, temp):
            if len(temp) == len(nums):
                out.append(list(temp))
            for i in range(len(nums)):
                if not visit[i]:
                    visit[i] = 1
                    temp.append(nums[i])
                    helper(nums, temp)
                    temp.pop()
                    visit[i] = 0
        helper(nums, [])
        return out

    # 47 Permutations II, having duplicates in the input array
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        N = len(nums)
        visited = [0] * N
        nums.sort()
        def helper(nums, temp):
            if len(temp) == N:
                out.append(list(temp))
            for i in range(N):
                # Use this visited array to avoid duplicates
                if (i > 0 and nums[i] == nums[i-1] and not visited[i-1]) or visited[i]:
                    continue
                # Variable visited and temp are mutable, so need to update properly in backtracking fashion 
                visited[i] = 1
                temp.append(nums[i])
                helper(nums, temp)
                temp.pop()
                visited[i] = 0
        helper(nums, [])
        return out
    
    # 322 Coin Change, using DP, outter loop is amount, inner loop is coins
    def coinChange(self, coins: List[int], n: int) -> int:
        cnt = [float('inf') for _ in range(0, n+1)]
        cnt[0]=0
        for i in range(1, n +1):
            for coin in coins:
                if coin <= i:
                    cnt[i] = min(cnt[i], cnt[i-coin]+1)
        if cnt[n] == float('inf'):
            return -1
        return cnt[n]
    
    # 518 Coin Change 2, basically it's a combination problem, so outter loop is coins, inner loop is amount
    def change(self, n: int, coins: List[int]) -> int:
        cnt = [0 for _ in range(0, n + 1)]
        cnt[0] = 1
        for coin in coins:
            for i in range(1, n+1):
                if coin <= i:
                    cnt[i] += cnt[i-coin]
        return cnt[n]
        
    
  