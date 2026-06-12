import random
import string

# Password generator function
def password_generator(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(pool)
    return password


# Password strength analyzer
def password_checker(password):
    score = 0
    
    # Check 1: Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    # Check 2: Uppercase
    if any(char.isupper() for char in password):
        score += 1
    
    # Check 3: Lowercase
    if any(char.islower() for char in password):
        score += 1
    
    # Check 4: Digits
    if any(char.isdigit() for char in password):
        score += 1
    
    # Check 5: Special characters
    if any(char in string.punctuation for char in password):
        score += 1
    
    # Check 6: Sequences (123, abc, etc.)
    has_sequence = False
    for i in range(len(password) - 2):
        if (ord(password[i+1]) == ord(password[i]) + 1 and
            ord(password[i+2]) == ord(password[i+1]) + 1):
            has_sequence = True
            break
    
    if has_sequence:
        score -= 2
    
    return max(1, min(score, 10))  # Return between 1-10


# Get strength label
def get_strength_label(score):
    if score <= 2:
        return "Very Weak"
    elif score <= 4:
        return "Weak"
    elif score <= 6:
        return "Moderate"
    elif score <= 8:
        return "Strong"
    else:
        return "Very Strong"


# Main function
def main():
    while True:
        print("Welcome to the Password Generator and Strength Analyzer! 🔒")
        print("_" * 50)
        print("\n1. Generate a Password")
        print("2. Analyze Password Strength")
        print("3. Exit")
        print("_" * 50)
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            length = int(input("How many characters do you want? "))
            password = password_generator(length)
            score = password_checker(password)
            label = get_strength_label(score)
            
            print(f"\nGenerated Password: {password}")
            print(f"Strength: {label} ({score}/10)\n")
        
        elif choice == "2":
            password_to_check = input("Enter password to analyze: ")
            score = password_checker(password_to_check)
            label = get_strength_label(score)
            
            print(f"\nPassword: {password_to_check}")
            print(f"Strength: {label} ({score}/10)\n")
        
        elif choice == "3":
            print("Goodbye for now!")
            print("_" * 50)
            break
        
        else:
            print("Please choose from (1-3) only!\n")


if __name__ == "__main__":
    main()
