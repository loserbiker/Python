#DAİRENİN ALANI VE ÇEVRESİNİ BULMA

# dairenin alanı = pi*r*r
# dairenin çevresi = 2*pi*r
# pi sayısı değeri = 3.14159

pi = 3.14159 #float veriable atandı

dairenin_yari_capi = float(input("Yarı çap :")) 
#dışarıdan veri alacağımız zaman input funciton kullanılır!
#en basit örneği adımı kendim yazabiliyorum gibi gibi!!

dairenin_alani = pi*dairenin_yari_capi*dairenin_yari_capi

dairenin_cevresi = 2 * pi * dairenin_yari_capi

print("Alan:",dairenin_alani)
print("Çevre",dairenin_cevresi)

############################################################################################################

#HESAP MAKİNESİ PROJESİ

number1 = int(input("Bir sayı girin:"))
number2 = int(input("İkinci sayıyı girin"))

toplam = number1 + number2

print("Toplam:",toplam)

############################################################################################################
