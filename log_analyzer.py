# Project 7: Log Analyzer Tool 📄
import os

print("Çalışma klasörü:", os.getcwd())

filename = input("Enter log file name: ")
print("📄 Log Analyzer Tool")
print("---------------------")

filename = input("Enter log file name (example: log.txt): ")

keywords = ["error", "failed", "attack", "warning"]

try:
    with open(filename, "r") as file:
        content = file.read().lower()

    print("\n--- Analysis Result ---")

    for word in keywords:
        count = content.count(word)
        print(f"'{word}' found: {count} times")

    print("\n✅ Log analysis finished.")

except FileNotFoundError:
    print("❌ File not found. Please check the file name.")
with open(filename, "r") as file:
    content = file.read().lower()

print("\nDosya içeriği:\n", content)
# Project 7 Debug Version

filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    print("\n--- DOSYA İÇERİĞİ ---")
    print(content)
    print("--- DOSYA SONU ---\n")

except FileNotFoundError:
    print("❌ File not found!")
