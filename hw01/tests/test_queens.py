import pytest
from src.queens import solve_n_queens

def test_4_queens():
    solutions = solve_n_queens(4)
    # N=4 时，共有 2 个解
    assert len(solutions) == 2

def test_8_queens():
    solutions = solve_n_queens(8)
    # N=8 时，共有 92 个解
    assert len(solutions) == 92

def test_invalid_n():
    # N=1 时有 1 个解，N=2,3 时无解
    assert len(solve_n_queens(1)) == 1
    assert len(solve_n_queens(2)) == 0
    assert len(solve_n_queens(3)) == 0