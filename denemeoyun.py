import random
tahminsayisi = 0
sayi = random.randint(1,51)

print("1 ile 50 arasında bir sayı tuttum.")

while True:
    tahmin = int(input("Tahminini söyle: "))
    if tahmin <= sayi:
        print("Daha büyük söyle!")
        tahminsayisi += 1
    elif tahmin >= sayi:
        print("Daha küçük söyle!")
        tahminsayisi += 1
    elif tahmin == sayi:
        print(f"Tebrikler! Toplam tahmin sayın: {tahminsayisi}")
        break