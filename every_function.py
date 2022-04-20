handla = ["Smör", "Bröd", "Juice", "Skinka"]
antal = len(handla)
meddelande = f"Min inköpslista innehåller {antal} saker: \n{handla}"
print(meddelande)
handla.append("Tomater")
handla.insert(0, "Ägg")
handla.remove("Skinka")
meddelande = f"Min inköpslista innehåller {antal} saker: \n{handla}"
print(meddelande.upper())
