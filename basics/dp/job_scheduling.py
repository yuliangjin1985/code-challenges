import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda a:a[1])
        dp = [[0,0]]
        for job in jobs:
            s, e, p = job
            i = bisect.bisect(dp, [s+1]) - 1 # Why s+1? Because we need to find the first element that is greater than s, so we need to find the first element that is greater than s+1
            print(f'i: {i}, s: {s}, {dp}, {job}')
            if dp[i][1] + p > dp[-1][1]: # Always the last element in dp is with the current max profit, it's greedy because if a later ended job would not be able to produce a bigger profit, then it will not be added to the dp.
                dp.append([e, dp[i][1] + p])
        print(dp)
        return dp[-1][1]
    
if __name__ == "__main__":
    startTime = [1,2,3,3,1]
    endTime = [3,4,5,6,7]
    profit = [50,10,40,70,130]
    solution = Solution()
    print(solution.jobScheduling(startTime, endTime, profit))
    # print(bisect.bisect([1,2,3,3,5,6,7,8,9], 40))
    # print(bisect.bisect([1,2,3,3,5,6,7,8,9], 1))
    # print(bisect.bisect([1,2,3,3,5,6,7,8,9], 3))
    # print(bisect.bisect([[0,0], [3,50]], [0]))
    # print(bisect.bisect([[0,0], [3,50]], [1]))
    # print(bisect.bisect([[0,0], [3,50]], [2]))
    # print(bisect.bisect([[0,0], [3,50]], [3]))
    # print(bisect.bisect([[0,0], [3,50]], [4]))
    print(bisect.bisect([[0,0], [3,50]], [3])) # Result is 1
    print(bisect.bisect([[0,0], [3,50]], [3,0])) # Result is 1
    print(bisect.bisect([[0,0], [3,50]], [3,50])) # Result is 2
    print(bisect.bisect([[0,0], [3,50]], [3,51])) # Result is 2

    print(bisect.bisect([[1, 10], [3, 20], [5, 30]], [4]))
    print(bisect.bisect([[1, 10], [3, 20], [5, 30]], [5]))