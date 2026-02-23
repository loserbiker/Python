
# ==========================================================
# OYUNCU CLASS
# ==========================================================

class Oyuncu:
    
    def __init__(self, isim, guc):
        self.isim = isim
        self.can = 100
        self.guc = guc


    # ------------------------------------------------------
    # HASAR ALMA METODU
    # ------------------------------------------------------

    def hasar_al(self, miktar):

        self.can -= miktar

        if self.can <= 0:
            self.can = 0
            return f"{self.isim} öldü!"
        
        return f"{self.isim} {miktar} hasar aldı. Kalan can: {self.can}"


    # ------------------------------------------------------
    # SALDIRI METODU
    # ------------------------------------------------------

    def saldir(self, rakip):

        sonuc_mesaji = rakip.hasar_al(self.guc)

        return f"{self.isim}, {rakip.isim} oyuncusuna saldırdı!\n{sonuc_mesaji}"


    # ------------------------------------------------------
    # KALAN CAN METODU
    # ------------------------------------------------------

    def kalan_can(self):
        return self.can


# ==========================================================
# OYUNUN DIŞ KISMI (ANA PROGRAM)
# ==========================================================

o1 = Oyuncu("Can", 30)
o2 = Oyuncu("Ali", 10)

print(o1.saldir(o2))
print(o2.saldir(o1))

print("Can'ın canı:", o1.kalan_can())
print("Ali'nin canı:", o2.kalan_can())

if o1.kalan_can() == 0:
    print("Can oyunu kaybetti!")

if o2.kalan_can() == 0:
    print("Ali oyunu kaybetti!")

# ==========================================================
# SAVAŞI DÖNGÜYE ALMAK İÇİN
# ==========================================================
# while True:
#     o1 = Oyuncu("Can", 30)
#     o2 = Oyuncu("Ali", 10)

#     print(o1.saldir(o2))
#     print(o2.saldir(o1))

#     print("Can'ın canı:", o1.kalan_can())
#     print("Ali'nin canı:", o2.kalan_can())

#     if o1.kalan_can() == 0:
#         print("Can oyunu kaybetti!")

#     if o2.kalan_can() == 0:
#         print("Ali oyunu kaybetti!")
