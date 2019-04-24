def is_palindrome(checked_int: int) -> bool:
    forward = str(checked_int)
    backward = forward[::-1]
    if forward == backward:
        return True
    else:
        return False


if __name__ == "__main__":
    checked_int = int(input("Please enter the integer: "))
    print(is_palindrome(checked_int))

