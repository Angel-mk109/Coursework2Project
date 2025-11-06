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