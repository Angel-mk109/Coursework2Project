def login_user(username, password):
    """Log in an existing user.""”
     with open("users.txt", "r") as f:
              for line in f.readlines():
                     user, hash = line.strip().split(',', 1)
                      if user == username:
                           return verify_password(password, hash)
  return False
