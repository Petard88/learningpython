magicians = ['alice', 'david', 'carolina']
for magician in magicians: #upprepar för varje värde i listan, gör om variabeln magician till det aktuella värdet
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!") #skriver ut texten efter for-loopen avslutats
