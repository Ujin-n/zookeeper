# put your python code here
day_duration = int(input())
food_cost_day = int(input())
one_way_fly_cost = int(input())
hotel_night_cost = int(input())

print(food_cost_day * day_duration + one_way_fly_cost * 2 + hotel_night_cost * (day_duration - 1))
