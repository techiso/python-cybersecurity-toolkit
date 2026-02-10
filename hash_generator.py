# Project 9: SHA256 Hash Generator 🔥

import hashlib

print("🔐 SHA256 Hash Generator")
print("-------------------------")

text = input("Enter text to hash: ")

hashed = hashlib.sha256(text.encode()).hexdigest()

print("\n✅ SHA256 Hash Result:")
print(hashed)
