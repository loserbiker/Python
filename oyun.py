import time
import random

skor = 0
alfabe_listesi = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
          "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z"]
time_limit = 1.0
tebrik_mesajlari = ["İyi Gidiyorsun!" , "Böyle Devam Et!" , "Hızına Kimse Yetişemez!" , "Doğru Bildin!"]
while True:

    target = random.choice(alfabe_listesi)
    tebrik = random.choice(tebrik_mesajlari)

    print("Seçilen harf:" , target)

    start_time = time.time()
    kullanıcı_secimi = input("Harf Seç:").lower()
    end_time = time.time()

    reaction_time = end_time - start_time

    if kullanıcı_secimi != target:
        print("Game Over!")
        print("Toplam Skorun:" , skor)
        print("Süren:" , round (reaction_time , 3))
        break

    if reaction_time > time_limit:
        print("Geç Kaldın!")
        print("Toplam Skorun:" , skor)
        print("Süren:" , round (reaction_time , 3))
        break

    else:
        skor += 1
        time_limit *= 0.95
        print(tebrik , "Skorun:" , skor , "Tepki Süren:" , round(reaction_time, 3))