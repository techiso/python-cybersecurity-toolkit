# Pygame başlatma
pygame.init()

# Renkler
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)

# Ekran boyutları
GENISLIK = 600
YUKSEKLIK = 400
BLOK_BOYUTU = 20

# Ekranı oluştur
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption('Yılan Oyunu')

# Saat
saat = pygame.time.Clock()
FPS = 10

# Font
font = pygame.font.SysFont('arial', 25)

def skor_goster(skor):
    metin = font.render(f'Skor: {skor}', True, BEYAZ)
    ekran.blit(metin, [10, 10])

def yilan_ciz(blok_boyutu, yilan_listesi):
    for blok in yilan_listesi:
        pygame.draw.rect(ekran, YESIL, [blok[0], blok[1], blok_boyutu, blok_boyutu])

def mesaj_goster(msg, renk):
    metin = font.render(msg, True, renk)
    ekran.blit(metin, [GENISLIK/6, YUKSEKLIK/3])

def oyun_dongusu():
    oyun_bitti = False
    oyun_kapandi = False

    # Yılanın başlangıç konumu
    x1 = GENISLIK / 2
    y1 = YUKSEKLIK / 2

    x1_degisim = 0
    y1_degisim = 0

    yilan_listesi = []
    yilan_uzunlugu = 1

    # Yem konumu
    yem_x = round(random.randrange(0, GENISLIK - BLOK_BOYUTU) / 20.0) * 20.0
    yem_y = round(random.randrange(0, YUKSEKLIK - BLOK_BOYUTU) / 20.0) * 20.0

    while not oyun_kapandi:

        while oyun_bitti:
            ekran.fill(SIYAH)
            mesaj_goster('Kaybettiniz! Q-Çık C-Tekrar', KIRMIZI)
            skor_goster(yilan_uzunlugu - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        oyun_kapandi = True
                        oyun_bitti = False
                    if event.key == pygame.K_c:
                        oyun_dongusu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_kapandi = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_degisim == 0:
                    x1_degisim = -BLOK_BOYUTU
                    y1_degisim = 0
                elif event.key == pygame.K_RIGHT and x1_degisim == 0:
                    x1_degisim = BLOK_BOYUTU
                    y1_degisim = 0
                elif event.key == pygame.K_UP and y1_degisim == 0:
                    y1_degisim = -BLOK_BOYUTU
                    x1_degisim = 0
                elif event.key == pygame.K_DOWN and y1_degisim == 0:
                    y1_degisim = BLOK_BOYUTU
                    x1_degisim = 0

        # Duvara çarpma kontrolü
        if x1 >= GENISLIK or x1 < 0 or y1 >= YUKSEKLIK or y1 < 0:
            oyun_bitti = True

        x1 += x1_degisim
        y1 += y1_degisim
        ekran.fill(SIYAH)

        # Yem çizimi
        pygame.draw.rect(ekran, KIRMIZI, [yem_x, yem_y, BLOK_BOYUTU, BLOK_BOYUTU])

        yilan_basi = []
        yilan_basi.append(x1)
        yilan_basi.append(y1)
        yilan_listesi.append(yilan_basi)

        if len(yilan_listesi) > yilan_uzunlugu:
            del yilan_listesi[0]

        # Kendine çarpma kontrolü
        for blok in yilan_listesi[:-1]:
            if blok == yilan_basi:
                oyun_bitti = True

        yilan_ciz(BLOK_BOYUTU, yilan_listesi)
        skor_goster(yilan_uzunlugu - 1)

        pygame.display.update()

        # Yem yeme kontrolü
        if x1 == yem_x and y1 == yem_y:
            yem_x = round(random.randrange(0, GENISLIK - BLOK_BOYUTU) / 20.0) * 20.0
            yem_y = round(random.randrange(0, YUKSEKLIK - BLOK_BOYUTU) / 20.0) * 20.0
            yilan_uzunlugu += 1

        saat.tick(FPS)

    pygame.quit()
    sys.exit()

# Oyunu başlat
oyun_dongusu()
