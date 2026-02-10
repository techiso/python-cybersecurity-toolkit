import random

# Kelime listesi
kelimeler = [
    'python', 'bilgisayar', 'programlama', 'oyun', 'klavye',
    'fare', 'ekran', 'internet', 'yazilim', 'kod',
    'algoritma', 'veri', 'fonksiyon', 'degisken', 'dongu',
    'liste', 'sozluk', 'string', 'sayi', 'proje'
]

# Adam asmaca çizimleri
asmaca_asamalari = [
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

def kelime_sec():
    return random.choice(kelimeler).upper()

def oyunu_goster(tahmin_edilen, yanlis_tahminler, kelime):
    print("\n" + "="*50)
    print(asmaca_asamalari[len(yanlis_tahminler)])
    print("="*50)
    
    # Kelimeyi göster
    gosterim = ""
    for harf in kelime:
        if harf in tahmin_edilen:
            gosterim += harf + " "
        else:
            gosterim += "_ "
    
    print("\nKelime: " + gosterim)
    print(f"\nYanlış tahminler ({len(yanlis_tahminler)}/6): {', '.join(yanlis_tahminler)}")
    print("="*50)

def oyun():
    print("\n** ADAM ASMACA OYUNUNA HOŞ GELDİNİZ **\n")
    
    kelime = kelime_sec()
    tahmin_edilen = set()
    yanlis_tahminler = []
    max_yanlis = 6
    
    while len(yanlis_tahminler) < max_yanlis:
        oyunu_goster(tahmin_edilen, yanlis_tahminler, kelime)
        
        # Kazanma kontrolü
        if all(harf in tahmin_edilen for harf in kelime):
            print("\n🎉 TEBRİKLER! KAZANDINIZ! 🎉")
            print(f"Kelime: {kelime}")
            break
        
        # Tahmin al
        tahmin = input("\nBir harf tahmin edin: ").upper()
        
        # Geçerlilik kontrolü
        if len(tahmin) != 1 or not tahmin.isalpha():
            print("❌ Lütfen sadece bir harf girin!")
            continue
        
        if tahmin in tahmin_edilen or tahmin in yanlis_tahminler:
            print("⚠️  Bu harfi zaten denediniz!")
            continue
        
        # Tahmin kontrolü
        if tahmin in kelime:
            tahmin_edilen.add(tahmin)
            print("✅ Doğru tahmin!")
        else:
            yanlis_tahminler.append(tahmin)
            print("❌ Yanlış tahmin!")
    
    # Kaybetme durumu
    if len(yanlis_tahminler) >= max_yanlis:
        oyunu_goster(tahmin_edilen, yanlis_tahminler, kelime)
        print("\n💀 OYUN BİTTİ! KAYBETTİNİZ! 💀")
        print(f"Kelime şuydu: {kelime}")
    
    # Tekrar oyna
    print("\n" + "="*50)
    tekrar = input("\nTekrar oynamak ister misiniz? (e/h): ").lower()
    if tekrar == 'e':
        oyun()
    else:
        print("\nOynadığınız için teşekkürler! Görüşmek üzere! 👋")

# Oyunu başlat
if __name__ == "_main_":
    oyun()
