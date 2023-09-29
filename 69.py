import math


def mySqrt(x):
    return math.floor(pow(2, 0.5 * math.log2(x)))



num=int(input("Enter any number"))
print(mySqrt(num))    