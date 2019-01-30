def athlete_sort(k, arr):
    sorted_arr = sorted(arr, key=lambda athlete: athlete[k])
    for athlete in sorted_arr:
        print(*athlete)
    return sorted_arr


if __name__ == "__main__":
    nm = input("Enter the input table: ").split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    print("\n")

    athlete_sort(k, arr)
