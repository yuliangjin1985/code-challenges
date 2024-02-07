# Basic questions

[15 3Sum](https://leetcode.com/problems/3sum/)

[26 Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

[37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/description/)

[44 Wildcard Matching](https://leetcode.com/problems/wildcard-matching/description/)

[51 N Queens](https://leetcode.com/problems/n-queens/description/)

[82 Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

[92 Reverse Linked II](https://leetcode.com/problems/reverse-linked-list-ii/description/)

[206 Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

[212. Word Search II](https://leetcode.com/problems/word-search-ii/description/)

[230 Kth smallest in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

[253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

[392 Is Subsequence](https://leetcode.com/problems/is-subsequence/description/)

[449 Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/description/)

[680 Valid Polindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)

[772 Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/description/)

[1229 Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/description/)

[1245 Tree Diameter](https://leetcode.com/problems/tree-diameter/description/)

[1905 Count Sub Islands](https://leetcode.com/problems/count-sub-islands/description/)

[2402 Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

## Normal solutions

1. Use set instead of list to check if an element is seen before. Like in bfs, dfs, enumeration and permutation, backtracking, etc. 

## 206 Reverse Linked List

One pass should revers the original list. Initial `prev` is set to be None.

## 92 Reverse Linked List II

Keep records of virtual head, first tail, sub head, sub tail, second head. 

## 1905 Count Sub Islands

First step, for every island in B which is not in A, change all the connected islands to 0. Then all the 1s in B will also be 1s in A, and count how many islands are there after the first step, using DFS.
