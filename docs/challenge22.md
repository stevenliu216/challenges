# Challenge 22

## Regular Expressions - Validating Phone Numbers

> Some people, when confronted with a problem, think 
“I know, I'll use regular expressions.”   Now they have two problems. - Jamie Kawinski

Let's dive into the interesting topic of regular expressions! You are given some
input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with 313 or 248.

### Function Prototype

    def validate_phone_number(phone_number_list):


    if __name__ == '__main__':
        n = int(input("Enter number of phone numbers: "))
        phone_number_list = []
        for number in range(n):
            entered_num = input("Phone number " + str(number + 1) + ": ")
            phone_number_list.append(entered_num)
        print(*validate_phone_number(phone_number_list), sep="\n")
    

### Input Format

The first line contains an integer N, the number of inputs. N lines follow, each
containing some string.

### Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if
it is not on separate lines. Do not print the quotes.

### Sample Input

    2
    3137456281
    1252478965
     
### Sample Output

    YES
    NO