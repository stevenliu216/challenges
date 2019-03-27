import calendar


def get_dotw(month, day, year):
    dotw = calendar.weekday(year, month, day)
    return calendar.day_name[dotw].upper()


if __name__ == "__main__":
    date = input("Please enter the date in MM DD YYYY format: ").split()
    month, day, year = int(date[0]), int(date[1]), int(date[2])
    print(get_dotw(month, day, year))

