import bcrypt
def hash_password(plain_text_pass):
    pass_bytes = plain_text_pass.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)
    return hashed_pass
passwd = "secret"
hashed_pass = hash_password(passwd)
print(f'Password:{passwd} Hash : {str(hashed_pass)}')
