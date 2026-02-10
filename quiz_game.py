print("🎮 Mini Quiz Oyununa Hoş Geldin!")
print("--------------------------------")

puan = 0

# Soru 1
cevap1 = input("1) Python hangi yılda çıktı? \nA) 1991\nB) 2005\nC) 2015\nCevap: ")

if cevap1.upper() == "A":
    print("✅ Doğru!")
    puan += 1
else:
    print("❌ Yanlış! Doğru cevap: A")

print()

# Soru 2
cevap2 = input("2) Python'da ekrana yazdırma komutu hangisi? \nA) echo\nB) print\nC) write\nCevap: ")

if cevap2.upper() == "B":
    print("✅ Doğru!")
    puan += 1
else:
    print("❌ Yanlış! Doğru cevap: B")

print()

# Soru 3
cevap3 = input("3) Siber güvenlikte en çok kullanılan dil hangilerinden biridir? \nA) Python\nB) Paint\nC) Excel\nCevap: ")

if cevap3.upper() == "A":
    print("✅ Doğru!")
    puan += 1
else:
    print("❌ Yanlış! Doğru cevap: A")

print()

# Sonuç
print("--------------------------------")
print("🎉 Quiz Bitti!")
print("Toplam Puanın:", puan, "/ 3")

if puan == 3:
    print("🔥 Mükemmelsin!")
elif puan == 2:
    print("👍 Çok iyi gidiyorsun!")
else:
    print("💪 Daha çok pratik yapacağız!")
