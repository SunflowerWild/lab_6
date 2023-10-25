def main():
    run = True
    while run:
        print('''
        Menu
        -------------
        1. Encode
        2. Decode
        3. Quit''')
        selection = int(input("Please enter an option:"))
        if selection == 1:
            password = int(input("Please enter your password to encode:"))
            new_password = encode(password)
            print('Your password has been encoded and stored!')
        if selection == 2:
            print(f'The encoded password is {x}, and the original password is {password}.')
        if selection == 3:
            break
            run = False
def encode(password): # Natalie Poche
    encoded = []
    list = password.split()
    for i in list:
        i = i + 3
        encoded.append(i)
    encoded = "".join(encoded)
    return encoded

if __name__ == "__main__":
    main()