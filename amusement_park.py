age = 122

if age < 4:
    print("Your admission cost is $0") #svårare att ändra på 3 olika
elif age < 18:
    print("Your admission cost is $25") #elif = else if / if else
else:
    print("Your admission cost is $40")

if age < 4:
    price = 0 #sätter price = värdet som angetts som en variabel som sparas
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.") #behöver bara ändra på ett ställe med den här metoden
#betydligt mer lättläst