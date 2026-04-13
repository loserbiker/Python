####################### GAME PROTOTYPE V1 (SWIPE GAME) ############################
import random


print (input("OYUNA HOŞ GELDİN! BAŞLAMAK İÇİN TIKLA"))


can = 0
skor = 0
combo = 0

yonler = ["w" , "a" , "s" , "d"]

while True:
    yon = random.choice(yonler)
    print(f"Harf: {yon}")
    secilen_harf = input("Rastgele Harf: " )

    if yon == secilen_harf:
        print("Kazandın")
    else:
        print(f"Kaybettin! Seçilen harf: {yon}")
        break