import random
import time
import os

score = 0
base_time = 2.0
min_time = 0.4
tur = 1
combo = 0

tuslar = ["w" , "a" , "s" , "d"]

tus_atmasi = {
          "w" : "Yukarı",
          "a" : "Sola",
          "s" : "Aşağı",
          "d" : "Sağa"
}                                 

def sure_hesapla(score):            
    sure = base_time - (score * 0.05)
    if sure <= min_time:
        return min_time
    else:
        return sure

print ("AI REFLEX")
print("-" * 25)
input("BAŞLAMAK İÇİN HERHANGİ BİR TUŞA BAS")

while True:
    #os.system("cls") #Windows için oyunu sıfırlamak amaçlı kullanılır
    os.system("clear") #Mac ve Linux için kullanılır

    print ("Tur:" , tur , "| Skor:" , score)
    
    secilen_tus = random.choice(tuslar)
    print("Yön:" , tus_atmasi[secilen_tus])

    izinli_sure = sure_hesapla(score)
    print("Süren:", round(izinli_sure, 2))

    baslangic = time.time()

    cevap = input("Tuşa Bas: ")

    bitis = time.time()
    gecen_sure = bitis - baslangic

    if gecen_sure > izinli_sure:
        print("Geç kaldın! Oyun bitti!")
        print("Final Skorun:" , score)
        break
    
    if cevap == secilen_tus:
        print("Doğru")
        score += 1
        tur += 1
        
        #COMBO BLOĞU
        if gecen_sure <= izinli_sure * 0.5:
            combo += 1
            print("COMBO:" , combo)
        else:
            combo = 0

        if combo >= 3:
            print("🔥 FAST COMBO 🔥")

    else:
        print("Yanlış! Oyun Bitti!")
        print("Final Skorun:" , score)
        break
    

    print("Geçen Süre:" , round(gecen_sure, 2))
