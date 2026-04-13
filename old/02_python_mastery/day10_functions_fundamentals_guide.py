# day10_functions_fundamentals_guide.py

# ============================================================
# DAY 10 - FUNCTIONS FUNDAMENTALS GUIDE
# ============================================================
#
# Bu guide, Python'da function (fonksiyon) konusunu en temelden
# ve sıfır karışıklıkla oturtmak için hazırlanmıştır.
#
# Bu dosyada şunları işleyeceğiz:
# 1) Function nedir?
# 2) Neden function kullanırız?
# 3) Function nasıl tanımlanır?
# 4) Function nasıl çağrılır?
# 5) Parametre nedir?
# 6) print ve return farkı nedir?
# 7) None neden oluşur?
# 8) return neden function'ı bitirir?
# 9) function ile function() farkı nedir?
# 10) bol örnek ve mini testler
#
# Ana hedef:
# - function mantığını temiz kurmak
# - print ve return farkını netleştirmek
# - None konusunu oturtmak
# - function çağırma mantığını karıştırmamak
#
# ============================================================


# ============================================================
# 1) FUNCTION NEDIR?
# ============================================================
#
# Function, belirli bir işi yapan kod bloğudur.
#
# Yani:
# - aynı işi tekrar tekrar yazmak yerine
# - o işi bir function içine koyarız
# - sonra ihtiyaç oldukça çağırırız
#
# Böylece:
# - kod tekrarını azaltırız
# - kod daha düzenli olur
# - okunması kolaylaşır
# - aynı işi yeniden kullanabiliriz
#
# Function'ı bir makine gibi düşünebilirsin:
# - bazen içine veri girer
# - içeride işlem yapar
# - bazen dışarı sonuç verir
#
# Ama bazen sadece çalışır ve ekrana bir şey yazar.
# Her function illa sonuç döndürmek zorunda değildir.
# Bunu birazdan net göreceğiz.


# ============================================================
# 2) NEDEN FUNCTION KULLANIRIZ?
# ============================================================
#
# Diyelim ki ekrana sürekli "Merhaba" yazdırmak istiyoruz.
# Function kullanmazsak şöyle tekrar tekrar yazarız:

print("Merhaba")
print("Merhaba")
print("Merhaba")

# Bu çalışır ama iyi bir yöntem değildir.
#
# Çünkü:
# - gereksiz tekrar vardır
# - kod uzar
# - düzen bozulur
#
# Bunun yerine function yazarsak:

def selam_ver():
    print("Merhaba")

# Sonra istediğimiz kadar çağırırız:
selam_ver()
selam_ver()
selam_ver()

# İşte function'ın temel gücü budur:
# bir kere yaz, çok kere kullan.


# ============================================================
# 3) FUNCTION NASIL TANIMLANIR?
# ============================================================
#
# Function tanımlamak için "def" kullanılır.
#
# Genel yapı:
#
# def function_adi():
#     yapılacak işlemler
#
# Örnek:

def test():
    print("Bu bir function")

# Burada:
# - def -> function tanımladığımızı söyler
# - test -> function adı
# - () -> function kısmı
# - : -> blok başlatır
# - girintili satır -> function'ın içi


# ============================================================
# 4) TANIMLAMAK AYRI, ÇAĞIRMAK AYRI
# ============================================================
#
# Bu en kritik noktalardan biridir.
#
# Şu kod:

def deneme():
    print("Merhaba")

# sadece function'ı TANIMLAR.
# Bu kod tek başına çıktı üretmez.
#
# Çünkü function yazıldı ama çağrılmadı.
#
# Çalışması için çağırmamız gerekir:

deneme()

# Çıktı:
# Merhaba
#
# Kural:
# - def deneme(): -> oluşturur
# - deneme()      -> çalıştırır


# ============================================================
# 5) FUNCTION ÇAĞRILMAZSA ÇALIŞMAZ
# ============================================================
#
# Aşağıdaki function sadece tanımlanmıştır:

def bilgi():
    print("Ben buradayım")

# Eğer bilgi() yazmazsak çalışmaz.
#
# Bu yüzden her zaman şunu sor:
# "Function sadece tanımlandı mı, yoksa gerçekten çağrıldı mı?"


# ============================================================
# 6) FUNCTION İÇİNDE BİRDEN FAZLA SATIR OLABİLİR
# ============================================================

def tanitim():
    print("Ad: Can")
    print("Konu: Python")
    print("Bolum: Functions")

tanitim()

# Çıktı:
# Ad: Can
# Konu: Python
# Bolum: Functions
#
# Demek ki function, içindeki satırları sırayla çalıştırır.


# ============================================================
# 7) PARAMETRE NEDİR?
# ============================================================
#
# Bazen function'ın dışarıdan veri almasını isteriz.
# İşte buna parametre deriz.
#
# Örnek:

