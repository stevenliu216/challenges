from typing import List
import itertools


def letter_combinations(digits: str) -> List[str]:
    number_pad = {"2": ("a", "b", "c"),
                  "3": ("d", "e", "f"),
                  "4": ("g", "h", "i"),
                  "5": ("j", "k", "l"),
                  "6": ("m", "n", "o"),
                  "7": ("p", "q", "r", "s"),
                  "8": ("t", "u", "v"),
                  "9": ("w", "x", "y", "z"),
                  }
    letter_groups = []
    for num in digits:
        letter_groups.append(number_pad[num])
    combos = []
    if letter_groups:
        for combo in itertools.product(*letter_groups):
            combos.append("".join(combo))
    return combos


if __name__ == "__main__":
    print(letter_combinations(input("Enter digit: ")))
