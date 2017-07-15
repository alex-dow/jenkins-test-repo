from jtr import jtr
import time

def test_add():
    a = 1
    b = 2

    assert jtr._add(a, b) == 3

def test_sub():
    a = 3
    b = 2

    time.sleep(30)

    assert jtr._sub(a, b) == 1

