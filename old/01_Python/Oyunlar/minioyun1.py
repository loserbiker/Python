# ===============================================
# TAM RPG MACERA OYUNU – MENÜ, GÖREVLER, SİLAHLAR, HAZİNE, ZAR, PUAN, SEVİYE, DÜŞMAN TÜRLERİ
# ===============================================

import random

# ----------------------------
# Kullanıcıdan isim alma
# ----------------------------
name = input("İsminiz: ")

# ----------------------------
# Silahlar ve güç değerleri
# ----------------------------
silahlar = { "Kılıç": 2, "Bıçak": 1, "Tüfek": 5, "Kalkan": 1}

secili_silah = random.choice(list(silahlar.keys()))

# ----------------------------
# Hazine listesi ve sayaçlar
# ----------------------------
hazine = ["Altın", "Elmas", "Gümüş", "Boş Hazine"]
altin_sayisi = 0
gumus_sayisi = 0
elmas_sayisi = 0

# ----------------------------
# Puan ve seviye
# ----------------------------
puan = 0
seviye = 1

# ----------------------------
# Görevler
# ----------------------------
gorevler = [
    "Ormana git ve 2 goblin temizle",
    "Mağaraya gir ve elmas bul",
    "Köyü savun ve zombi yen",
    "Ejderhayı alt et"
]

# ----------------------------
# Düşman türleri
# ----------------------------
dusmanlar = ["Goblin", "Ork", "Ejderha", "Zombi"]

# ----------------------------
# Oyun döngüsü
# ----------------------------
while True:
    # Menü ve seçenekler
    print("\n===== MENÜ =====")
    print("1- Zar at ve maceraya devam et")
    print("2- Görev al")
    print("3- Silah değiştir")
    print("4- Durumunu göster")
    print("5- Oyundan çık")
    secim = input("Seçiminizi yapın (1-5): ")

    if secim == "1":
        input("\nZarı atmak için Enter tuşuna basın...")

        # Zar atma
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        toplam = zar1 + zar2 + silahlar[secili_silah]  # silah gücü eklendi

        # Güç seviyesi belirleme
        if toplam <= 4:
            guc = "Zayıf"
        elif toplam <= 8:
            guc = "Normal"
        else:
            guc = "Güçlü"

        # Hazine kazanma ağırlıklı olasılık
        if guc == "Zayıf":
            haz = random.choices(hazine, weights=[1,1,1,10], k=1)[0]
        elif guc == "Normal":
            haz = random.choices(hazine, weights=[3,3,3,1], k=1)[0]
        else:
            haz = random.choices(hazine, weights=[5,5,3,1], k=1)[0]

        # Puan ve hazine sayacı
        if haz == "Altın":
            puan += 10
            altin_sayisi += 1
        elif haz == "Gümüş":
            puan += 5
            gumus_sayisi += 1
        elif haz == "Elmas":
            puan += 20
            elmas_sayisi += 1

        # Seviye atlama (puan bazlı)
        if puan >= seviye * 50:
            seviye += 1
            print(f"\nTebrikler! Seviye atladınız. Yeni seviyeniz: {seviye}")

        # Rastgele düşman karşılaşması (%40)
        dusman_var_mi = random.random() < 0.4
        if dusman_var_mi:
            dusman = random.choice(dusmanlar)
            dusman_gucu = random.randint(1,12)
            print(f"\nDüşmanla karşılaştınız! Düşman: {dusman} - Güç: {dusman_gucu}")
            if toplam >= dusman_gucu:
                print("Düşmanı yendiniz! Ekstra 10 puan kazandınız.")
                puan += 10
            else:
                print("Düşmana yenildiniz! 5 puan kaybettiniz.")
                puan -= 5
                if puan < 0:
                    puan = 0
        else:
            print("\nDüşman yok, rahat bir tur!")

        # Sonuçların yazdırılması
        print(f"\n{name} zarı attı!")
        print("1.Zar:", zar1)
        print("2.Zar:", zar2)
        print(f"Silah gücü ({secili_silah}):", silahlar[secili_silah])
        print("Toplam:", toplam)
        print("Güç:", guc)
        print("Kazanılan hazine:", haz)
        print("Toplam puan:", puan)
        print(f"Hazine durumu → Altın: {altin_sayisi}, Gümüş: {gumus_sayisi}, Elmas: {elmas_sayisi}")
        print(f"Seviyeniz: {seviye}")

    elif secim == "2":
        gorev = random.choice(gorevler)
        print(f"\nYeni Göreviniz: {gorev}")

    elif secim == "3":
        secili_silah = random.choice(list(silahlar.keys()))
        print(f"\nYeni silahınız: {secili_silah} (Güç: {silahlar[secili_silah]})")

    elif secim == "4":
        print(f"\nDurumunuz:")
        print(f"İsim: {name}")
        print(f"Seviye: {seviye}")
        print(f"Puan: {puan}")
        print(f"Hazine → Altın: {altin_sayisi}, Gümüş: {gumus_sayisi}, Elmas: {elmas_sayisi}")
        print(f"Silah: {secili_silah} (Güç: {silahlar[secili_silah]})")

    elif secim == "5":
        print(f"\nOyun bitti! Toplam puanın: {puan}")
        print(f"Hazine toplamın → Altın: {altin_sayisi}, Gümüş: {gumus_sayisi}, Elmas: {elmas_sayisi}")
        print(f"Son seviyen: {seviye}")
        break

    else:
        print("\nGeçersiz seçim! Lütfen 1-5 arasında bir seçenek girin.")
