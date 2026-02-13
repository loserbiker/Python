name = input("İsminiz: ")
import random
zar1 = random.randint(1,6)
zar2 = random.randint(1,6)
durum = ["Zayıf","Normal","Güçlü"]

print(name , "Zarı Attı!")
print("1.zar: " , zar1)
print("2.zar: " , zar2)
print("Toplam: " , zar1+zar2)
print("Durum: " , random.choice(durum))