# Programın kalbi: notları saklayacak liste
notlar = []

# Programın sürekli çalışması için döngü
while True:
    # Menü ekrana yazdırılıyor
    print("1- Not Ekle")
    print("2- Notları Göster")
    print("3- Çıkış")
    
    # Kullanıcının seçimi alınıyor
    secim = input("Seçiminiz: ")
    
    # Seçime göre davranış
    if secim == "1":
        # Kullanıcıdan not alınır
        notun = input("Notunuzu yazın: ")
        # Not listeye eklenir
        notlar.append(notun)
        print("Not eklendi ✅\n")
    
    elif secim == "2":
        # Liste boş mu diye kontrol
        if not notlar:
            print("Henüz hiç not yok.\n")
        else:
            print("Tüm Notlar:")
            for i, n in enumerate(notlar, start=1):
                print(f"{i}. {n}")
            print()  # boş satır
    
    elif secim == "3":
        # Programdan çıkış
        print("Programdan çıkılıyor…")
        break
    
    else:
        print("Geçersiz seçim! Tekrar deneyin.\n")
