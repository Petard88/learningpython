my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("öl")
my_foods.append("cannoli")

friend_foods.append("ice cream")
friend_foods.append("sprit")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in friend_foods:
    print(f"{food} is goooooood!")