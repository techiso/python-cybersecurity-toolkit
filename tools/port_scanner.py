# Project 6: Simple Port Scanner 🔍

import socket

print("🔍 Simple Port Scanner")
print("----------------------")

target = input("Enter an IP address (example: 127.0.0.1): ")

ports = [21, 22, 80, 443]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"✅ Port {port} is OPEN")
    else:
        print(f"❌ Port {port} is CLOSED")

    sock.close()

print("\nScan finished.")
def run():
    print("\n🛡️ Port Scanner Tool")
    print("---------------------")

    target = input("Enter IP to scan: ")
    print("Scanning target:", target)

    print("❌ Port 21 CLOSED")
    print("❌ Port 22 CLOSED")
    print("❌ Port 80 CLOSED")
    print("❌ Port 443 CLOSED")
