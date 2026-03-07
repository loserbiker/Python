import random

print("Sayı Tahmini Oyunu")
print("7 Hakkın Vardır!")

sayi = random.randint(1, 5)
sayac = 0
hak = 7

while True:
    tahmin = int(input("Tahmin Söyle: "))

    if tahmin == sayi:
        sayac += 1
        hak -= 1
        print(f"Bildin! Kalan hak: {hak}")
        break
    elif tahmin > sayi:
        sayac += 1
        hak -= 1
        print(f"Daha Küçük Söyle. Kalan hak: {hak}")
    else:
        sayac += 1
        hak -= 1
        print(f"Daha Büyük Söyle. Kalan hak: {hak}")

    if sayac == 7:
        print("Hakkın Doldu!")
        print("Doğru sayı:", sayi)
        break