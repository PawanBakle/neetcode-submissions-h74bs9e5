class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        sorted_cars = sorted(cars,reverse = True)

        fleet = 0
        max_arrival_time = 0
        for pos, spd in sorted_cars:
            arrival_time = (target - pos)/spd
            if arrival_time > max_arrival_time:
                fleet += 1
                max_arrival_time = arrival_time
        return fleet