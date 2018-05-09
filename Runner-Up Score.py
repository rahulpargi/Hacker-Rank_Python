if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx=max(arr)
    arr.sort()
    arr.reverse()
    for i in arr:
        if i<mx:
            print(i)
            break