def selamla(isim):
    print("Merhaba", isim)

selamla("Can")
selamla("Ali")
selamla("Ayse")

# Çıktı:
# Merhaba Can
# Merhaba Ali
# Merhaba Ayse
#
# Burada:
# - isim -> parametre
# - "Can", "Ali", "Ayse" -> çağırırken verdiğimiz değerler
#
# Parametre sayesinde function daha esnek olur.
# Aynı function, farklı verilerle kullanılabilir.


# ============================================================
# 8) BİRDEN FAZLA PARAMETRE
# ============================================================

def topla(a, b):
    print(a + b)

topla(3, 4)
topla(10, 5)

# Çıktı:
# 7
# 15
#
# Burada:
# - a ve b parametredir
# - çağırırken verdiğimiz sayılar bu parametrelere yerleşir


# ============================================================
# 9) PARAMETRE SAYISI ÖNEMLİDİR
# ============================================================
#
# Eğer function 2 parametre bekliyorsa,
# normalde çağırırken 2 değer vermeliyiz.

def carp(a, b):
    print(a * b)

carp(2, 3)

# Bu doğru kullanım.
#
# Ama şöyle yaparsak:
#
# carp(2)
#
# hata alırız.
# Çünkü function 2 değer bekliyor ama 1 değer veriyoruz.
#
# Yani function'ın istediği veri sayısı ile
# bizim verdiğimiz veri sayısı uyumlu olmalı.


# ============================================================
# 10) PRINT NE YAPAR?
# ============================================================
#
# print sadece ekrana yazar.
#
# Bu çok ama çok önemli.
#
# Örnek:

print(5)

# Çıktı:
# 5
#
# Burada olan şey sadece şudur:
# 5 ekranda görünür.
#
# print, değeri dışarıya "geri vermek" anlamına gelmez.
# Sadece gösterir.
#
# Function içinde de aynı mantık geçerli:

def yazdir():
    print(10)

yazdir()

# Çıktı:
# 10
#
# Bu 10 sadece gösterildi.
# Dışarı kullanılabilir bir sonuç olarak verilmedi.


# ============================================================
# 11) RETURN NE YAPAR?
# ============================================================
#
# return, function'ın sonucunu dışarı geri verir.
#
# Örnek:

def bes_dondur():
    return 5

sonuc = bes_dondur()
print(sonuc)

# Çıktı:
# 5
#
# Burada önemli fark şu:
# 5 sadece ekranda görünmedi.
# Aynı zamanda function dışına geri verildi.
# Bu yüzden sonuc değişkenine atandı.
#
# Kısacası:
# - print = göster
# - return = geri ver


# ============================================================
# 12) PRINT VE RETURN FARKI
# ============================================================
#
# Bu konu function mantığının bel kemiğidir.
#
# Şimdi aynı sayıyı iki farklı yolla görelim.

def ornek_print():
    print(5)

def ornek_return():
    return 5

# İlkini deneyelim:
x = ornek_print()
print(x)

# Çıktı:
# 5
# None
#
# Neden?
# - function içinde print(5) çalıştı -> 5 ekrana yazıldı
# - ama return yok
# - function dışarıya bir değer vermedi
# - bu yüzden x = None oldu
# - print(x) -> None yazdı

# Şimdi return olanı deneyelim:
y = ornek_return()
print(y)

# Çıktı:
# 5
#
# Burada 5 gerçekten function dışına geri verildi.
# Bu yüzden y değişkenine atandı.


# ============================================================
# 13) NONE NEDİR?
# ============================================================
#
# None, "hiçbir değer yok" gibi düşünülebilir.
#
# Python'da bir function açıkça return etmezse,
# varsayılan olarak None döner.
#
# Örnek:

def selam():
    print("Selam")

a = selam()
print(a)

# Çıktı:
# Selam
# None
#
# Çünkü:
# - function içerde sadece yazdırdı
# - ama return etmedi
# - bu yüzden dönüş değeri None oldu
#
# Kritik kural:
# return yoksa -> function sonucu None


# ============================================================
# 14) PRINT GÖSTERİR, RETURN KULLANILABİLİR DEĞER VERİR
# ============================================================
#
# Çok önemli karşılaştırma:

def print_topla(a, b):
    print(a + b)

def return_topla(a, b):
    return a + b

# print kullanan:
p = print_topla(2, 3)
print(p)

# Çıktı:
# 5
# None

# return kullanan:
r = return_topla(2, 3)
print(r)

