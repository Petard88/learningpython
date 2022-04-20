#skriver att green peppers är slut. om man önskar det.
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, no pepper for u.")
    else:
        print(f"Adding {requested_topping} to your pizza.")

print("\nYour pizza be done")

#annan variant som kollar om man verkligen vill ha en pizza utan något på om man lämnar listan tom
requested_toppings = ["keso"]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f" Adding {requested_topping}.")
    print("\nDone")
else:
    print("Are u sure?")