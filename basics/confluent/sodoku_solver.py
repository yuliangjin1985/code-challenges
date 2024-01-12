class Solution:
    def solveSudoku(self, b: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols, sub = set(), set(), set()

        for i in range(9):
            for j in range(9):
                if b[i][j] != '.':
                    cur = int(b[i][j])
                    rows.add((i,cur))
                    cols.add((j,cur))
                    sub.add((i // 3,j // 3,cur))
        
        def is_valid(i,j,k):
            if ((i,k)) in rows or ((j,k)) in cols or ((i//3,j//3,k)) in sub:
                # print("invalid")
                return False

            # print(f'is valid: i {i}, j {j}, k: {k}')
            return True
        
        def update_set(i,j,k):
            rows.add((i,k))
            cols.add((j,k))
            sub.add((i//3,j//3,k))

        def reset_set(i,j,k):
            # print(f'Removing {i}, {j}, {k}')
            rows.remove((i,k))
            cols.remove((j,k))
            sub.remove((i//3,j//3,k))

        def helper(i,j):
            if j == 9:
                i += 1
                j = 0
            if i == 9:
                return True
            if b[i][j] == '.':
                for k in range(1,10):
                    if is_valid(i,j,k):
                        b[i][j] = str(k)
                        update_set(i,j,k)
                        if( not helper(i,j+1)):
                            reset_set(i,j,k) #Backtracking
                            b[i][j] = '.'
                        else:
                            return True
            else:
                return helper(i,j+1)
        helper(0,0)

# tests
s = Solution()
b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(b)
print(b)