import random
n=random.randint(1,10)
g=None
print("1-10 arası sayı tuttum")

while g!=n:
    g=int(input("Tahmin: "))
    if g<n: print("Yukarı")
    elif g>n: print("Aşağı")
print("Bildin :D")