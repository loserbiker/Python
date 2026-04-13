# ==================================================
# FUNCTIONS WORKSHOP
# Verimli / Kısa / Referanslık Sürüm
# ==================================================

# --------------------------------------------------
# 1) Fonksiyon Nedir?
# --------------------------------------------------
# Fonksiyon, belirli bir işi yapan kod bloğudur.
# Amaç:
# - tekrar eden kodu azaltmak
# - kodu düzenli yazmak
# - büyük işi küçük parçalara bölmek
# - aynı işlemi tekrar kullanabilmek


# --------------------------------------------------
# 2) Temel Kullanım
# --------------------------------------------------
def selam_ver():
    print("Merhaba")

selam_ver()


# --------------------------------------------------
# 3) Parametre ve Argüman
# --------------------------------------------------
# Parametre: fonksiyon tanımındaki değişken
# Argüman: fonksiyon çağrılırken verilen gerçek değer

def selam_ver_isimle(isim):
    print("Merhaba", isim)

selam_ver_isimle("Can")
selam_ver_isimle("Ahmet")


# --------------------------------------------------
# 4) print vs return
# --------------------------------------------------
# print:
# - ekrana yazar
#
# return:
# - sonucu geri döndürür
# - başka yerde kullanılabilir

def topla_yaz(a, b):
    print(a + b)

def topla_dondur(a, b):
    return a + b

x = topla_yaz(2, 3)      # ekrana 5 basar, x = None olur
y = topla_dondur(2, 3)   # y = 5 olur

print(x)
print(y)


# --------------------------------------------------
# 5) return ile Değer Döndürme
# --------------------------------------------------
def topla(a, b):
    return a + b

sonuc = topla(3, 5)
print(sonuc)


# --------------------------------------------------
# 6) True / False Döndüren Fonksiyonlar
# --------------------------------------------------
# Bir ifade zaten True / False üretiyorsa direkt return edilebilir.

def cift_mi(sayi):
    return sayi % 2 == 0

def buyuk_mu(sayi):
    return sayi > 10

def bos_mu(metin):
    return metin == ""

print(cift_mi(4))
print(cift_mi(7))

print(buyuk_mu(15))
print(buyuk_mu(3))

print(bos_mu(""))
print(bos_mu("Python"))


# --------------------------------------------------
# 7) Karar Veren Fonksiyonlar
# --------------------------------------------------
def not_durumu(notu):
    if notu >= 50:
        return "Geçti"
    else:
        return "Kaldı"

print(not_durumu(80))
print(not_durumu(30))


def harf_notu(puan):
    if puan >= 85:
        return "A"
    elif puan >= 70:
        return "B"
    elif puan >= 50:
        return "C"
    else:
        return "F"

print(harf_notu(90))
print(harf_notu(72))
print(harf_notu(40))


# --------------------------------------------------
# 8) Birden Fazla Parametre
# --------------------------------------------------
def giris_hakki(yas, kart_var_mi):
    if yas >= 18 and kart_var_mi:
        return "Girebilir"
    else:
        return "Giremez"

print(giris_hakki(20, True))
print(giris_hakki(20, False))
print(giris_hakki(16, True))


# --------------------------------------------------
# 9) Fonksiyon Sonucunu if İçinde Kullanmak
# --------------------------------------------------
def uygun_mu(yas):
    return yas >= 18

if uygun_mu(20):
    print("Girebilir")

if uygun_mu(15):
    print("Girebilir")
else:
    print("Giremez")


# --------------------------------------------------
# 10) Bir Fonksiyonun Başka Fonksiyonu Kullanması
# --------------------------------------------------
def gecer_mi(notu):
    return notu >= 50

def sonuc_yaz(notu):
    if gecer_mi(notu):
        return "Geçti"
    else:
        return "Kaldı"

print(sonuc_yaz(80))
print(sonuc_yaz(30))


# --------------------------------------------------
# 11) Kritik Notlar
# --------------------------------------------------
# 1. Fonksiyon adı yaptığı işi anlatmalı.
# 2. Parametre = tanım içindeki değişken.
# 3. Argüman = çağırırken verdiğimiz gerçek değer.
# 4. print sadece gösterir.
# 5. return sonucu geri verir.
# 6. return edilen değer değişkene atanabilir.
# 7. Bazı yollarda return var, bazılarında yoksa return olmayan yol sonunda None oluşur.
# 8. Bir ifade zaten boolean üretiyorsa direkt return edilebilir.
#
# Örnek:
# return sayi > 10
# return sayi % 2 == 0
# return metin == ""


# --------------------------------------------------
# 12) Seçilmiş Alıştırmalar
# --------------------------------------------------

# Soru 1
# Bir fonksiyon yaz:
# def pozitif_mi(sayi):
# sayı 0'dan büyükse True, değilse False dönsün.

# Soru 2
# Bir fonksiyon yaz:
# def yas_grubu(yas):
# 18 ve üstüne "Yetişkin", altına "Çocuk" dönsün.

# Soru 3
# Bir fonksiyon yaz:
# def indirimli_fiyat(fiyat):
# fiyat 100 ve üstüyse %10 indirimli halini döndürsün,
# değilse aynı fiyatı döndürsün.

# Soru 4
# Bir fonksiyon yaz:
# def mesaj_ver(sayi):
# sayı çiftse "Çift", tekse "Tek" döndürsün.
# İçeride cift_mi(sayi) fonksiyonunu kullan.