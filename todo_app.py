# Project 4: To-Do List App 📝

tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\n📌 Your Tasks:")
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nWhich task number do you want to remove?")
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            remove = int(input("Enter number: "))
            if 1 <= remove <= len(tasks):
                tasks.pop(remove - 1)
                print("🗑️ Task removed!")
            else:
                print("❌ Invalid number.")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("❌ Please choose between 1-4.")
