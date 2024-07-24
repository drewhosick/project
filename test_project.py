import pytest
from project import check_win

def test_check_win():
    assert check_win([5, 3],[5, 3]) == True
    assert check_win([5, 3],[3, 5]) == False
    assert check_win([5, 3],[5, 11]) == False