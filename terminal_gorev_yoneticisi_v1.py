gorevler = []

while True:
    print("\n--- GÖREV YÖNETİCİSİ ---")
    print("1 - Görev Ekle")
    print("2 - Görevleri Göster")
    print("3 - Görev Sil")
    print("4 - Çıkış")
    print("5 - Görevi tamamlandı yap")

    secim = input("Seçimin: ")

    if secim == "1":
        gorev = input("Görev gir: ")

        if gorev == "":
            print("Boş görev eklenemez.")
        else:
            gorevler.append(gorev)
            print("Görev eklendi.")

    elif secim == "2":
        if len(gorevler) == 0:
            print("Henüz görev yok.")
        else:
            for i in range(len(gorevler)):
                if gorevler[i].startswith("✔ "):
                    print(f"{i + 1} - [x] {gorevler[i][2:]}")
                else:
                    print(f"{i + 1} - [ ] {gorevler[i]}")

    elif secim == "3":
        if len(gorevler) == 0:
            print("Silinecek görev yok.")
        else:
            for i in range(len(gorevler)):
                print(f"{i + 1} - {gorevler[i]}")

            sil = int(input("Silmek istediğin görev numarası: "))

            if sil >= 1 and sil <= len(gorevler):
                silinen_gorev = gorevler.pop(sil - 1)
                print(f"Silindi: {silinen_gorev}")
            else:
                print("Geçersiz görev numarası.")
    elif secim == "5":
        if len(gorevler) == 0:
            print("Tamamlanacak görev yok.")
        else:
            for i in range (len(gorevler)):
                print(f"{i+1} - {gorevler[i]}")
            tamamla = int(input("Tamamlanan görev numarası: "))
            if tamamla >= 1 and tamamla <= len(gorevler):
                if gorevler[tamamla - 1].startswith("✔ "):
                    print("Bu görev zaten tamamlanmış.")
            else:
                gorevler[tamamla - 1] = "✔ " + gorevler[tamamla - 1]
                print("Görev tamamlandı olarak işaretlendi.")

    elif secim == "4":
        print("Program Kapandı.")
        break

    else:
        print("Geçersiz seçim yaptın.")