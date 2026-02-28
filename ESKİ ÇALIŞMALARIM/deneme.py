import time
import string
import random

can = 3
puan = 0

while can > 0:
    harf = random.choice(string.ascii_lowercase)
    print("Harf:", harf)
    baslangic = time.time()
    cevap = input("Seçilen harf:")
    bitis = time.time()

    if cevap == harf:
        print(f"Doğru bildin. Tepki süren: {bitis - baslangic:.2f} saniye")
        puan += 1
    else:
        print("Yanlış bildin!")
        can -= 1
    print(f"Can: {can} | Puan: {puan}\n")

