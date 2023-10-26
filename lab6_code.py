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
            password = str(input("Please enter your password to encode:"))
            x = encode(password)
            print('Your password has been encoded and stored!')
        if selection == 2:
            password = decode(x)
            print(f'The encoded password is {x}, and the original password is {password}.')
        if selection == 3:
            break
            run = False

def encode(password): # Natalie Poche
    encoded = [] # creates a list
    for i in password[::]: # separates the numbers in the previous list
        i = int(i) + 3 # adds 3 to the previous numbers
        encoded.append(str(i)) # adds the new number to the new list
    encoded = "".join(encoded) # turns the list into a string
    return encoded

def decode(new_password): # Natalie Poche
    decode = [] # creates a new list
    for i in new_password[::]: # goes through each previous number
        i = int(i) - 3 # subtracts 3
        decode.append(str(i)) # adds to new list
    decode = "".join(decode) # turns list into a string
    return decode

if __name__ == "__main__":
    main()