# Çıktı:
# 5
#
# Dışarıdan bakınca ikisinde de 5 görünmüş gibi olur.
# Ama mantıkları farklıdır:
#
# print_topla:
# - 5'i sadece gösterdi
# - sonucu geri vermedi
#
# return_topla:
# - 5'i gerçekten function dışına verdi
# - bu yüzden değişkende tutulabildi


# ============================================================
# 15) RETURN GELİNCE FUNCTION BİTER
# ============================================================
#
# Bu da aşırı önemli bir kuraldır.
#
# Function içinde return çalıştığı anda function biter.
# Altındaki satırlara artık gelinmez.

def kontrol():
    print("ilk satir")
    return 5
    print("ikinci satir")

print(kontrol())

# Çıktı:
# ilk satir
# 5
#
# "ikinci satir" neden yazmadı?
# Çünkü return çalıştıktan sonra function bitti.
#
# Kural:
# return = değeri geri ver + function'ı bitir


# ============================================================
# 16) FUNCTION VE FUNCTION() AYNI ŞEY DEĞİLDİR
# ============================================================
#
# Bu da çok karıştırılan bir yerdir.
#
# yaz    -> function'ın kendisi
# yaz()  -> function'ın çalıştırılmış hali

def yaz():
    return "Merhaba"

print(yaz)
print(yaz())

# İlk print şuna benzer bir şey verir:
# <function yaz at ...>
#
# İkinci print ise:
# Merhaba
#
# Yani:
# - print(yaz)  -> function nesnesini yazdırır
# - print(yaz()) -> function'ı çalıştırır


# ============================================================
# 17) RETURN EDİLEN DEĞERLE İŞLEM YAPABİLİRİZ
# ============================================================

def kare(x):
    return x * x

sonuc = kare(3)
print(sonuc)
print(sonuc + 1)

# Çıktı:
# 9
# 10
#
# Çünkü return edilen değer dışarıda kullanılabilir.
#
# Bu function sadece göstermekle kalmıyor,
# gerçekten veri geri veriyor.


# ============================================================
# 18) PRINT EDİLEN DEĞERLE İŞLEM YAPAMAYIZ
# ============================================================

def kare_print(x):
    print(x * x)

deger = kare_print(3)
print(deger)

# Çıktı:
# 9
# None
#
# Çünkü function 9'u sadece gösterdi.
# Geri vermedi.
# Bu yüzden deger = None oldu.
#
# Eğer sonra:
# print(deger + 1)
#
# yapmaya çalışırsak hata alırız.
# Çünkü None ile sayı toplanmaz.


# ============================================================
# 19) NEDEN BAZI YERDE HATA ALIYORUZ?
# ============================================================
#
# En klasik hata şu mantıktan gelir:
# "Ekranda gördüm, o zaman değişkende de vardır."
#
# Hayır.
#
# Ekranda görmek başka,
# function'ın gerçekten değer döndürmesi başka şeydir.
#
# Örnek:

def test_hata():
    print(10)

x = test_hata()

# x şu an 10 değil, None'dır.
#
# Eğer:
# print(x + 1)
#
# yaparsak hata olur.
#
# Çünkü bu aslında:
# None + 1
#
# demektir.


# ============================================================
# 20) DEFAULT PARAMETREYE GİRİŞ
# ============================================================
#
# Function parametresine varsayılan değer verebiliriz.

def selam_default(isim="Can"):
    print("Selam", isim)

selam_default()
selam_default("Ali")

# Çıktı:
# Selam Can
# Selam Ali
#
# Eğer değer vermezsek varsayılan kullanılır.
# Eğer değer verirsek verdiğimiz değer kullanılır.


# ============================================================
# 21) BASİT AKIŞ MANTIĞI
# ============================================================
#
# Function sorularında her zaman şu sırayla düşün:
#
# 1) Function çağrıldı mı?
# 2) İçinde print mi var?
# 3) İçinde return var mı?
# 4) Dönen değer bir değişkene atandı mı?
# 5) Sonra bu değer print edildi mi?
#
# Bu 5 soru, function konusundaki karışıklığın büyük kısmını çözer.


# ============================================================
# 22) ADIM ADIM ÖRNEK 1
# ============================================================

def topla_ornek(a, b):
    return a + b

x = topla_ornek(2, 3)
print(x)

# Akış:
# - function çağrıldı
# - 2 + 3 hesaplandı
# - return ile 5 geri verildi
# - x = 5 oldu
# - print(x) -> 5
#
# Çıktı:
# 5


# ============================================================
# 23) ADIM ADIM ÖRNEK 2
# ============================================================

def topla_ornek2(a, b):
    print(a + b)

x = topla_ornek2(2, 3)
print(x)

# Akış:
# - function çağrıldı
# - içerde print(5) çalıştı
# - ekrana 5 yazıldı
# - return olmadığı için function sonucu None oldu
# - x = None
# - print(x) -> None
#
# Çıktı:
# 5
# None


