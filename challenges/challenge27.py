from typing import List


def reach_the_finish(batteries: List[int]) -> bool:
    current_batt = batteries[0]
    road_length = len(batteries)
    if road_length > 1:
        for pos in range(road_length - 1):
            battery_on_road = batteries[pos]
            if battery_on_road > current_batt:
                current_batt = battery_on_road
            if current_batt == 0:
                return False
            current_batt -= 1
    return True


if __name__ == "__main__":
    road_length = int(input("Please enter length of road: "))
    battery_locations = [
        int(input(f"Please enter battery {pos + 1}: ")) for pos in range(road_length)
    ]
    print(reach_the_finish(battery_locations))
