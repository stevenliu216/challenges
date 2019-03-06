# Challenge 21

## String Split, Join, and Slicing

Python has powerful string manipulation capabilities including string indexing,
splitting, joining, and slicing.

This challenge has you take in a string and output three other strings:
1. One with each space replaced by a dash
2. One with last 5 characters all in lowercase
3. One with the string backwards with every other character skipped

### Input Format

Only one line of input containing the string.

### Output Format

Print three lines each on its own line.

### Function Prototypes
    def split_join_slice(line):

    if __name__ == '__main__':
        line = input()
        split_join_slice(line)

### Sample Input
    Sammy Shark

### Sample Output
    Sammy-Shark
    shark
    kaSymS
