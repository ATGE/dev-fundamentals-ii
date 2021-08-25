#https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    words={}
    n = int(input())
    for x in range(n):
        word=input()
        if words.get(word):
            words[word]+=1
        else:
            words[word]=1
    print(len(words))
    print(*words.values())
