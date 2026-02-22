class Oyuncu:
    def __init__(self, isim, guc):
        self.isim = isim
        self.can = 100
        self.guc = guc
        pass

    def hasar_al(self,miktar):
        self.can -= miktar

        if self.can <0:
            self.can = 0
            print(self.isim,"öldü!")
            
        else:
            print(self.isim , miktar , "hasar aldı!")
            print("Kalan can:" , self.can)

    def saldir(self , rakip):
        print(self.isim , rakip.isim , "oyuncusuna saldırdı!")
        rakip.hasar_al(self.guc)

    def kalan_can(self , isim , can):
        print("Kalan Can:" , self.isim , self.can)

# Oyuncular
o1 = Oyuncu ("Can" , 30)
o2 = Oyuncu ("Ali" , 10)

o1.saldir (o2)
o2.saldir (o1)