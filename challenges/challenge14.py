from collections import Counter


def captains_room(group_size, room_numbers):
    counts = Counter(room_numbers)
    for room_num in room_numbers:
        if counts[room_num] < group_size:
            return room_num


if __name__ == "__main__":
    group_size = int(input("Enter the size of each group: "))
    room_numbers = [
        int(num)
        for num in input(
            "Enter the space separated array of all room numbers: "
        ).split()
    ]
    print(f"The captain's room is {captains_room(group_size, room_numbers)}")
