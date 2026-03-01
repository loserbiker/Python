"""
=========================================================
OOP - RETURN KULLANARAK OYUNCU SİSTEMİ
=========================================================

Bu dosyada şunları göreceğiz:

1) print yerine return kullanımı
2) Metodların veri üretmesi
3) Yazdırma kontrolünün dışarı bırakılması
4) Daha profesyonel class yapısı

Önemli prensip:
Class veri üretir.
Ana program yazdırır.
"""

# ==========================================================
# OYUNCU CLASS
# ==========================================================

class Oyuncu:
    
    def __init__(self, isim, guc):
        """
        Constructor (kurucu metod).
        Nesne oluşturulduğunda otomatik çalışır.
        """
        self.isim = isim
        self.can = 100
        self.guc = guc


    # ------------------------------------------------------
    # HASAR ALMA METODU
    # ------------------------------------------------------

    def hasar_al(self, miktar):
        """
        Oyuncunun canını azaltır.
        print yapmaz.
        Sadece sonucu return eder.
        """

        self.can -= miktar

        # Eğer can 0'ın altına düşerse sıfıra sabitleriz
        if self.can <= 0:
            self.can = 0
            return f"{self.isim} öldü!"
        
        # Eğer oyuncu yaşıyorsa mesaj döndürür
        return f"{self.isim} {miktar} hasar aldı. Kalan can: {self.can}"


    # ------------------------------------------------------
    # SALDIRI METODU
    # ------------------------------------------------------

    def saldir(self, rakip):
        """
        Rakibe saldırır.
        print etmez.
        Hasar sonucunu return eder.
        """

        # Rakibe hasar aldırıyoruz
        sonuc_mesaji = rakip.hasar_al(self.guc)

        # Saldırı mesajı oluşturuyoruz
        return f"{self.isim}, {rakip.isim} oyuncusuna saldırdı!\n{sonuc_mesaji}"


    # ------------------------------------------------------
    # KALAN CAN METODU
    # ------------------------------------------------------

    def kalan_can(self):
        """
        Oyuncunun mevcut canını döndürür.
        Parametre almaz.
        Çünkü oyuncu kendi canını zaten bilir.
        """

        return self.can


# ==========================================================
# OYUNUN DIŞ KISMI (ANA PROGRAM)
# ==========================================================

"""
Burada artık print işlemleri class içinde değil.
Dışarıda yapılıyor.

Bu çok önemli bir mimari farktır.
"""

o1 = Oyuncu("Can", 30)
o2 = Oyuncu("Ali", 10)

# Saldırı sonuçlarını yazdırıyoruz
print(o1.saldir(o2))
print(o2.saldir(o1))

# Kalan canları kontrol ediyoruz
print("Can'ın canı:", o1.kalan_can())
print("Ali'nin canı:", o2.kalan_can())

# Artık kontrol yapabiliyoruz
if o1.kalan_can() == 0:
    print("Can oyunu kaybetti!")

if o2.kalan_can() == 0:
    print("Ali oyunu kaybetti!")