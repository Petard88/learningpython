current_users = ["AuGust", "bEngAn", "CesaR", "David", "erIK"]
current_users_lower = [user.lower() for user in current_users] #ny lista som konverterar till lowercase.
new_users = ["aUgUST", "BENGAN", "filip", "göran", "henrik", "ERIK", "666iNgVaR666"]

for user in new_users:
    if user.lower() in current_users_lower: #konverterar namnen i new_users till lowercase och kollar mot listan
        print(f'Username "{user.title()}" already in use. Please select another username.')
    else:
        print(f'Username "{user.title()}" available.')