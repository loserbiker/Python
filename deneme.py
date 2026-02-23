class Oyuncu:
    def __init__(self, isim, guc):
        self.isim = isim
        self.can = 50
        self.guc = guc

    def hasar_al(self, miktar):
        self.can -= miktar
        if self.can <= 0:
            self.can = 0
            return f"{self.isim} öldü!"
        else:
            return f"{self.isim} artık {self.can} cana sahip."

    def saldir(self, rakip):
        sonuc = rakip.hasar_al(self.guc)
        return f"{self.isim} {rakip.isim} oyuncusuna saldırdı!\n{sonuc}"

# Oyuncular
o1 = Oyuncu("Can", 30)
o2 = Oyuncu("Ali", 25)

mesaj1 = o1.saldir(o2)
mesaj2 = o2.saldir(o1)