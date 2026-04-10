tasks = []

while True:
    print("\n--- MINI TASK MANAGER ---")
    print("1 - Görev ekle")
    print("2 - Görevleri listele")
    print("3 - Görev sil")
    print("4 - Görev tamamlandı olarak işaretle")
    print("5 - Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        gorev = input("Eklemek istediğiniz görevi yaz: ")

        if gorev.strip() == "":
            print("Boş görev eklenemez.")
            continue

        yeni_gorev = {"gorev": gorev, "tamamlandi": False}
        tasks.append(yeni_gorev)
        print("Görev eklendi.")

    elif secim == "2":
        if not tasks:
            print("Hiç görev yok.")
            continue

        print("\nGörevler:")
        for i in range(len(tasks)):
            durum = "✓" if tasks[i]["tamamlandi"] else "X"
            print(f"{i + 1}. [{durum}] {tasks[i]['gorev']}")

    elif secim == "3":
        if not tasks:
            print("Silinecek görev yok.")
            continue

        print("\nGörevler:")
        for i in range(len(tasks)):
            durum = "✓" if tasks[i]["tamamlandi"] else "X"
            print(f"{i + 1}. [{durum}] {tasks[i]['gorev']}")

        silinecek = input("Silmek istediğin görevin numarasını yaz: ")

        if not silinecek.isdigit():
            print("Geçersiz giriş!")
            continue

        silinecek = int(silinecek)

        if silinecek < 1 or silinecek > len(tasks):
            print("Böyle bir görev numarası yok.")
            continue

        silinen_gorev = tasks.pop(silinecek - 1)
        print(f"Silinen görev: {silinen_gorev['gorev']}")

    elif secim == "4":
        if not tasks:
            print("Tamamlanacak görev yok.")
            continue

        print("\nGörevler:")
        for i in range(len(tasks)):
            durum = "✓" if tasks[i]["tamamlandi"] else "X"
            print(f"{i + 1}. [{durum}] {tasks[i]['gorev']}")

        tamamlanacak = input("Tamamlanan görevin numarasını yaz: ")

        if not tamamlanacak.isdigit():
            print("Geçersiz giriş!")
            continue

        tamamlanacak = int(tamamlanacak)

        if tamamlanacak < 1 or tamamlanacak > len(tasks):
            print("Böyle bir görev numarası yok.")
            continue

        tasks[tamamlanacak - 1]["tamamlandi"] = True
        print("Görev tamamlandı olarak işaretlendi.")

    elif secim == "5":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz işlem, tekrar dene.")