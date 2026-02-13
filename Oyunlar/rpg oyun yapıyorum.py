import random

# Kullanıcıdan isim al
karakter = input("İsim girin:")

# Zar at
zar1 = random.randint(1,6)
zar2 = random.randint(1,6)
toplam = zar1 + zar2
print("Toplam zar:", toplam)

if toplam >= 7:
    print("Kazandın")
else:
    print("Kaybettin")

# Hazine toplama
puan = 0
hazine_listesi = ["Altın", "Gümüş", "Elmas"]

# Rastgele hazine seç ve değişkene ata
kazanan_hazine = random.choice(hazine_listesi)
print("Kazanılan Hazine:", kazanan_hazine)

# Puan güncelle
if kazanan_hazine == "Altın":
    puan += 10
elif kazanan_hazine == "Gümüş":
    puan += 5
else:
    puan += 20

print("Toplam Puan:", puan)