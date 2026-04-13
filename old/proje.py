import random
print (input("OYUNA HOŞ GELDİN! BAŞLAMAK İÇİN TIKLA"))
gizli_sayi = random.randint(1,10)
can = 3

while can > 0:
    tahmin = int(input("Tahmin Girin: "))

    if tahmin == gizli_sayi:
        print("Kazandın!")
        break
    elif tahmin < gizli_sayi:
        can -= 1
        print(f"Daha Büyük Tahmin! Kalan Can: {can}")
        
    elif tahmin > gizli_sayi:
        can -= 1
        print(f"Daha Küçük Tahmin! Kalan Can: {can}")

if can == 0:
        print(f"OYUN BİTTİ! GİZLİ SAYI: {gizli_sayi}")