# https://www.hackerrank.com/challenges/python-loops/problem

def print_square(number):
    if number<1 or number>20:
        return
    for x in range(0,number):
        print(x**2)
if __name__ == '__main__':
    n = int(input())
    print_square(n)
