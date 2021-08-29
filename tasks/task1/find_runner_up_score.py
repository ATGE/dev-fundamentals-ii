#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up_index =-2
    runner_up =sorted(set(arr))[runner_up_index]
    print(runner_up)