# ============================================================
# 24) ADIM ADIM ÖRNEK 3
# ============================================================

def sayi_ver():
    return 10

print(sayi_ver() + 1)

# Akış:
# - sayi_ver() -> 10
# - 10 + 1 -> 11
# - print -> 11
#
# Çıktı:
# 11


# ============================================================
# 25) ADIM ADIM ÖRNEK 4
# ============================================================

def sayi_yaz():
    print(10)

# Eğer aşağıdaki satırı çalıştırırsak:
# print(sayi_yaz() + 1)
#
# önce 10 yazılır, sonra hata alınır.
#
# Çünkü:
# - sayi_yaz() sadece 10'u gösterir
# - geri değer vermez
# - sonucu None olur
# - None + 1 hatadır


# ============================================================
# 26) MINI QUIZ BLOĞU
# ============================================================
#
# Aşağıdaki soruları yorum olarak bırakıyorum.
# İstersen sonra kendi başına çözebilirsin.

# SORU 1
def q1():
    print("A")

# q1() çağrılırsa çıktı nedir?
# Cevap: A


# SORU 2
def q2():
    return "A"

# print(q2()) çıktısı nedir?
# Cevap: A


# SORU 3
def q3():
    print("A")

# x = q3()
# print(x)
#
# Çıktı nedir?
# Cevap:
# A
# None


# SORU 4
def q4():
    return 10

# x = q4()
# print(x + 1)
#
# Çıktı nedir?
# Cevap:
# 11


# SORU 5
def q5(a, b):
    return a + b

# print(q5(2, 5))
#
# Çıktı nedir?
# Cevap:
# 7


# SORU 6
def q6(a, b):
    print(a + b)

# sonuc = q6(2, 5)
# print(sonuc)
#
# Çıktı nedir?
# Cevap:
# 7
# None


# ============================================================
# 27) FINAL BOSS MANTIĞI
# ============================================================
#
# Aşağıdaki gibi sorularda panik yapma.
# Satır satır ilerle.

def bir(a):
    print("bir basladi", a)
    return a + 1

def iki(b):
    print("iki basladi", b)
    x = bir(b)
    print("iki icinde x:", x)
    return x * 2

sonuc = iki(3)
print("final:", sonuc)

# Akış:
# - iki(3) çağrılır
# - "iki basladi 3" yazılır
# - x = bir(3) çalışır
# - bir(3) içinde "bir basladi 3" yazılır
# - bir(3) -> 4 döndürür
# - x = 4 olur
# - "iki icinde x: 4" yazılır
# - iki(3) -> 8 döndürür
# - sonuc = 8 olur
# - "final: 8" yazılır
#
# Çıktı:
# iki basladi 3
# bir basladi 3
# iki icinde x: 4
# final: 8


# ============================================================
# 28) ÇOK KISA ÖZET
# ============================================================
#
# Function konusunda cebinde kalması gereken kurallar:
#
# 1) def -> function tanımlar
# 2) function() -> function çalıştırır
# 3) print -> ekrana yazar
# 4) return -> değeri geri verir
# 5) return yoksa sonuç None olur
# 6) return çalışınca function biter
# 7) function ile function() aynı şey değildir
# 8) ekranda görmek = değişkende var demek değildir
#
# En kritik ayrım:
# print = göster
# return = geri ver


# ============================================================
# 29) KENDİ KENDİNE KONTROL SORULARI
# ============================================================
#
# Aşağıdaki 5 soruyu function konusu çalışırken kendine sor:
#
# 1) Function gerçekten çağrıldı mı?
# 2) İçeride print mi var?
# 3) İçeride return var mı?
# 4) Dönen değer değişkene atandı mı?
# 5) Sonuç dışarıda kullanıldı mı?
#
# Eğer bu 5 soruyu doğru sorarsan,
# function konusundaki kafa karışıklığının çoğu çözülür.


# ============================================================
# 30) KAPANIŞ
# ============================================================
#
# Function konusu Python'ın temel direklerinden biridir.
# İlk başta karışması çok normaldir.
#
# Özellikle şu noktalar zaman ister:
# - print ve return farkı
# - None mantığı
# - function ile function() farkı
# - değer gerçekten döndü mü, sadece yazıldı mı?
#
# Ama bu konu oturduğunda:
# - kodu daha düzenli yazarsın
# - tekrar eden işleri toparlarsın
# - ileride OOP ve profesyonel Python konularına daha sağlam geçersin
#
# Bu dosyayı birkaç kez okuyup örnekleri çalıştırırsan,
# function temeli ciddi şekilde oturur.
#
# Day 10 tamam.
# Sonraki adım: function mini practice + scope'a giriş
#
# ============================================================