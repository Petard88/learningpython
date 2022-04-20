prompt = "Enter what topping you'd like on your pizza: "
prompt += "\nEnter 'quit' when you're done."
total_toppings = []# tom lista för totalen, kommer fyllas på senare
while True:
    topping = input(prompt)# variabeln topping är lika med vad användaren skriver

    if topping.lower() == 'quit':# om variabelns värde är lika med quit
        break# byt från true till false
    else:
        print(f"Adding {topping} to your pizza")# topping = vad användaren skrev
        total_toppings.append(topping.title())# lägger till topping med stor bokstav till total listan
        print(f"\nYour pizza has the following toppings:")
        for top in total_toppings:# för varje sparat värde i totala listan, printa ut det
            print(f"{top}\t")