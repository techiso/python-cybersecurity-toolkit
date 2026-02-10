import hashlib

print("🔐 Secure Login System Demo")
print("----------------------------")

# Register
password = input("Create a password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\n✅ Password saved securely!\n")

# Login
login_password = input("Enter password to login: ")
login_hash = hashlib.sha256(login_password.encode()).hexdigest()

if login_hash == hashed_password:
    print("\n✅ Login Successful!")
else:
    print("\n❌ Wrong Password!")
