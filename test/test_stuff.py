import sys
sys.path.append('src/')
import stuff

def test_add():
    assert stuff.add(1, 2) == 3
    assert stuff.add(10, 1) == 11
    assert stuff.add(5, 6) == 11
    assert stuff.add(6, 6) == 12

def test_dot():
    assert stuff.dot(1, 1) == 1
    assert stuff.dot(5, 1) == 5
    assert stuff.dot(3, 5) == 15
    assert stuff.dot(4, 5) == 20
