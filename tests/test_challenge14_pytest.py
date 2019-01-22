from challenges.challenge14 import captains_room


def test_captains_room():
    room_numbers = [
        1,
        2,
        3,
        6,
        5,
        4,
        4,
        2,
        5,
        3,
        6,
        1,
        6,
        5,
        3,
        2,
        4,
        1,
        2,
        5,
        1,
        4,
        3,
        6,
        8,
        4,
        3,
        1,
        5,
        6,
        2,
    ]
    captains_num = captains_room(5, room_numbers)
    assert captains_num == 8
    room_numbers = [3, 1, 2, 1, 2]
    captains_num = captains_room(2, room_numbers)
    assert captains_num == 3
