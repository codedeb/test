def test(*args):
    return sum(*args)


obj = test([1, 2, 3, 4, 5, 5])
print(obj)
