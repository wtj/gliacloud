#!/usr/bin/env python
def func(max_num=1000):
    result = 0
    for i in range(1, max_num):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    print("Find the sum of all the multiples of 3 or 5 below %d." % max_num)
    print("The sum of these multiples is %d." % result)


if __name__ == "__main__":
    func()
