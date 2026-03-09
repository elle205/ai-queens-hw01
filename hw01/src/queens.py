def solve_n_queens(n: int) -> list[list[str]]:
    """
    解决 N 皇后问题，返回所有合法的棋盘布局。
    每个布局是一个字符串列表，'Q' 代表皇后，'.' 代表空位。
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_valid(row: int, col: int) -> bool:
        # 检查同一列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 检查左上对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 检查右上对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row: int) -> None:
        if row == n:
            # 将当前棋盘转换为字符串列表并保存
            solution = [''.join(row) for row in board]
            result.append(solution)
            return
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # 回溯

    backtrack(0)
    return result

def print_solutions(solutions: list[list[str]]) -> None:
    """打印所有解的布局"""
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in sol:
            print(row)
        print()

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"Found {len(solutions)} solutions for {n}-Queens:")
    print_solutions(solutions)
