# Mini ATM System 💳

print("💳 Welcome to Mini ATM System")

# PIN code
correct_pin = "1234"

# Balance
balance = 1000

# PIN Check
pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("❌ Wrong PIN! Access denied.")
else:
    print("✅ Login successful!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"💰 Your balance is: {balance} TL")

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print(f"✅ Deposited successfully. New balance: {balance} TL")

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))

            if amount > balance:
                print("❌ Not enough balance!")
            else:
                balance -= amount
                print(f"✅ Withdraw successful. New balance: {balance} TL")

        elif choice == "4":
            print("👋 Thank you for using Mini ATM. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")
