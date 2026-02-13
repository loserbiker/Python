"""
DEĞİŞKENLER (VARIABLES)

Değişkenler veri saklamak için kullanılan isimlendirilmiş hafıza alanlarıdır.
Python dinamik tipli bir dildir. Veri tipini ayrıca belirtmemize gerek yoktur.
"""

# ------------------------------
# Temel Veri Tipleri
# ------------------------------

x = 7              # int (tam sayı)
y = "python"       # str (metin)
z = 0.54           # float (ondalıklı sayı)
comp = 2j          # complex (karmaşık sayı)

print(type(x))
print(type(y))
print(type(z))
print(type(comp))

# ------------------------------
# Case Sensitive (Büyük-Küçük Harf Duyarlılığı)
# ------------------------------

name = "hello"
Name = "hello"

# Bu iki değişken farklıdır.

# ------------------------------
# Değişken Kuralları
# ------------------------------

"""
1- Sayı ile başlayamaz
2- Sadece harf, sayı ve _ içerebilir
3- Büyük-küçük harfe duyarlıdır
4- Python anahtar kelimesi olamaz
"""

_isim = "Can"
isim = "Can"

print(_isim)
print(isim)

# ------------------------------
# Çoklu Değer Atama
# ------------------------------

a, b, c = "Apple", "Banana", "Grape"
print(a, b, c)

# ------------------------------
# Variable Unpacking
# ------------------------------

colors = ["white", "black", "orange", "purple", "blue"]

a, b, c, d, e = colors
print(a, b, c, d, e)
