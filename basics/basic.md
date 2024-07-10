# Basic questions

[15 3Sum](https://leetcode.com/problems/3sum/)

[26 Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

[36 Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)

[37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/description/)

[44 Wildcard Matching](https://leetcode.com/problems/wildcard-matching/description/)

[51 N Queens](https://leetcode.com/problems/n-queens/description/)

[82 Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

[92 Reverse Linked II](https://leetcode.com/problems/reverse-linked-list-ii/description/)

[127 Word Ladder](https://leetcode.com/problems/word-ladder/description/)

[139 Word Breaker](https://leetcode.com/problems/word-break/)

[206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

[210 Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

[212. Word Search II](https://leetcode.com/problems/word-search-ii/description/)

[230 Kth smallest in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

[253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

[333 Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/description/)

[340 Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)

[392 Is Subsequence](https://leetcode.com/problems/is-subsequence/description/)

[437 Path Sum III](https://leetcode.com/problems/path-sum-iii/description/)

[449 Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/description/)

[545 Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/description/)

[680 Valid Polindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)

[772 Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/description/)

[787 Cheapest Flights within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

[870 Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/description/)

[1057 Campus Bikes](https://leetcode.com/problems/campus-bikes/description/)

[1229 Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/description/)

[1245 Tree Diameter](https://leetcode.com/problems/tree-diameter/description/)

[1647 Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/)

[1905 Count Sub Islands](https://leetcode.com/problems/count-sub-islands/description/)

[1971 Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

[2340 Minimus Adjacent Swaps to Make a Valid Array](https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/)

[2402 Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

## Normal solutions

1. Use set instead of list to check if an element is seen before. Like in bfs, dfs, enumeration and permutation, backtracking, etc. 

## Valid Sudoku

Use the list comprehension and flatten method `sum` in python.

```python
def isValidSudoku(self, board):
        # list comprehension
        data = [[(i,v),(v,j),(i//3,j//3,v)] for i, row in enumerate(board)
            for j, v in enumerate(row) if v != '.']
        # flatten the list of lists
        tuples = sum(data, [])
        return len(tuples) == len(set(tuples))

# Or a better way of using list comprehension:

def isValidSudoku(self, board):
    tuples = [
        t 
        for i, row in enumerate(board) 
        for j, n in enumerate(row) if n != '.' 
        for t in ((i, n), (n, j), (i // 3, j // 3, n))
    ]
    return len(tuples) == len(set(tuples))

```

## 15 3Sum

There is a requirement that the result must not contain duplicate triplets, so need to skip any possible duplicates. For the first element, we have to skip the duplicate this way: `if i > 0 and A[i] == A[i-1]: continue`, for the second and the third: `while l < r and A[l] == A[l+1]: l += 1` and `while l < r and A[r] == A[r-1]: r -= 1`.

```python
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        n = len(A)
        out = []
        for i in range(n-2):
            if i > 0 and A[i] == A[i-1]: continue
            l, r = i +1, n-1
            while l < r:
                if A[i] + A[l] + A[r] == 0:
                    out.append([A[i], A[l], A[r]])
                    while l < r and A[l] == A[l+1]: l += 1
                    while l < r and A[r] == A[r-1]: r -= 1
                    l += 1
                    r -= 1
                elif A[i] + A[l] + A[r] < 0:
                    l += 1
                else:
                    r -= 1
        
        return out
```

## 206 Reverse Linked List

One pass should revers the original list. Initial `prev` is set to be None.

## 92 Reverse Linked List II

Keep records of virtual head, first tail, sub head, sub tail, second head. 

## 1905 Count Sub Islands

First step, for every island in B which is not in A, change all the connected islands to 0. Then all the 1s in B will also be 1s in A, and count how many islands are there after the first step, using DFS.

## Calculations

|--|--|
|The integer division should truncate toward zero.|`return a//b+1 if a//b<0 and a%b !=0 else a//b`|
