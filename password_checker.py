print("🔐 Password Strength Checker")
print("----------------------------")

password = input("Enter a password: ")

strength = 0

# 1) Length check
if len(password) >= 8:
    strength += 1

# 2) Uppercase letter check
if any(char.isupper() for char in password):
    strength += 1

# 3) Number check
if any(char.isdigit() for char in password):
    strength += 1

# 4) Special character check
if any(char in "!@#$%^&*()" for char in password):
    strength += 1

print()

# Final Result
if strength == 4:
    print("✅ Strong Password!")
elif strength == 3:
    print("👍 Medium Password")
elif strength == 2:
    print("⚠️ Weak Password")
else:
    print("❌ Very Weak Password")
