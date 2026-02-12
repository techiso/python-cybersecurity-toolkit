import base64

print("🔓 Decrypt Notes App")
print("----------------------")

# Read encrypted file
with open("secret_note.txt", "rb") as file:
    encoded_data = file.read()

# Decode
decoded_data = base64.b64decode(encoded_data).decode()

# Split password and note
saved_password, saved_note = decoded_data.split("::")

# Ask user password
password_input = input("Enter password to unlock note: ")

if password_input == saved_password:
    print("\n✅ Correct Password!")
    print("Your Secret Note:\n")
    print(saved_note)
else:
    print("\n❌ Wrong Password! Access Denied.")
