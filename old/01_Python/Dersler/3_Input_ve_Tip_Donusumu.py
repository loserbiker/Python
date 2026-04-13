"""
====================================
INPUT VE TIP DÖNÜŞÜMÜ EĞİTİMİ
====================================

Python'da kullanıcıdan veri almak için input() fonksiyonu kullanılır.
Ancak input() her zaman string (metin) tipinde veri döndürür.
Bu yüzden sayısal işlemler yapmak için tip dönüşümü gerekir.
"""

# ------------------------------
# 1. INPUT KULLANIMI
# ------------------------------

# input() fonksiyonu kullanıcıdan veri alır ve string olarak döndürür
isim = input("Adınız: ")  # Kullanıcıdan isim alır
print("Merhaba", isim)    # Merhaba + kullanıcıdan alınan isim

# ------------------------------
# 2. STRING + INTEGER HATASI
# ------------------------------

yas = 27

# print("Yaş: " + yas)  ❌ Bu hata verir çünkü string + integer birleştirilemez

# Doğru kullanım 1: virgül ile yazdırma
print("Yaş:", yas)  # ✔ Çıktı: Yaş: 27

# Doğru kullanım 2: integer değeri stringe çevirerek birleştirme
print("Yaş: " + str(yas))  # ✔ Çıktı: Yaş: 27

# NOT:
# - "," virgül ile yazdırırsak Python otomatik araya boşluk koyar ve tip farkı sorun olmaz
# - "+" ile birleştirmek istersek tüm verilerin string olması gerekir

# ------------------------------
# 3. TIP DÖNÜŞÜMLERİ
# ------------------------------

# int() -> sayısal tam sayı dönüşümü
sayi = int("10")           # String "10" integer 10'a dönüşür
print(sayi, type(sayi))    # 10 <class 'int'>

# float() -> ondalıklı sayı dönüşümü
ondalik = float("3.14")     # String "3.14" float 3.14'e dönüşür
print(ondalik, type(ondalik))  # 3.14 <class 'float'>

# str() -> stringe dönüşüm
metin = str(100)            # Integer 100 string "100" olur
print(metin, type(metin))   # 100 <class 'str'>
