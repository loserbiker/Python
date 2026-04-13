"""
==========================================================
PYTHON OOP - RETURN KAVRAMI DETAYLI ANLATIMLI EĞİTİM
==========================================================

Bu dosyada şunları öğreneceğiz:

1) print ile return arasındaki fark
2) Fonksiyonlarda return mantığı
3) OOP içinde return kullanımı
4) Oyuncu sistemi üzerinde profesyonel yapı
5) Veri üretmek vs veri yazdırmak farkı

Amaç:
Metodların neden return kullanması gerektiğini
gerçek bir oyun sistemi üzerinden anlamak.
"""

# ==========================================================
# 1) PRINT vs RETURN FARKI
# ==========================================================

"""
print():
Sadece ekrana yazı yazdırır.
Değeri dışarıya göndermez.

return:
Fonksiyonun içindeki sonucu dışarıya gönderir.
Bu değer başka bir değişkene atanabilir,
başka bir yerde kullanılabilir.
"""

# ---- PRINT ÖRNEĞİ ----

def kare_print(x):
    print("Sonuç:", x * x)

sonuc1 = kare_print(5)

print("kare_print fonksiyonundan gelen değer:", sonuc1)

"""
Çıktı:
Sonuç: 25
kare_print fonksiyonundan gelen değer: None

Neden None?

Çünkü print sadece yazdırdı.
Fonksiyon geriye bir değer DÖNDÜRMEDİ.
Bu yüzden varsayılan olarak None döndü.
"""


# ---- RETURN ÖRNEĞİ ----

def kare_return(x):
    return x * x

sonuc2 = kare_return(5)

print("kare_return fonksiyonundan gelen değer:", sonuc2)

"""
Burada 25 değeri gerçekten fonksiyondan çıktı
ve sonuc2 değişkenine atandı.

İşte return budur:
Değeri dış dünyaya vermek.
"""


# ==========================================================
# 2) OOP İÇİNDE RETURN NEDEN ÖNEMLİ?
# ==========================================================

"""
Profesyonel yazılımda bir class:

- Veriyi yönetir
- Davranışı içerir
- Ama kullanıcıya zorla print yapmaz

Çünkü yazdırma kararı dışarıya aittir.

Bu prensip:
Veri üret, kontrolü dışarı bırak.
"""


# ==========================================================
# 3) OYUNCU CLASS - PROFESYONEL TASARIM
# ==========================================================

class Oyuncu:
    """
    Bu class bir oyuncu nesnesi oluşturur.

    Her oyuncunun:
    - isim
    - can
    - guc

    özellikleri vardır.
    """

    def __init__(self, isim, guc):
        """
        Constructor metodudur.
        Nesne oluşturulurken otomatik çalışır.
        """

        self.isim = isim
        self.can = 100
        self.guc = guc

    # ------------------------------------------------------

    def hayatta_mi(self):
        """
        Oyuncunun yaşayıp yaşamadığını kontrol eder.

        return True  -> oyuncu yaşıyor
        return False -> oyuncu ölü
        """

        return self.can > 0

    # ------------------------------------------------------

    def hasar_al(self, miktar):
        """
        Oyuncunun canını azaltır.

        Bu metod print yapmaz.
        Sadece veriyi değiştirir.
        """

        self.can -= miktar

        if self.can < 0:
            self.can = 0

    # ------------------------------------------------------

    def saldir(self, rakip):
        """
        Rakip oyuncuya saldırır.

        ÖNEMLİ:
        Bu metod sonucu print etmez.
        return ile mesaj döndürür.
        """

        # Eğer oyuncu ölü ise saldıramaz
        if not self.hayatta_mi():
            return f"{self.isim} ölü olduğu için saldıramaz!"

        # Rakip hasar alır
        rakip.hasar_al(self.guc)

        return f"{self.isim}, {rakip.isim} oyuncusuna {self.guc} hasar verdi!"

    # ------------------------------------------------------

    def can_goster(self):
        """
        Oyuncunun mevcut canını döndürür.

        Neden print değil return?

        Çünkü:
        - Belki oyunu bitirme kontrolü yapacağız
        - Belki UI sistemine göndereceğiz
        - Belki veritabanına yazacağız

        Veri üretmek class'ın görevidir.
        Yazdırmak değil.
        """

        return self.can


# ==========================================================
# 4) SİSTEMİN KULLANIMI
# ==========================================================

o1 = Oyuncu("Can", 30)
o2 = Oyuncu("Ali", 15)

print(o1.saldir(o2))
print("Ali'nin kalan canı:", o2.can_goster())

print(o2.saldir(o1))
print("Can'ın kalan canı:", o1.can_goster())


# ==========================================================
# 5) RETURN NEDEN DAHA PROFESYONEL?
# ==========================================================

"""
Şimdi düşün:

Eğer can_goster() print yapsaydı,
şu kontrolü yapamazdık:

if o1.can_goster() <= 0:
    print("Oyun bitti!")

Ama return sayesinde bunu yapabiliyoruz.

Yani return:
Sistemi büyütmemizi sağlar.

print:
Sistemi sabit bırakır.
"""


# ==========================================================
# GENEL ÖZET
# ==========================================================

"""
Bugün öğrendiğin en kritik konu:

print = gösterir
return = gönderir

OOP'de doğru yaklaşım:

✔ Metod veri üretir
✔ Veri return edilir
✔ Yazdırma ve kontrol dışarı yapılır

Bu mimari seni:
"kod yazan biri" seviyesinden
"sistem kuran biri" seviyesine taşır.
"""