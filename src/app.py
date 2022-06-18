import sys
import os


def prime(s):
    # your code goes here
    for num in range(2,s):
        if s % num == 0:
            return f' The value {s} is not a prime number'
        else:
            return f' The value {s} is a prime number'

s = int(input("enter a value: "))

def solution(s):
    return prime(s)

print(solution(s))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))

print(type(sys))