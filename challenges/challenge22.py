def validate_phone_number(phone_number_list):
    pass


if __name__ == '__main__':
    n = int(input("Enter number of phone numbers: "))
    phone_number_list = []
    for number in range(n):
        entered_num = int(input("Phone number " + str(number + 1) + ": "))
        phone_number_list.append(entered_num)
    print(validate_phone_number(phone_number_list))
