# ============================================================
# FILE NAME: day10_print_return_none_break_continue_scope_guide.py
# ============================================================
# KONU:
# - print() ve return farkı
# - None nedir, ne zaman oluşur?
# - break ve continue mantığı
# - truthy / falsy
# - scope (local / global değişken mantığı)
# - nested loop okuma mantığı
#
# AMAÇ:
# Bugüne kadar soru-cevapla gördüğümüz temel kavramları,
# düzenli, açıklamalı ve repo'ya koyulabilecek şekilde toplamak.
#
# NOT:
# Bu dosya "öğretici guide" mantığında hazırlanmıştır.
# Kodların çoğu açıklama amaçlıdır.
# ============================================================


# ============================================================
# 1) PRINT() NEDİR?
# ============================================================
#
# print(), bir değeri ekrana yazdırmak için kullanılır.
# Yani print'in işi:
# "göster"
#
# Ama şunu çok iyi ayırmak gerekiyor:
# print() bir değeri ekrana yazar,
# fakat fonksiyonun sonucunu geri göndermek zorunda değildir.
#
# Bu ayrım, Python'da en kritik temel taşlardan biridir.
#


print("=== 1) PRINT ORNEGI ===")
print("Merhaba")
print(5)
print(True)


# ============================================================
# 2) RETURN NEDİR?
# ============================================================
#
# return, fonksiyonun ürettiği sonucu dışarı geri vermek için kullanılır.
#
# print = ekrana yazdırır
# return = değeri geri döndürür
#
# Çok önemli:
# Bir fonksiyon içinde print kullanman,
# o fonksiyonun dışarıya değer döndürdüğü anlamına gelmez.
#


def topla_print(a, b):
    print(a + b)


def topla_return(a, b):
    return a + b


print("\n=== 2) PRINT VS RETURN ===")

sonuc1 = topla_print(3, 4)
print("topla_print fonksiyonundan gelen deger:", sonuc1)

sonuc2 = topla_return(3, 4)
print("topla_return fonksiyonundan gelen deger:", sonuc2)

# Açıklama:
# topla_print(3, 4) ekrana 7 yazar.
# Ama return olmadığı için fonksiyonun gerçek dönüş değeri None olur.
#
# topla_return(3, 4) ise 7 değerini geri döndürür.
# Bu yüzden sonuc2 = 7 olur.


# ============================================================
# 3) NONE NEDİR?
# ============================================================
#
# None, "hiçbir değer yok", "boş dönüş", "özel olarak bir şey dönmedi"
# gibi düşünülmesi gereken özel bir değerdir.
#
# Python'da bir fonksiyon return kullanmazsa,
# otomatik olarak None döndürür.
#
# Bu çok kritik bir kuraldır.
#


def selam_ver():
    print("Selam Can")


print("\n=== 3) NONE ORNEGI ===")
deger = selam_ver()
print("Fonksiyonun donus degeri:", deger)

# Çıktı mantığı:
# Selam Can
# Fonksiyonun donus degeri: None
#
# Çünkü:
# - print("Selam Can") sadece ekrana yazdı
# - return yok
# - dolayısıyla otomatik None döndü


# ============================================================
# 4) PRINT VE RETURN KARIŞTIRILIRSA NE OLUR?
# ============================================================
#
# Yeni başlayanların en çok düştüğü tuzak:
# "Ekrana bir şey yazdı, demek ki o değeri döndürdü"
#
# Hayır.
#
# Bir fonksiyonun ekrana bir şey yazması ile
# dışarıya değer döndürmesi aynı şey değildir.
#


def kontrol_1(sayi):
    if sayi % 2 == 0:
        print("cift")
    else:
        return "tek"


print("\n=== 4) PRINT VE RETURN KARISIK ORNEK ===")
a = kontrol_1(4)
b = kontrol_1(5)

print("a =", a)
print("b =", b)

# Mantık:
# kontrol_1(4):
# - sayı çift
# - print("cift") çalışır
# - return yok
# - sonuç None
#
# kontrol_1(5):
# - sayı tek
# - return "tek"
# - sonuç "tek"
#
# Bu yüzden çıktı mantığı:
# cift
# a = None
# b = tek


# ============================================================
# 5) RETURN GELDİĞİ ANDA FONKSİYON BİTER
# ============================================================
#
# return sadece değer döndürmez.
# Aynı zamanda fonksiyonun çalışmasını da bitirir.
#


def ornek_return():
    print("1. satir")
    return "bitti"
    print("2. satir")  # Bu satır asla çalışmaz


print("\n=== 5) RETURN FONKSIYONU BITIRIR ===")
sonuc = ornek_return()
print("Donen deger:", sonuc)

# Çünkü return gelince fonksiyon orada biter.
# return'den sonraki satırlar çalışmaz.


# ============================================================
# 6) BREAK NEDİR?
# ============================================================
#
# break, döngüyü tamamen durdurur.
#
# Yani:
# "Bu döngü burada bitsin."
#


