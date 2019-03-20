# Chellenge 23

### Decorators to Create a Name Directory

Let's use decorators to build a name directory! You are given some information
about  people. Each person has a first name, last name, age, and gender. Print their
names in a specific format sorted by their age in ascending order, for example the
youngest person's name should be printed first. For two people of the same age,
print them in the order of their input.

For Ignas Brazdeikis, the output should be:

    Mr. Ignas Brazdeikis

For Japreece Dean, the output should be:

    Ms. Japreece Dean

### Function Prototype
    def person_lister(func):
        def inner(people):
            # Your code here
        return inner


    @person_lister
    def name_format(person):
        return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


    if __name__ == "__main__":
        n = int(input("Enter number of names to format: "))
        people = [input("Enter name age gender " + str(i + 1) + ": ").split() for i in range(n)]
        print(*name_format(people), sep="\n")
        
### Input Format

The first line contains the integer N, the number of people. N lines follow each
containing the space separated values of the first name, last name, age, and gender.


### Output Format

Output N names on separate lines in the format described above in ascending order of age.

Sample Input

    3
    Zion Williamson 20 M
    Ja Morant 19 M
    Macy Miller 22 F
    
Sample Output

    Mr. Ja Morant
    Mr. Zion Williamson
    Ms. Macy Miller
