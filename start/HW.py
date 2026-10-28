import os
from passlib.hash import sha512_crypt

def load_dictionary(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.readlines()

def crack_passwords():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shadow_path = os.path.join(script_dir, "shadow")
    
    if not os.path.exists(shadow_path):
        print("Shadow file not found!")
        return

    wordlists = ["top10.txt", "top1000.txt", "top10000000.txt"]
    found_count = 0

    for wl_name in wordlists:
        print(f"\n--- Testing wordlist: {wl_name} ---")
        dictionary = load_dictionary(wl_name)
        if not dictionary:
            print(f"File {wl_name} not found, skipping...")
            continue
        
        with open(shadow_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                shadow_line = line.strip()
                if not shadow_line or ':' not in shadow_line:
                    continue
                
                print(f"Line from shadow file: {shadow_line}")
                
                shadow_parts = shadow_line.split(':')
                user_name = shadow_parts[0]
                user_hash = shadow_parts[1]
                
                if user_hash in ('*', '!', 'x', ''):
                    print("Not found")
                    continue

                found_for_user = False
                for password_guess in dictionary:
                    guess = password_guess.strip()
                    if not guess:
                        continue
                    
                    try:
                        if sha512_crypt.verify(guess, user_hash):
                            print(f"[+] FOUND -> {user_name} : {guess}")
                            found_count += 1
                            found_for_user = True
                            break
                    except Exception:
                        continue
                
                if not found_for_user:
                    print("Not found")
                
                if found_count >= 10:
                    print(f"\n[+] Target reached: Successfully found {found_count} passwords!")
                    return

    print(f"\n[+] Finished. Total passwords found: {found_count}")

if __name__ == "__main__":
    crack_passwords()