print("\n=== 6) BREAK ORNEGI ===")
for i in range(5):
    if i == 2:
        break
    print(i)

# Mantık:
# i = 0 -> yaz
# i = 1 -> yaz
# i = 2 -> break -> döngü tamamen biter
#
# Çıktı:
# 0
# 1


# ============================================================
# 7) CONTINUE NEDİR?
# ============================================================
#
# continue, döngüyü bitirmez.
# Sadece o turu atlar ve sonraki tura geçer.
#
# Yani:
# "Bu turu boş ver, devam et."
#


print("\n=== 7) CONTINUE ORNEGI ===")
for i in range(5):
    if i == 2:
        continue
    print(i)

# Mantık:
# i = 0 -> yaz
# i = 1 -> yaz
# i = 2 -> bu turu atla
# i = 3 -> yaz
# i = 4 -> yaz
#
# Çıktı:
# 0
# 1
# 3
# 4


# ============================================================
# 8) BREAK VE CONTINUE FARKI
# ============================================================
#
# break    -> döngüyü tamamen bitirir
# continue -> sadece o turu atlar
#


print("\n=== 8) BREAK / CONTINUE FARKI ===")

print("BREAK:")
for i in range(5):
    if i == 2:
        break
    print(i)

print("CONTINUE:")
for i in range(5):
    if i == 2:
        continue
    print(i)


# ============================================================
# 9) TRUTHY / FALSY NEDİR?
# ============================================================
#
# Python'da bazı değerler koşul içinde False gibi davranır.
# Bunlara falsy denir.
#
# Sık görülen falsy değerler:
# - 0
# - 0.0
# - ""
# - ''
# - []
# - {}
# - ()
# - set()
# - None
# - False
#
# Bunların dışında pek çok değer truthy kabul edilir.
#
# Örnek truthy:
# - 5
# - -1
# - "Python"
# - [1, 2]
# - True
#


print("\n=== 9) TRUTHY / FALSY ORNEK ===")

degerler = [0, "", None, [], False, "Python", 5, [1, 2], True]

for eleman in degerler:
    if eleman:
        print(eleman, "-> truthy")
    else:
        print(eleman, "-> falsy")


# ============================================================
# 10) FALSY DEGERLERI ATLAMA ORNEGI
# ============================================================
#
# if not eleman:
# ifadesi:
# "Eğer eleman falsy ise"
# anlamına gelir.
#


def yazdir_gecerli_degerler(liste):
    for eleman in liste:
        if not eleman:
            continue
        print(eleman)


print("\n=== 10) FALSY ATLAMA ORNEGI ===")
yazdir_gecerli_degerler([0, None, "", "Python", 5, False])

# Çıktı:
# Python
# 5


# ============================================================
# 11) SCOPE NEDİR?
# ============================================================
#
# Scope, bir değişkenin nerede erişilebilir olduğunu anlatır.
#
# En temel haliyle:
# - fonksiyon içindeki değişkenler local'dir
# - fonksiyon dışındaki değişkenler global olabilir
#
# Local değişken:
# Sadece ait olduğu fonksiyon içinde yaşar.
#


def fonksiyon_ici_ornek():
    x = 10
    print("Fonksiyon icinde x =", x)


print("\n=== 11) SCOPE - LOCAL ORNEGI ===")
fonksiyon_ici_ornek()

# Burada x değişkeni sadece fonksiyon içinde vardır.
# Fonksiyon dışından direkt kullanamayız.


# ============================================================
# 12) LOCAL DEGISKENE DISARIDAN ERISMEYE CALISMAK
# ============================================================
#
# Eğer fonksiyon içindeki bir değişkene dışarıdan ulaşmaya çalışırsan,
# NameError alırsın.
#
# Çünkü o değişken o alanın dışında tanımlı değildir.
#


def ornek_scope():
    x = 10
    print(x)


print("\n=== 12) LOCAL DISARIDA YOKTUR ===")
ornek_scope()

# print(x)
#
# Yukarıdaki satırı açarsan hata alırsın:
# NameError: name 'x' is not defined
#
# Çünkü o x sadece fonksiyonun içindeydi.


# ============================================================
# 13) AYNI ISIMLI DEGISKENLER HER ZAMAN AYNI DEGISKEN DEGILDIR
# ============================================================
#
# Dışarıda x = 5 olabilir.
# Fonksiyon içinde x = 8 yazarsan,
# bu genelde yeni bir local değişken olur.
# Yani dışarıdaki x değişmez.
#


x = 5

def test_scope():
    x = 8
    print("Fonksiyon icindeki x =", x)


print("\n=== 13) LOCAL VE GLOBAL AYRIMI ===")
test_scope()
print("Disaridaki x =", x)

# Çıktı:
# Fonksiyon icindeki x = 8
# Disaridaki x = 5
#
# Çünkü bunlar farklı scope içindeki değişkenlerdir.


# ============================================================
# 14) NESTED LOOP NEDİR?
# ============================================================
#
# Nested loop = iç içe döngü
#
# Bir döngünün içinde başka bir döngü olmasıdır.
#
# Çok önemli mantık:
# Dış döngü bir tur döner,
# her turda iç döngü baştan sona tekrar çalışır.
#


