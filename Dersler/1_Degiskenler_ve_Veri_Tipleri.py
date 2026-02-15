"""
==============================
DEĞİŞKENLER (VARIABLES) EĞİTİMİ
==============================

Değişkenler, veri saklamak için kullanılan isimlendirilmiş hafıza alanlarıdır.
Python, dinamik tipli bir dildir; yani değişken oluştururken veri tipini belirtmeye gerek yoktur.
"""

# ------------------------------
# TEMEL VERİ TİPLERİ
# ------------------------------

# Tam sayı (integer)
x = 7

# Metin/string
y = "python"

# Ondalıklı sayı (float)
z = 0.54

# Karmaşık sayı (complex)
comp = 2j

# type() fonksiyonu değişkenin veri tipini gösterir
print(type(x))    # <class 'int'>
print(type(y))    # <class 'str'>
print(type(z))    # <class 'float'>
print(type(comp)) # <class 'complex'>

# ------------------------------
# CASE SENSITIVE (BÜYÜK-KÜÇÜK HARF DUYARLILIĞI)
# ------------------------------

# Python değişken isimlerinde büyük/küçük harf farkı vardır
name = "hello"
Name = "hello"

# name ve Name iki farklı değişkendir
print(name)  # hello
print(Name)  # hello

# ------------------------------
# DEĞİŞKEN KURALLARI
# ------------------------------

"""
1- Değişken isimleri sayı ile başlayamaz
2- Sadece harf, sayı ve alt çizgi (_) içerebilir
3- Büyük/küçük harfe duyarlıdır
4- Python anahtar kelimeleri değişken adı olarak kullanılamaz
"""

# Örnek:
_isim = "Can"   # alt çizgi ile başlayan değişken geçerlidir
isim = "Can"    # normal değişken

print(_isim)  # Can
print(isim)   # Can

# ------------------------------
# ÇOKLU DEĞER ATAMA
# ------------------------------

# Tek satırda birden fazla değişkene değer atayabiliriz
a, b, c = "Apple", "Banana", "Grape"
print(a, b, c)  # Apple Banana Grape

# ------------------------------
# VARIABLE UNPACKING (LİSTEDEKİ DEĞERLERİ DEĞİŞKENLERE ATAMA)
# ------------------------------

colors = ["white", "black", "orange", "purple", "blue"]

# Liste elemanlarını tek tek değişkenlere aktarabiliriz
a, b, c, d, e = colors
print(a, b, c, d, e)  # white black orange purple blue

# NOT:
# Unpacking yaparken değişken sayısı ile listenin uzunluğu eşleşmelidir.
# Aksi takdirde hata alırsınız.
