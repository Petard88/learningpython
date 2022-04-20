prompt1 = "Vill du ha tjock eller tunn botten?"
prompt1 += "\nSkriv här: "


prompt = "Skriv vad du vill ha på din pizza!"
prompt += "\n'exit' = avsluta, 'list' = visa vad som finns på diskusen"
prompt += "\nIngrediens: "

available = ['oxfilé', 'kyckling', 'pommes', 'ost', 'tomatsås', 'vitlök', 'räkor', 'bacon', 'salami', 'skinka',
             'kebabkött', 'sallad', 'lök', 'gurka', 'tomat', 'champinjoner', 'bearnaise', 'kebabsås', 'vitlöksås']
pizza = []
bottens = ['tjock', 'tunn', 'knäcke', 'ingen']
vald_botten = []
running = True

while running == True:
    botten = input(prompt1)# måste vara under while true annars blire infinite loop
    if len(vald_botten) == 0:
        if botten.lower() == 'exit':
            running == False
            break
        else:
            if botten.lower() not in bottens:
                print(f"\nVälj ett av alternativen din specialbegåvade palsternacka!")
                for bottnar in bottens:
                    print(f"\t{bottnar.title()}")
            else:
                print(f"Du har valt {botten.title()} botten!")
                vald_botten.append(botten)

    while len(vald_botten) > 0:
        topping = input(prompt) # måste vara under while true annars blir det en infinite loop

        if topping.lower() == 'exit':
            running = False
            break
        elif topping.lower() == 'list':
            print("\n*****************************************")
            print(f"\tDu har valt {vald_botten} botten.")
            print("\tDin pizza har följande pålägg:")
            for ingrediens in pizza:
                print(f"\t*{ingrediens.title()}")
            print("*****************************************\n")
        else:
            if topping.lower() not in available:
                print("\n*****************************************")
                print(f"Den ingrediensen har vi inte. \nVälj något från listan:")
                for ingrediens in available:
                    print(f"*{ingrediens.title()}")
                print("*****************************************\n")
            else:
                print(f"\n***Lägger till {topping} på din pizza!***\n")
                pizza.append(topping)
