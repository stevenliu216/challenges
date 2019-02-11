order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"


def ginorts_sort(s):
    sort_string = sorted(s, key=order.index)
    print(*sort_string, sep="")
    return "".join(map(str, sort_string))


if __name__ == "__main__":
    s = input("Enter the string: ")

    ginorts_sort(s)
