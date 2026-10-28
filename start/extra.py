import random
import sys

COLOR_RESET = "\033[0m"
COLOR_LETTER = "\033[92m"    
COLOR_NUMBER = "\033[93m"    
COLOR_SYMBOL = "\033[91m"    

def get_integer_input(prompt, min_val, max_val):
    """Helper to safely get and validate numeric input within a range."""
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_yes_no(prompt):
    """Helper to get a yes/no response."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'yes']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")

def color_char(char):
    """Color-codes a single character based on its type."""
    if char.isalpha():
        return f"{COLOR_LETTER}{char}{COLOR_RESET}"
    elif char.isdigit():
        return f"{COLOR_NUMBER}{char}{COLOR_RESET}"
    else:
        return f"{COLOR_SYMBOL}{char}{COLOR_RESET}"

def generate_password(length, use_lower, use_upper, use_numbers, use_symbols, 
                      use_unicode, exclude_similar, exclude_ambiguous, first_letter):
    """Generates a single customized password based on user preferences."""
    
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    unicode_chars = "éàèùâêîôûäëïöüçñß€£¥§±÷×"

    pool = ""
    if use_lower: pool += lower
    if use_upper: pool += upper
    if use_numbers: pool += numbers
    if use_symbols: pool += symbols
    if use_unicode: pool += unicode_chars

    if exclude_similar:
        similar_chars = "iIlL1|!"
        pool = ''.join([c for c in pool if c not in similar_chars])

    if exclude_ambiguous:
        ambiguous_chars = "{}[]()/\'\"!,;:>,."
        pool = ''.join([c for c in pool if c not in ambiguous_chars])

    if not pool:
        raise ValueError("Error: Character pool is empty! Please enable at least one character type.")

    password_chars = []

    if first_letter:
        letter_pool = lower + upper
        if exclude_similar:
            letter_pool = ''.join([c for c in letter_pool if c not in "iIlL"])
        if letter_pool:
            first_char = random.choice(letter_pool)
            password_chars.append(first_char)
        else:
            password_chars.append(random.choice(pool))
    
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(random.choice(pool))

    if first_letter and len(password_chars) > 1:
        first = password_chars[0]
        rest = password_chars[1:]
        random.shuffle(rest)
        password_chars = [first] + rest
    else:
        random.shuffle(password_chars)

    return "".join(password_chars)

def main():
    print("    ADVANCED PYTHON PASSWORD GENERATOR ")

    length = get_integer_input("Enter password length (4-300): ", 4, 300)

    print("\n   Select Character Types   ")
    use_lower = get_yes_no("Include lowercase letters (a-z)?: ")
    use_upper = get_yes_no("Include uppercase letters (A-Z)?: ")
    use_numbers = get_yes_no("Include numbers (0-9)?: ")
    use_symbols = get_yes_no("Include symbols (!@#$...)?: ")
    
    print("\n[Note on Unicode]: Unicode characters include accented letters and symbols (e.g: é, ü, ñ).")
    use_unicode = get_yes_no("Include Unicode characters in generation?: ")

    print("\n    Custom Filters    ")
    exclude_similar = get_yes_no("Exclude similar characters (i, I, l, L, 1, |, !)?: ")
    exclude_ambiguous = get_yes_no("Exclude ambiguous characters ({}[]()/\'\"!,;:>,.)?: ")
    first_letter = get_yes_no("Ensure the first character is a letter?: ")

    num_passwords = get_integer_input("\nHow many passwords would you like to generate? (1-20): ", 1, 20)

    print("           GENERATED PASSWORDS            ")
    print(f"({COLOR_LETTER}Green=Letters{COLOR_RESET} | {COLOR_NUMBER}Yellow=Numbers{COLOR_RESET} | {COLOR_SYMBOL}Red=Symbols/Unicode{COLOR_RESET})\n")

    try:
        for i in range(1, num_passwords + 1):
            raw_pwd = generate_password(
                length, use_lower, use_upper, use_numbers, use_symbols,
                use_unicode, exclude_similar, exclude_ambiguous, first_letter
            )
            colored_pwd = "".join([color_char(c) for c in raw_pwd])
            print(f"Password {i:2d}: {colored_pwd}")
    except ValueError as e:
        print(e)
        sys.exit(1)

    print("\n==========================================")

if __name__ == "__main__":
    main()
