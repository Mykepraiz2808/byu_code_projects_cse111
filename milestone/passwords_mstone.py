# Constants
LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")

# Function to check if a word exists in a file
def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False

# Function to check if word has any character from a given list
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# Function to calculate complexity of password
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# Function to evaluate password strength
def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "topPasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity. This is a good password.")
        return 5

    # Otherwise, compute strength based on complexity
    complexity_score = word_complexity(password)
    strength_score = 1 + complexity_score
    print(f"Password has a complexity score of {complexity_score}.")
    return strength_score

# Main input loop
def main():
    print("Welcome to the Password Strength Checker!")
    weak_password_count = 0

    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print(f"\nSession ended. You entered {weak_password_count} weak password(s).")
            break

        strength = password_strength(password)
        print(f"Password Strength Score: {strength} (0 = worst, 5 = best)\n")

        # Recommendations
        if strength <= 2:
            weak_password_count += 1
            print("Tip: Try using a longer password with a mix of UPPER, lower, digits, and special characters.\n")
        elif strength <= 4:
            print("Decent! Add more complexity or length to make it stronger.\n")
        else:
            print("Great job! Your password is strong.\n")

# Only run the main function if this file is the entry point
if __name__ == "__main__":
    main()
