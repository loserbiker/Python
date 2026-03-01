"""
=========================================
STRINGLERDE DİLİMLEME VE BİRLEŞTİRME
=========================================

Python'da stringler üzerinde dilimleme (slicing) ve birleştirme (concatenation) işlemleri sık kullanılır.
Bu yöntemler metinleri parçalama, birleştirme veya üzerinde değişiklik yapma imkanı sağlar.
"""

# ------------------------------
# 1. STRING DİLİMLEME (SLICING STRINGS)
# ------------------------------

ornek_text = "Python Programlama"

# İlk 6 karakteri al
print(ornek_text[0:6])   # Çıktı: Python
# Not: 0 dahil, 6 dahil değil

# Başlangıçtan belirli bir indekse kadar
print(ornek_text[:6])    # Python (başlangıç varsayılan olarak 0)

# Belirli indeksten sona kadar
print(ornek_text[7:])    # Programlama

# Sondan dilimleme
print(ornek_text[-9:])   # Programlama
# Negatif indeksler sondan başlar (-1 son karakter)

# Belirli aralıkta her n. karakter
print(ornek_text[0:18:2])  # 0'dan 17'ye kadar her 2. karakter
# Çıktı: Pto rgaml

# ------------------------------
# 2. STRING BİRLEŞTİRME (CONCATENATION)
# ------------------------------

# + operatörü ile birleştirme
isim = "Can"
selam = "Merhaba "
print(selam + isim)  # Merhaba Can

# Boşluk ekleme
print(selam + " " + isim)  # Merhaba  Can

# ------------------------------
# 3. join() METODU
# ------------------------------

# Bir listeyi stringe dönüştürüp birleştirmek
kelimeler = ["Python", "ile", "kodlama"]
cumle = " ".join(kelimeler)
print(cumle)  # Python ile kodlama

# Farklı ayırıcı
cumle2 = "-".join(kelimeler)
print(cumle2)  # Python-ile-kodlama

# ------------------------------
# 4. split() METODU
# ------------------------------

# Stringi parçalamak
text = "Python ile kodlama"
parcalar = text.split()  # Boşluklardan ayırır
print(parcalar)  # ['Python', 'ile', 'kodlama']

# Belirli bir karakter ile ayırma
csv_text = "elma,armut,çilek"
csv_list = csv_text.split(",")
print(csv_list)  # ['elma', 'armut', 'çilek']

# ------------------------------
# 5. STRING FORMATLAMA (BİRLEŞTİRMEDE ALTERNATİF)
# ------------------------------

isim = "Can"
yas = 27

# Eski yöntem
print("Merhaba " + isim + ", yaşınız " + str(yas))  # Merhaba Can, yaşınız 27

# format() yöntemi
print("Merhaba {}, yaşınız {}".format(isim, yas))   # Merhaba Can, yaşınız 27

# f-string yöntemi (Python 3.6+)
print(f"Merhaba {isim}, yaşınız {yas}")             # Merhaba Can, yaşınız 27

# ------------------------------
# 6. ÖRNEKLERLE PEKİŞTİRME
# ------------------------------

text = "Python"

# 1. İlk 2 karakter
print(text[:2])   # Py

# 2. Son 3 karakter
print(text[-3:])  # hon

# 3. Ortadaki karakterler
print(text[2:5])  # tho

# 4. Her karakteri "-" ile birleştirme
print("-".join(text))  # P-y-t-h-o-n

# 5. Split ile parçalama ve tekrar birleştirme
kelimeler = "Python-Programlama-Öğren"
kelime_listesi = kelimeler.split("-")
print(kelime_listesi)             # ['Python', 'Programlama', 'Öğren']
print(" ".join(kelime_listesi))   # Python Programlama Öğren
