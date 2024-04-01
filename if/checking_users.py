current_users = ['catyaya', 'learncode', 'rosamundpike', 'catislife', 'venUs']

new_users = ['valorant', 'twitter', 'Learncode', 'VENUS', 'redvelvet']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'\033[31mThe username {user} is not available. You will need to enter a new username.\033[m')
    else:
        print(f'\033[32mThe username {user} is available!\033[m')