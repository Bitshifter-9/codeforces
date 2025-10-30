# cook your dish here
def main():
    n = int(input())
    n = n - 1
    w_list = list(map(int, input().split()))
    w_list = sorted(w_list)
    count = 0
    w = 0
    for i in range(1, n + 1):
        count += w_list[w]
        w += i
        print(w)
    print(count)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        main()