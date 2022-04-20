motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
bilar = []
bilar.append("gul bil") #append lägger till nytt item till listan
bilar.append("röd bil")
bilar.append("blå bil")
print(bilar)
bilar.insert(0, "svart bil") #insert lägger till på en viss position i listan
print(bilar)
bilar.insert(0, "rosa bil")
print(bilar)
del motorcycles[0] #tar bort item från listan
print(motorcycles)
popped_motorcycle = motorcycles.pop() #pop tar bort den sista på listan om man inte anger en position i parantesen
print(motorcycles)
print(popped_motorcycle)#printar det objekt som togs ur listan
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('suzuki') #tar bort stringen #grr
print(motorcycles)
too_shitty = 'yamaha'
motorcycles.remove(too_shitty) #tar bort variabeln från listan
print(motorcycles)
print(f"\nA {too_shitty.title()} is too shitty for me.")