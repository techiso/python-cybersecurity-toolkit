# Project 5: Website IP Finder 🌐

import socket

print("🌍 Website IP Finder Tool")
print("--------------------------")

website = input("Enter a website (example: google.com): ")

try:
    ip_address = socket.gethostbyname(website)
    print(f"✅ The IP address of {website} is: {ip_address}")

except socket.gaierror:
    print("❌ Website not found. Please enter a valid domain.")
import socket

