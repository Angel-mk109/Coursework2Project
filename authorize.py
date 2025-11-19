import bcrypt
def hash_password(plain_text_pass):
    pass_bytes = plain_text_pass.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)
    return hashed_pass
passwd = "secret"
hashed_pass = hash_password(passwd)
print(f'Password:{passwd} Hash : {str(hashed_pass)}')

import bcrypt
import username

from authorize import hash_password

def register_user(username, password):
    """Register a new user."""
    hashed_password = hash_password(password)


with open("users.txt", "a") as f:
    f.write(f"{username},{hash_password}\n")
print(f"User '{username}' registered.")


def login_user(username, password):
    """Log in an existing user.""”
     with open("users.txt", "r") as f:
              for line in f.readlines():
                     user, hash = line.strip().split(',', 1)
                      if user == username:
                           return verify_password(password, hash)
  return False"""
print()

from authorize import hash_password
test_password = "SecurePassword123"
hashed = hash_password(test_password)
print(f"Original password: {test_password}")
print(f"Hashed password: {hashed}")
print(f"Hash length: {len(hashed)} characters")
is_valid = verify_password(test_password, hashed)
print(f"\nVerification with correct password: {is_valid}")
is_invalid = verify_password("WrongPassword", hashed)
print(f"Verification with incorrect password: {is_invalid}")


import loop
import program


def display_menu():
"""Displays the main menu options."""
print("\n" + "="*50)
print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
print(" Secure Authentication System")
print("="*50)
print("\n[1] Register a new user")
print("[2] Login")
print("[3] Exit")
print("-"*50)
def main():
""Main program loop."""
print("\nWelcome to the Week 7 Authentication System!")
while True:
display_menu()
choice = input("\nPlease select an option (1-3): ").strip()
if choice == '1':
# Registration flow
print("\n--- USER REGISTRATION ---")
username = input("Enter a username: ").strip()
# Validate username
is_valid, error_msg = validate_username(username)
if not is_valid:
print(f"Error: {error_msg}")
continue
password = input("Enter a password: ").strip()
# Validate password
is_valid, error_msg = validate_password(password)
if not is_valid:
print(f"Error: {error_msg}")
continue
# Confirm password
password_confirm = input("Confirm password: ").strip()
if password != password_confirm:
print("Error: Passwords do not match.")
continue
# Register the user
register_user(username, password)
elif choice == '2':
# Login flow
print("\n--- USER LOGIN ---")
username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()
# Attempt login
if login_user(username, password):
print("\nYou are now logged in.")
print("(In a real application, you would now access the d
# Optional: Ask if they want to logout or exit
input("\nPress Enter to return to main menu...")
elif choice == '3':
# Exit
print("\nThank you for using the authentication system.")
print("Exiting...")
break
else:
print("\nError: Invalid option. Please select 1, 2, or 3.")
if __name__ == "__main__":
main()


<username.Username object at 0x10f08b770>,<function hash_password at 0x10f26a200>
<username.Username object at 0x1078c7770>,<function hash_password at 0x107aa5800>
<username.Username object at 0x104533770>,<function hash_password at 0x104711800>
<username.Username object at 0x10422f770>,<function hash_password at 0x10440d800>
<username.Username object at 0x1119c0440>,<function hash_password at 0x1119bfba0>
<username.Username object at 0x116bf5940>,<function hash_password at 0x116c2b560>
<username.Username object at 0x112500440>,<function hash_password at 0x1124ffba0>
