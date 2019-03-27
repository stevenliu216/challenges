# Challenge 24

## Calendars!
The calendar module allows you to output calendars and provides additional useful functions for them.

class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.

### Sample Code

    >>> import calendar
    >>> print(calendar.TextCalendar().formatyear(2019))
                                      2019
                                      
          January                   February                   March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6                   1  2  3                   1  2  3
     7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
    14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
    21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
    28 29 30 31               25 26 27 28               25 26 27 28 29 30 31
    
           April                      May                       June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7             1  2  3  4  5                      1  2
     8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
    15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
    22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
    29 30                     27 28 29 30 31            24 25 26 27 28 29 30
    
            July                     August                  September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7                1  2  3  4                         1
     8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
    15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
    22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
    29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                        30
                                                        
          October                   November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6                   1  2  3                         1
     7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
    14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
    21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
    28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                        30 31

### Task

You are given a date. Your task is to find what the day is on that date.

### Function Prototype

    import calendar


    def get_dotw(month, day, year):
        # Your code here


    if __name__ == "__main__":
        date = input("Please enter the date in MM DD YYYY format: ").split()
        month, day, year = int(date[0]), int(date[1]), int(date[2])
        print(get_dotw(month, day, year))


### Input Format

A single line of input containing the space separated month, day, and year, respectively, in MMDDYYYY format.

### Output Format

Output the correct day in capital letters.

### Sample Input

    03 27 2019
    
### Sample Output

    WEDNESDAY
    
### Explanation

March 27, 2019 was a WEDNESDAY.