import bcrypt
import username

from authorize import hash_password


def register_user(username, password):
    """Register a new user."""
    hashed_password = hash_password(password)


with open("users.txt", "a") as f:
    f.write(f"{username},{hash_password}\n")
print(f"User '{username}' registered.")
