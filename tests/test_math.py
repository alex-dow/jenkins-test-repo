from jtr import jtr
import time

def test_add():
    a = 1
    b = 2
    time.sleep(10)
    assert jtr._add(a, b) == 3

def test_sub():
    a = 3
    b = 2

    assert jtr._sub(a, b) == 1

def test_mult():
    a = 2
    b = 4

    assert jtr._mult(a, b) == 8

def test_div():
    a = 0
    b = 0
    assert jtr._div(a, b) == 0

