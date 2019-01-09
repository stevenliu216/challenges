def fizz_buzz(game_length):
    for game_num in range(1, game_length + 1):
        if game_num % 3 == 0 and game_num % 5 == 0:
            print("FizzBuzz")
        elif game_num % 3 == 0:
            print("Fizz")
        elif game_num % 5 == 0:
            print("Buzz")
        else:
            print(game_num)


fizz_buzz(15)
