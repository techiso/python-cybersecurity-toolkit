import random
import string

print("🔐 Password Generator Tool")
print("--------------------------")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for i in range(length))

print("\n✅ Generated Strong Password:")
print(password)
import random
import string

def run():
    print("\n🔐 Password Generator")
    print("----------------------")

    length = int(input("Enter password length: "))

    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))

    print("\n✅ Generated Password:")
    print(password)