print("\n=== 14) NESTED LOOP ORNEGI ===")
for i in range(3):
    for j in range(2):
        print(i, j)

# Sıra şöyle olur:
# i = 0 iken j = 0, 1
# i = 1 iken j = 0, 1
# i = 2 iken j = 0, 1
#
# Çıktı:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


# ============================================================
# 15) NESTED LOOP + CONTINUE
# ============================================================
#
# continue hangi döngünün içindeyse, o döngünün akışını etkiler.
#
# Aşağıdaki örnekte continue dış döngüde.
# Bu yüzden i == 1 olduğunda,
# o dış tur tamamen atlanır.
#


print("\n=== 15) NESTED LOOP + CONTINUE ===")
for i in range(3):
    if i == 1:
        continue
    for j in range(2):
        print(i, j)

# Çıktı:
# 0 0
# 0 1
# 2 0
# 2 1


# ============================================================
# 16) MINI ORNEK - BREAK + CONTINUE + NONE
# ============================================================
#
# Şimdi birkaç konuyu tek örnekte birleştirelim.
#


def kontrol_liste(liste):
    for eleman in liste:
        if not eleman:
            continue

        if eleman == "stop":
            break

        print(eleman)


print("\n=== 16) BIRLESMIS ORNEK ===")
sonuc = kontrol_liste([0, None, "Python", 5, "stop", 9])
print("Fonksiyonun donus degeri:", sonuc)

# Mantık:
# 0 -> falsy -> continue
# None -> falsy -> continue
# "Python" -> yazdır
# 5 -> yazdır
# "stop" -> break -> döngü biter
# 9 -> artık hiç işlenmez
#
# return olmadığı için sonuc = None olur.


# ============================================================
# 17) HATA ILE NONE AYNI SEY DEGILDIR
# ============================================================
#
# Çok kritik nokta:
#
# None:
# - geçerli bir değerdir
# - fonksiyon return etmezse oluşabilir
#
# Hata:
# - programın yanlış bir şeye denk geldiğini gösterir
# - örneğin tanımsız değişken kullanmak
#
# Örnek:
#
# def a():
#     print("selam")
#
# sonuc = a()
# print(sonuc)
#
# Burada None vardır, hata yoktur.
#
# Ama:
#
# def b():
#     x = 10
#
# b()
# print(x)
#
# Burada NameError vardır.
#
# Çünkü x dışarıda tanımlı değildir.
#


# ============================================================
# 18) KISA OZET
# ============================================================
#
# print():
# - ekrana yazar
#
# return:
# - değeri geri döndürür
# - fonksiyonu bitirir
#
# None:
# - return yoksa otomatik oluşabilir
#
# break:
# - döngüyü tamamen bitirir
#
# continue:
# - sadece o turu atlar
#
# truthy/falsy:
# - if içinde bir değerin doğru/yanlış gibi davranmasıdır
#
# scope:
# - değişkenin hangi alanda yaşadığını belirler
#
# nested loop:
# - dış döngünün her turunda iç döngü tekrar başlar
#


# ============================================================
# 19) MINI QUIZ
# ============================================================
#
# Aşağıdaki soruları çalıştırmadan önce tahmin etmeye çalış.
# Sonra kodu açıp test et.
#


# SORU 1
def soru1():
    print("A")

x1 = soru1()
print("\n=== 19) MINI QUIZ ===")
print("Soru 1 sonucu:", x1)

# Beklenen mantık:
# "A" yazılır
# sonra x1 = None olur


# SORU 2
def soru2(x):
    if x > 0:
        return x
    print("sifir veya negatif")

x2 = soru2(0)
print("Soru 2 sonucu:", x2)

# Beklenen mantık:
# "sifir veya negatif" yazılır
# sonra None döner


# SORU 3
for i in range(4):
    if i == 2:
        break
    print("Soru 3:", i)

# Beklenen çıktı:
# 0
# 1


# SORU 4
for i in range(4):
    if i == 2:
        continue
    print("Soru 4:", i)

# Beklenen çıktı:
# 0
# 1
# 3


# SORU 5
x = 100

def soru5():
    x = 50
    print("Fonksiyon ici:", x)

soru5()
print("Disari:", x)

# Beklenen çıktı:
# Fonksiyon ici: 50
# Disari: 100


# ============================================================
# 20) SON SOZ
# ============================================================
#
# Bu dosyadaki kavramlar küçük görünüyor olabilir.
# Ama aslında Python temelinin omurgalarından bazıları bunlar.
#
# Özellikle:
# - print vs return
# - None
# - break / continue
# - scope
#
# Bunlar oturursa ileride fonksiyonlar, OOP, hata yönetimi,
# veri işleme ve proje mantığı çok daha rahat anlaşılır.
#
# Bir sonraki mantıklı adım:
# Artık sadece çıktı tahmini değil,
# gerçek bir mini proje yazmak.
# ============================================================