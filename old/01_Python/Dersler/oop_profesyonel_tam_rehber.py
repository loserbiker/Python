"""
==========================================================
PYTHON NESNE YÖNELİMLİ PROGRAMLAMA (OOP) EĞİTİM SETİ
==========================================================

Bu dosya baştan sona OOP mantığını öğretmek için hazırlanmıştır.

İçerik:

1) Class Nedir?
2) Object (Nesne) Nedir?
3) __init__ Metodu
4) Instance Attribute vs Class Attribute
5) Metodlar
6) Encapsulation (Kapsülleme)
7) Inheritance (Kalıtım)
8) Polymorphism (Çok Biçimlilik)
9) Magic Methods
10) Küçük Proje Örneği

Tüm açıklamalar eğitim amaçlı detaylı yazılmıştır.
"""

# ==========================================================
# 1) CLASS NEDİR?
# ==========================================================

"""
Class (Sınıf), bir şablondur.

Gerçek hayattan örnek:
'Araba' bir class olabilir.
Ama kırmızı bir BMW gerçek bir nesnedir (object).

Class = Taslak
Object = Gerçek varlık
"""

class Insan:
    pass

# Nesne üretme
kisi1 = Insan()
kisi2 = Insan()

print("kisi1 tipi:", type(kisi1))
print("kisi2 tipi:", type(kisi2))


# ==========================================================
# 2) __init__ METODU
# ==========================================================

"""
__init__ metodu, nesne oluşturulurken otomatik çalışır.

self:
O an oluşturulan nesnenin kendisini temsil eder.
"""

class Araba:

    def __init__(self, marka, renk):
        self.marka = marka
        self.renk = renk

araba1 = Araba("BMW", "Kırmızı")
araba2 = Araba("Mercedes", "Siyah")

print(araba1.marka)
print(araba2.renk)


# ==========================================================
# 3) INSTANCE ATTRIBUTE vs CLASS ATTRIBUTE
# ==========================================================

"""
Instance attribute:
Her nesneye özel değişken.

Class attribute:
Tüm nesneler tarafından ortak kullanılan değişken.
"""

class Ogrenci:

    okul_adi = "Python Akademi"  # Class attribute

    def __init__(self, isim):
        self.isim = isim  # Instance attribute

o1 = Ogrenci("Ahmet")
o2 = Ogrenci("Ayşe")

print(o1.isim)
print(o2.okul_adi)


# ==========================================================
# 4) METOD NEDİR?
# ==========================================================

"""
Class içinde tanımlanan fonksiyonlara metod denir.
"""

class Kopek:

    def __init__(self, isim):
        self.isim = isim

    def havla(self):
        print(self.isim, "havladı!")

k = Kopek("Karabaş")
k.havla()


# ==========================================================
# 5) ENCAPSULATION (KAPSÜLLEME)
# ==========================================================

"""
Veriyi dış müdahaleden koruma mantığıdır.
Python'da '_' ve '__' ile yapılır.
"""

class BankaHesabi:

    def __init__(self, bakiye):
        self.__bakiye = bakiye  # Private değişken

    def para_yatir(self, miktar):
        self.__bakiye += miktar

    def bakiye_goster(self):
        return self.__bakiye

hesap = BankaHesabi(1000)
hesap.para_yatir(500)

print("Güncel bakiye:", hesap.bakiye_goster())


# ==========================================================
# 6) INHERITANCE (KALITIM)
# ==========================================================

"""
Bir class başka bir class'ın özelliklerini miras alabilir.
"""

class Hayvan:

    def konus(self):
        print("Hayvan ses çıkarıyor")

class Kedi(Hayvan):

    def konus(self):
        print("Miyav")

class Kopek2(Hayvan):

    def konus(self):
        print("Hav hav")

kedi = Kedi()
kopek = Kopek2()

kedi.konus()
kopek.konus()


# ==========================================================
# 7) POLYMORPHISM (ÇOK BİÇİMLİLİK)
# ==========================================================

"""
Aynı metod ismi, farklı davranış.
"""

def hayvan_konustur(hayvan):
    hayvan.konus()

hayvan_konustur(kedi)
hayvan_konustur(kopek)


# ==========================================================
# 8) MAGIC METHODS
# ==========================================================

"""
__str__ gibi özel metodlardır.
"""

class Kitap:

    def __init__(self, isim, yazar):
        self.isim = isim
        self.yazar = yazar

    def __str__(self):
        return f"{self.isim} - {self.yazar}"

kitap = Kitap("Python 101", "Can")
print(kitap)


# ==========================================================
# 9) KÜÇÜK PROJE ÖRNEĞİ - OYUNCU SİSTEMİ
# ==========================================================

class Oyuncu:

    def __init__(self, isim):
        self.isim = isim
        self.can = 100

    def hasar_al(self, miktar):
        self.can -= miktar

        if self.can <= 0:
            self.can = 0
            print(self.isim, "öldü!")
        else:
            print(self.isim, miktar, "hasar aldı.")
            print("Kalan can:", self.can)

    def saldir(self, rakip, hasar):
        print(self.isim, rakip.isim, "oyuncusuna saldırdı!")
        rakip.hasar_al(hasar)


# Oyuncular
o1 = Oyuncu("Can")
o2 = Oyuncu("Ali")

o1.saldir(o2, 30)
o2.saldir(o1, 50)
o1.saldir(o2, 80)


# ==========================================================
# GENEL ÖZET
# ==========================================================

"""
Bu dosyada öğrendiklerimiz:

✔ Class ve Object
✔ __init__ ve self
✔ Attribute türleri
✔ Metod mantığı
✔ Encapsulation
✔ Inheritance
✔ Polymorphism
✔ Magic Methods
✔ Basit oyun sistemi örneği

Bu dosya temel-orta seviye OOP bilgisi sağlar.

Bir sonraki aşama:
Gerçek bir mini oyun mimarisi kurmak olabilir.
"""