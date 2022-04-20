squares = []
for value in range(1, 11):
    squares.append(value**2) #kortare verision som gör samma sak som exemplet nedan

print(squares)

upphöjt = []
for value in range(1, 11):
    upphöj = value ** 2
    upphöjt.append(upphöj)

print(upphöjt)

squares2 = [value**2 for value in range(1, 11)]
print(squares2)