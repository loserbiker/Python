"""
INPUT VE TİP DÖNÜŞÜMÜ
"""

# input() her zaman string döndürür
isim = input("Adınız: ")
print("Merhaba", isim)

# ------------------------------
# String + Integer Hatası
# ------------------------------

yas = 27

# print("Yaş: " + yas)  ❌ HATA

print("Yaş:", yas)  # ✔ Doğru kullanım

# Eğer + kullanmak istersek:
print("Yaş: " + str(yas))

# ------------------------------
# Tip Dönüşümleri
# ------------------------------

sayi = int("10")
ondalik = float("3.14")
metin = str(100)

print(type(sayi))
print(type(ondalik))
print(type(metin))
