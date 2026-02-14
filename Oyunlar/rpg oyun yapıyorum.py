import random  # Rastgele sayı ve seçim işlemleri için random modülünü import ediyoruz

# -------------------
# Karakter Bilgileri
# -------------------
karakter = input("İsmini gir: ")  # Kullanıcıdan karakter ismini alıyoruz
karakter_cani = 50  # Başlangıç canı
iksir_sayisi = 3  # Başlangıçta 3 iksir hakkı
puan = 0  # Başlangıç puanı

# -------------------
# Zar Atma ve Şans Kontrolü
# -------------------
zar1 = random.randint(1,6)  # 1 ile 6 arasında rastgele zar
zar2 = random.randint(1,6)  # 1 ile 6 arasında rastgele zar
toplam = zar1 + zar2
print("Toplam zar:", toplam)

# Zar toplamına göre kullanıcıya şans durumu
if toplam >= 7:
    print("Zar 7'den büyük geldi, şanslısın!")
else:
    print("Zar düşük geldi, biraz şansın yaver gitmedi.")

# -------------------
# Hazine Toplama
# -------------------
hazine_listesi = ["Altın", "Gümüş", "Elmas"]  # Hazine seçenekleri
kazanan_hazine = random.choice(hazine_listesi)  # Rastgele hazine seç
print("Kazanılan hazine:", kazanan_hazine)

# Hazineye göre puan artırma
if kazanan_hazine == "Altın":
    puan += 10
elif kazanan_hazine == "Gümüş":
    puan += 5
else:
    puan += 20

print("Toplam puan:", puan)

# -------------------
# Düşman Seçimi
# -------------------
input("Saldırıya başlamak için Enter'a bas!")  # Kullanıcı hazır olduğunda başlasın
dusman_listesi = ["Goblin", "Org", "Büyücü"]  # Düşman seçenekleri
dusman = random.choice(dusman_listesi)  # Rastgele düşman seçimi

# Düşman can değerlerini belirleme
if dusman == "Goblin":
    dusman_cani = 30
elif dusman == "Org":
    dusman_cani = 20
else:
    dusman_cani = 25

print("Karşına çıkan düşman:", dusman)

# -------------------
# Savaş Döngüsü
# -------------------
while karakter_cani > 0 and dusman_cani > 0:  # Karakter ve düşman ölmediği sürece döngü devam eder
    secim = input("Ne yapmak istersin? (s= Saldır, i= İksir, k= Kaç): ")

    # ---------
    # Seçim İşlemleri
    # ---------
    if secim == "s":
        # Saldırınca düşmana rastgele hasar ver
        dusman_hasar = random.randint(5,10)
        dusman_cani -= dusman_hasar
        print("Düşmana", dusman_hasar, "hasar verdin!")

    elif secim == "i":
        # İksir kullan
        if iksir_sayisi > 0:
            karakter_cani += 10  # Canı 10 artır
            iksir_sayisi -= 1  # İksir sayısını azalt
            print("İksir kullandın! Canın 10 arttı. Kalan iksir:", iksir_sayisi)
        else:
            print("İksir kalmadı!")  # İksir yoksa uyarı

    elif secim == "k":
        # Kaçma seçeneği
        print("Savaştan kaçtın!")
        break  # Döngüden çık

    else:
        print("Geçersiz seçim! Tekrar dene.")  # Hatalı giriş kontrolü

    # ---------
    # Düşman Saldırısı
    # ---------
    if dusman_cani > 0:  # Düşman ölmüşse saldırmasın
        dusman_hasar = random.randint(5,10)  # Düşman hasarı
        karakter_cani -= dusman_hasar
        print("Düşman sana", dusman_hasar, "hasar verdi!")

    # ---------
    # Tur Sonu Can Bilgisi
    # ---------
    print("Karakter canı:", karakter_cani)
    print(dusman, "canı:", dusman_cani)
    print("-"*30)  # Ayrım çizgisi

# -------------------
# Savaş Sonucu
# -------------------
if karakter_cani <= 0:
    print(karakter, "Savaşı kaybettin!")
elif dusman_cani <= 0:
    print(karakter, "Savaşı kazandın! Tebrikler!")
