import Calculator

def test_add():
    x = 10
    y = 20
    result = Calculator.add(x, y)
    assert x+y==result

def test_sub():
    x = 30
    y = 12
    result = Calculator.sub(x, y)
    assert x-y==result

def test_mul():
    x = 10
    y = 20
    result = Calculator.mul(x, y)
    assert x*y==result

def test_div():
    x = 20
    y = 10
    result = Calculator.div(x, y)
    assert x/y==result

