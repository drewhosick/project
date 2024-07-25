import pytest
from project import check_win, pick_direction, pick_start, check_edge

def test_check_win():
    assert check_win([5, 3],[5, 3]) == True
    assert check_win([5, 3],[3, 5]) == False
    assert check_win([5, 3],[5, 11]) == False

def test_pick_direction():
    assert pick_direction(["left"]) == "left"
    assert pick_direction(["right"]) == "right"
    assert pick_direction(["up"]) == "up"
    assert pick_direction(["down"]) == "down"

def test_pick_start():
    start = pick_start(5, 5)
    assert 1 in start or 2 in start or 3 in start
    assert 0 not in start or 5 not in start

def test_check_edge():
    assert check_edge(1, 1, 20, 10) == ["down", "right"]
    assert check_edge(10, 10, 12, 15) == ["up", "left", "right"]
    assert check_edge(5, 10, 20, 12) != ["up", "down", "left", "right"]