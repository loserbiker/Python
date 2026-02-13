isimgir = input("İsim girin:")

import random
rastgele_icecek = ["latte" , "americano" , "kola"]
random.choice(rastgele_icecek)
puan = 0

if rastgele_icecek=="latte":
    puan += 10
elif rastgele_icecek=="americano":
    puan += 20
else:
    puan +=30

print("Çıkan içecek:" , random.choice(rastgele_icecek))
print("Say:" , puan)