mina_goa_pizzor = ["vesuvio", "frutti del mare", "capriciosa"]
alex_goa_pizzor = mina_goa_pizzor[:]
mina_goa_pizzor.append("calzone")
alex_goa_pizzor.append("smörbabben")
print("\nMina favoritpizzor är:")
for pizza in mina_goa_pizzor:
    print(pizza.title())
print("\nAlex favoriter är:")
for pizza in alex_goa_pizzor:
    print(pizza.title())

print("\n\njävla smarrigt du")