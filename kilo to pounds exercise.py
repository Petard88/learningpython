weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "K":
    print(f"You are {weight / 0.45} lbs")
elif unit.upper() == "L":
    print(f"You are {weight * 0.45} kgs")
else:
    print("Type k for Kgs or l for Lbs")