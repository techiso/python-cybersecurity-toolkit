from tools import ip_finder
from tools import port_scanner
from tools import password_generator
from tools import hash_generator
from tools import log_analyzer
from tools import encrypted_notes


def show_menu():
    print("\n🛡️ CyberSecurity Toolkit Panel")
    print("--------------------------------")
    print("1) IP Finder")
    print("2) Port Scanner")
    print("3) Password Generator")
    print("4) Hash Generator")
    print("5) Log Analyzer")
    print("6) Encrypted Notes App")
    print("0) Exit")


while True:
    show_menu()
    choice = input("\nSelect an option: ")

    if choice == "1":
        ip_finder.run()

    elif choice == "2":
        port_scanner.run()

    elif choice == "3":
        password_generator.run()

    elif choice == "4":
        hash_generator.run()

    elif choice == "5":
        log_analyzer.run()

    elif choice == "6":
        encrypted_notes.run()

    elif choice == "0":
        print("\n👋 Exiting... Goodbye Patron!")
        break

    else:
        print("❌ Invalid choice! Try again.")