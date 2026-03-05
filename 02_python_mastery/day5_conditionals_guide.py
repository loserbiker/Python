"""
day5_conditionals_guide.py
DAY 5 — KOŞULLAR (IF / ELIF / ELSE) | DERİN REHBER (TR)

Bu dosya repo’ya tek başına “rehber” olarak konulacak şekilde hazırlandı.

🎯 Bugünün hedefi
- if / elif / else’in nasıl çalıştığını %100 anlamak (akış + öncelik + yaygın hatalar)
- Koşulları birleştirmek: and / or / not
- Comparison chaining (10 < x < 20)
- Nested if (iç içe koşullar) ne zaman mantıklı / ne zaman değil
- Ternary (kısa if) ile okunabilirlik
- Egzersizlerle refleks kazanmak

Kural:
- Bu rehberi okurken kodları TEK TEK çalıştır.
- "print" satırları bilinçli kondu: akışı gözünle görmen için.
"""

# ============================================================
# 0) Koşul mantığı: Program nasıl “düşünür”?
# ============================================================
# Program bir "if" gördüğünde şunu yapar:
# 1) Koşulu değerlendirir (True/False)
# 2) True ise bloğu çalıştırır
# 3) False ise bloğu atlar (elif/else varsa sıradakine bakar)

print("\n--- 0) Koşul mantığı ---")
x = 5
print("x =", x)
print("x > 3 ?", x > 3)   # True/False gözüksün diye
if x > 3:
    print("x 3'ten büyük -> blok çalıştı")


# ============================================================
# 1) if: En temel karar noktası
# ============================================================
print("\n--- 1) if ---")

age = 20
if age >= 18:
    print("Yetiskin (age >= 18)")

age = 16
if age >= 18:
    print("Bu satır çalışmaz çünkü age < 18")


# ============================================================
# 2) else: if False ise alternatif yol
# ============================================================
print("\n--- 2) else ---")

age = 16
if age >= 18:
    print("Yetiskin")
else:
    print("Cocuk / Reşit değil")


# ============================================================
# 3) elif: Birden fazla ihtimalin zinciri
# ============================================================
print("\n--- 3) elif ---")

score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 🔥 En önemli kural:
# Python, ilk True bulduğu anda DURUR.
# Yani yukarıdaki örnekte score=75 iken:
# - score>=90 False
# - score>=80 False
# - score>=70 True -> "C" basar ve biter

print("İlk True bulunca durur: score=75 -> C")


# ============================================================
# 4) Sıralama (order) neden kritiktir?
# ============================================================
print("\n--- 4) Sıralama (order) kritik ---")

# HATALI SIRALAMA:
# score >= 70 önce kontrol edilirse, 95 bile olsa ilk koşul True olur ve "C" yazdırır.
score = 95

print("score =", score)

if score >= 70:
    print("HATALI: C (çünkü ilk koşul çok geniş)")
elif score >= 90:
    print("A")
else:
    print("F")

