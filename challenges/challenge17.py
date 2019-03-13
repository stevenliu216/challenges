order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"


def ginorts_sort(s):
    sort_string = sorted(s, key=order.index)
    return "".join(map(str, sort_string))


if __name__ == "__main__":
    s = input("Enter the string: ")
    print(ginorts_sort(s))
