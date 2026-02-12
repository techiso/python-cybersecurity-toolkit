import base64

print("🔐 Encrypted Notes App")
print("----------------------")

# Note input
note = input("Enter your secret note: ")

# Password input
password = input("Enter a password to lock it: ")

# Combine note + password
combined = password + "::" + note

# Encode (simple encryption)
encoded_note = base64.b64encode(combined.encode())

# Save to file
with open("secret_note.txt", "wb") as file:
    file.write(encoded_note)

print("\n✅ Note saved securely in secret_note.txt")
def run():
    print("\n🔐 Encrypted Notes App")
    print("----------------------")

    note = input("Enter your secret note: ")

    with open("data/secret_note.txt", "w") as file:
        file.write(note)

    print("✅ Note saved successfully!")