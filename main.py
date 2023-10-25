def main():
    print("Menu")
    print("-" * 13)
    print("1. Encode \n2. Decode \n3. Quit")

def encode(number):
    pass

def decode():
    pass

if __name__ == "__main__":
    condition = True
    while condition == True:
        main()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            number = encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
            print(number)
        elif choice == 2:
            print(f"The encoded password is {new_number}, and the original password is {number}")
        elif choice == 3:
            condition = False