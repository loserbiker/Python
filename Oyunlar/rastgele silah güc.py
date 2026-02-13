isim = input("İsim girin: ")

import random

silah = ["kılıç" , "bıçak" , "kalkan" , "tüfek"]

güc = [10 , 20 , 30]

print("Adınız:" , isim)
print("Silah: " , random.choice(silah))
print("Gücünüz: " , random.choice(güc))