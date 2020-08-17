# count all the steps
def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')

# 1 + 1 + n/2 + 1000 = 1002 + n/2 = o(n/2) = 0(n)

# increase input size
# compare increase in the function steps


def simple_recurse(n):
    if n <= 1:
        return n
    simple_recurse(n-1)


simple_recurse(5)  # 10 steps
simple_recurse(10)  # 20 steps
# 0(n)


def weird_recurse(num):
    if n <= 1:
        return n
    simple_recurse(n-1)
    simple_recurse(n-1)
    simple_recurse(n-1)
# double last time: 0(n)?
