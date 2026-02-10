import random

kelimeler = ['PYTHON', 'BILGISAYAR', 'PROGRAMLAMA', 'OYUN', 'KLAVYE', 'INTERNET', 'KOD', 'ALGORITMA']

asmaca = [
"""
   ------
   |    |
   |
   |
   |
   |
--------
""",
"""
   ------
   |    |
   |    O
   |
   |
   |
--------
""",
"""
   ------
   |    |
   |    O
   |    |
   |
   |
--------
""",
"""
   ------
   |    |
   |    O
   |   /|
   |
   |
--------
""",
"""
   ------
   |    |
   |    O
   |   /|\\
   |
   |
--------
""",
"""
   ------
   |    |
   |    O
   |   /|\\
   |   /
   |
--------
""",
"""
   ------
   |    |
   |    O
   |   /|\\
   |   / \\
   |
--------
"""
]

print("\n** ADAM ASMACA OYUNU **\n")

kelime = random.choice(kelimeler)
tahmin_edilen = []
yanlis = []

while len(yanlis) < 6:
    print(asmaca[len(yanlis)])
    
    kelime_goster = ""
    for harf in kelime:
        if harf in tahmin_edilen:
            kelime_goster += harf + " "
        else:
            kelime_goster += "_ "
    
    print("Kelime:", kelime_goster)
    print("Yanlis tahminler:", ", ".join(yanlis))
    
    if "_" not in kelime_goster:
        print("\nTEBRIKLER! KAZANDINIZ!")
        print("Kelime:", kelime)
        break
    
    harf = input("\nBir harf tahmin edin: ").upper()
    
    if len(harf) != 1:
        print("Sadece bir harf girin!")
        continue
    
    if harf in tahmin_edilen or harf in yanlis:
        print("Bu harfi zaten denediniz!")
        continue
    
    if harf in kelime:
        tahmin_edilen.append(harf)
        print("Dogru!")
    else:
        yanlis.append(harf)
        print("Yanlis!")

if len(yanlis) >= 6:
    print(asmaca[6])
    print("\nKAYBETTINIZ!")
    print("Kelime:", kelime)
