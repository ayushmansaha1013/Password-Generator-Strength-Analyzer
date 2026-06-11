import random
import string

#the main function to run the program
def main():
    print("Welcome to the Password Generator and Strength Analyzer! 🔒")
    print ("_" * 50)
    print("\n")
    print("1. Generate a Password")
    print("2. Analyze Password Strength")
    print("3. Exit")
    print("_" * 30)
    print("\n")
    choice = input("Enter your choice (1-3): _")
    if choice == "1":
        length = int(input("How many characters do you want in your password? 🕵️‍♂️ "))
        password = password_generator(length)
        print(f"Generated Password: {password}")
    elif choice == "2":
        letters = int(input("Enter the no. of letters you wanted in the password! 🔑"))
        checking = input("Enter the password that was generated! _")
    #rest to be made
    
    elif choice == "3":
        print("Goodbye for now! ")
        print("_" * 50)
    else:
        print("please choose from (1-3) only! ")
    

#Password generator function
def password_generator(length):
    pool = string.ascii_letters + string.digits + string.punctuation #storing all the characters in a variable
    
    password = "" #main variable to store the password
    for i in range(length):
        password += random.choice(pool)
    return password #printing the password to user
#def password_checker:
    

#calling the function
if __name__ == "__main__":
    main()
