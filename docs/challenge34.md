# Challenge 34
### Bank Terminal

Write a program that computes the net amount of a bank account based a transaction log from console input.
```
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
```

### Example
Suppose the following input is supplied to the program:
```
D 300
D 300
W 200
D 100
```
Then, the output should be:
```
500
```

### Function Prototype
```
def bank_terminal():
    pass

if __name__ == "__main__":
    bank_terminal()
