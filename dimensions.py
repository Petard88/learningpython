dimensions = (200, 50)  # tuples kan inte ändras
# print(dimensions[0]) print(dimensions[1]) dimensions[0] = 250 #ger error eftersom den försöker ändra en tuple och
# tuples kan inte ändras my_t = (3,) #man måste ha kommat med för att det ska bli en tuple även om den bara
# innehåller en siffra av någon anledning.
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