# DOĞRU SIRALAMA: En spesifik / en yüksek eşik en üstte olmalı.
if score >= 90:
    print("DOĞRU: A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# Genel kural:
# - Kapsamı dar olan koşullar üstte
# - Kapsamı geniş olan koşullar altta


# ============================================================
# 5) Truthy / Falsy: if içi her zaman boolean olmak zorunda değil
# ============================================================
print("\n--- 5) Truthy / Falsy ---")

# Python’da birçok şey boolean gibi davranır.
# Falsy örnekleri: 0, 0.0, "", [], {}, set(), None, False
# Geri kalanların çoğu truthy’dir.

values = [0, 1, "", "merhaba", [], [1, 2], None, True, False]

for v in values:
    if v:
        print(f"{v!r:>10} -> truthy")
    else:
        print(f"{v!r:>10} -> falsy")

# Pratik kullanım:
name = ""
if not name:
    print("İsim boş (not name) -> kullanıcıdan isim istemelisin")


# ============================================================
# 6) Boolean operatörler: and / or / not
# ============================================================
print("\n--- 6) and / or / not ---")

# and: iki taraf da True ise True
# or : en az biri True ise True
# not: tersine çevirir

age = 22
has_license = True
is_drunk = False

can_drive = (age >= 18) and has_license and (not is_drunk)
print("can_drive =", can_drive)

if can_drive:
    print("Araba kullanabilir")
else:
    print("Araba kullanamaz")

# Koşulları anlaşılır yazma tekniği:
# Karmaşık bir koşulu tek satırda gömmek yerine parçalara ayır:
age_ok = age >= 18
license_ok = has_license
sober_ok = not is_drunk

if age_ok and license_ok and sober_ok:
    print("Parçalı yazım: Kullanabilir")
else:
    print("Parçalı yazım: Kullanamaz")


# ============================================================
# 7) Short-circuit (kısa devre) mantığı
# ============================================================
print("\n--- 7) Short-circuit ---")

# and: solda False ise sağa bakmaya gerek yok (zaten sonuç False)
# or : solda True ise sağa bakmaya gerek yok (zaten sonuç True)

def expensive_check():
    print("expensive_check çalıştı!")
    return True

print("False and expensive_check()")
result = False and expensive_check()
print("Sonuç:", result)  # expensive_check çalışmaz

print("\nTrue or expensive_check()")
result = True or expensive_check()
print("Sonuç:", result)  # expensive_check çalışmaz

# Bu mantık çok işe yarar: None kontrolü gibi
user = None
# user None iken user['name'] gibi bir erişim hata verir.
# önce user var mı diye kontrol edip sonra erişebilirsin.
if user and "name" in user:
    print(user["name"])
else:
    print("user yok ya da name yok -> güvenli akış")


# ============================================================
# 8) Comparison chaining: 10 < x < 20
# ============================================================
print("\n--- 8) Comparison chaining ---")

x = 15
if 10 < x < 20:
    print("x 10 ile 20 arasında")

# Aynı şey şudur:
if (x > 10) and (x < 20):
    print("Aynı mantık: (x>10) and (x<20)")

# Dikkat: Bu zincir Python’a özgü güzel bir okunabilirlik sağlar.


# ============================================================
# 9) Nested if (iç içe koşullar) + Alternatif yaklaşım
# ============================================================
print("\n--- 9) Nested if ---")

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Nested if: Kullanabilir")
    else:
        print("Nested if: Ehliyet yok")
else:
    print("Nested if: Yaş yetmez")

# Nested if bazen gereksiz karmaşa yaratır.
# Alternatif: koşulları birleştir
if (age >= 18) and has_license:
    print("Birleştirilmiş koşul: Kullanabilir")

# Alternatif 2 (guard / early return mantığı):
# Fonksiyonlarda daha temiz olur; burada örnek olsun diye fonksiyon yapalım.

def drive_decision(age: int, has_license: bool, is_drunk: bool) -> str:
    if age < 18:
        return "Yaş yetmez"
    if not has_license:
        return "Ehliyet yok"
    if is_drunk:
        return "Alkollü"
    return "Kullanabilir"

print("drive_decision:", drive_decision(17, True, False))
print("drive_decision:", drive_decision(22, False, False))
print("drive_decision:", drive_decision(22, True, True))
print("drive_decision:", drive_decision(22, True, False))


# ============================================================
# 10) Ternary operator (kısa if): Doğru yerde kullan
# ============================================================
print("\n--- 10) Ternary (kısa if) ---")

age = 20
status = "yetiskin" if age >= 18 else "cocuk"
print("status =", status)

# Ternary için kural:
# - Tek satırda anlaşılırsa kullan
# - Uzunsa normal if/else daha okunaklıdır


# ============================================================
# 11) En yaygın hata: elif yerine ayrı if yazmak
# ============================================================
print("\n--- 11) Yaygın hata: ayrı if ---")

score = 95
print("score =", score)

# HATALI: Bu iki if ayrı ayrı değerlendirilir.
if score >= 90:
    print("A (doğru)")
if score >= 80:
    print("B (hatalı çıktı: bu da çalışır!)")

# DOĞRU: elif zinciri tek yol seçer.
if score >= 90:
    print("A (tek çıktı)")
elif score >= 80:
    print("B")


# ============================================================
# 12) “Karar ağacı” düşüncesi (Decision Tree)
# ============================================================
print("\n--- 12) Decision Tree düşüncesi ---")

# Bir problemi if yazmadan önce şu şekilde yaz:
#
# 1) En büyük “engelleyici” durum nedir?
# 2) Sonra ikinci engelleyici nedir?
# 3) Hepsi geçerse -> OK
#
# Bu yaklaşım temiz kod üretir.

# Örnek: Araç kullanma kuralı
# - Yaş < 18 => RED
# - Ehliyet yok => RED
# - Alkollü => RED
# - Aksi => OK

age = 19
has_license = True
is_drunk = False

if age < 18:
    print("RED: Yaş yetmez")
elif not has_license:
    print("RED: Ehliyet yok")
elif is_drunk:
    print("RED: Alkollü")
else:
    print("OK: Kullanabilir")


# ============================================================
# 13) Egzersizler (Bugünün asıl kas geliştireni)
# ============================================================
print("\n--- 13) Egzersizler ---")

# ---------------------------
# Egzersiz 1
# ---------------------------
# Kullanıcıdan yaş al:
# 0-12  -> çocuk
# 13-17 -> genç
# 18+   -> yetişkin
#
# TODO: input alıp int'e çevir, if/elif/else ile sınıflandır.

def classify_age(age: int) -> str:
    # TODO: Burayı doldur
    if 0 <= age <= 12:
        return "cocuk"
    elif 13 <= age <= 17:
        return "genc"
    elif age >= 18:
        return "yetiskin"
    else:
        return "gecersiz"

print("classify_age(10) ->", classify_age(10))
print("classify_age(15) ->", classify_age(15))
print("classify_age(22) ->", classify_age(22))

# ---------------------------
# Egzersiz 2
# ---------------------------
# Kullanıcıdan sayı al, pozitif/negatif/sıfır yazdır
def sign_of_number(n: int) -> str:
    # TODO: Burayı doldur
    if n > 0:
        return "pozitif"
    elif n < 0:
        return "negatif"
    else:
        return "sifir"

print("sign_of_number(5)  ->", sign_of_number(5))
print("sign_of_number(-2) ->", sign_of_number(-2))
print("sign_of_number(0)  ->", sign_of_number(0))

# ---------------------------
# Egzersiz 3
# ---------------------------
# Kullanıcıdan: yaş, ehliyet, alkollü bilgisi al
# Kurallar:
# 18 altı -> kullanamaz
# ehliyet yok -> kullanamaz
# alkollü -> kullanamaz
# hepsi uygunsa -> kullanabilir
def can_drive(age: int, has_license: bool, is_drunk: bool) -> bool:
    # TODO: Burayı doldur (iki farklı yöntemle deneyebilirsin)
    return (age >= 18) and has_license and (not is_drunk)

print("can_drive(17, True, False) ->", can_drive(17, True, False))
print("can_drive(22, False, False)->", can_drive(22, False, False))
print("can_drive(22, True, True)  ->", can_drive(22, True, True))
print("can_drive(22, True, False) ->", can_drive(22, True, False))

# ---------------------------
# Mini Challenge
# ---------------------------
# Not sistemi:
# 90+ -> A
# 80+ -> B
# 70+ -> C
# 60+ -> D
# altı -> F
def grade_letter(score: int) -> str:
    # TODO: Burayı doldur
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("grade_letter(95) ->", grade_letter(95))
print("grade_letter(83) ->", grade_letter(83))
print("grade_letter(72) ->", grade_letter(72))
print("grade_letter(61) ->", grade_letter(61))
print("grade_letter(10) ->", grade_letter(10))


# ============================================================
# 14) Pratik: CLI (Kullanıcıdan input alarak)
# ============================================================
print("\n--- 14) CLI Pratik (istersen aç) ---")

# Bu bölüm interaktif. Çalıştırmak istersen yorumları kaldır.
# (Repo’da kalsın ama default kapalı dursun diye yorumlu bıraktım.)

# age_in = int(input("Yas gir: "))
# has_license_in = input("Ehliyet var mi? (e/h): ").strip().lower() == "e"
# is_drunk_in = input("Alkollu musun? (e/h): ").strip().lower() == "e"
#
# if age_in < 18:
#     print("Kullanamaz: yas yetmez")
# elif not has_license_in:
#     print("Kullanamaz: ehliyet yok")
# elif is_drunk_in:
#     print("Kullanamaz: alkollu")
# else:
#     print("Kullanabilir")


# ============================================================
# 15) Bugün bittiğinde kendini test etmen gerekenler
# ============================================================
"""
✅ Checklist (kendini yokla)
- elif zincirinde “ilk True’da durma” mantığını anlatabiliyor muyum?
- Yanlış sıralamanın nasıl bug ürettiğini biliyor muyum?
- and/or/not ile koşul birleştirirken okunabilir yazabiliyor muyum?
- Separate if vs elif farkını net biliyor muyum?
- Nested if’i ne zaman kullanacağımı / ne zaman kaçınacağımı biliyor muyum?
- Ternary’i sadece basitse kullandığımı söyleyebiliyor muyum?

Hazır olduğunda:
"tamam sorulara geçelim" yaz.
"""