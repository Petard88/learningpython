prompt = "\nPLease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)

    if city.lower() == 'quit':
        break
    else:
        print(f"I'd love to go to {city}!")