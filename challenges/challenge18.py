def exceptions(a, b):
    try:
        division = int(a) // int(b)
        print(division)
        return division
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
        return f"Error Code: {e}"


if __name__ == "__main__":
    dividers = input("Enter the inputs to divide: ").split()
    t = int(dividers[0])
    ab_pairs = []
    for _ in range(t):
        ab_pairs.append(list(input().split()))
    print("\n")
    for i in range(t):
        exceptions(ab_pairs[i][0], ab_pairs[i][1])
