import operator


def person_lister(func):
    def inner(people):
        people.sort(key=operator.itemgetter(2))
        return [func(person) for person in people]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    n = int(input("Enter number of names to format: "))
    people = [input("Enter name age gender " + str(i + 1) + ": ").split() for i in range(n)]
    print(*name_format(people), sep="\n")
