def int_to_roman(input_integer):
    number_value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_numeral = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    solution = ''
    i = 0
    while input_integer > 0:
        for _ in range(input_integer // number_value[i]):
            solution += roman_numeral[i]
            input_integer -= number_value[i]
        i += 1
    return solution



if __name__ == "__main__":
    input_integer = int(input("Enter an integer: "))
    print(int_to_roman(input_integer))
