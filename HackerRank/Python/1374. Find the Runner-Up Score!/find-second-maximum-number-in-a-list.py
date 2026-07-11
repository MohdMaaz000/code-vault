if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = sorted(set(arr))
    print(scores[-2])
