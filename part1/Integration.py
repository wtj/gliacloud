#!/usr/bin/env python
def anonymous(x):
    return x**2 + 1


def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    i = 0
    while intercept < end:
        intercept += step
        # Start of code block
        intercept = round(intercept, 1)
        area += (anonymous(intercept) + anonymous(intercept-step)) * step / 2
        # End of code block
    return area


print(integrate(anonymous, 0, 10))
