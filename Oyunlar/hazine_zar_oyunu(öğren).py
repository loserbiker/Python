# Kullanıcıdan isim alıyoruz
name = input("İsminiz: ")

# random modülünü import ediyoruz
import random

# 1–6 arasında zar atıyoruz
zar = random.randint(1,6)
print(name, "zarı attı: ", zar)

# Ödül listesi oluşturuyoruz
odul = ["Altın", "Elmas", "Boş Sandık"]

# if kullanmadan zar >= 5 ise ödül, değilse "Maalesef hazine yok" vermek için
# random.choices ve weights kullanıyoruz
# True = 1, False = 0 olduğu için sadece zar >= 5 ise ödül seçilebilir
sonuc = random.choices(
    ["Altın", "Elmas", "Maalesef hazine yok"], # seçim yapılacak öğeler
    weights=[zar >= 5, zar >= 5, zar < 5],     # ağırlıklar
    k=1                                       # kaç seçim yapılacak
)

# Seçilen sonucu ekrana yazdırıyoruz
print("Tebrikler! Hazinen: ", sonuc[0])

#if else ile yaparsak
## sonuc = random.choice(["Altın", "Elmas"]) if zar >= 5 else "Maalesef hazine yok"
#                         Altın için : if zar >= 5 
#                         Elmas için : else "Maalesef hazine yok"                           

