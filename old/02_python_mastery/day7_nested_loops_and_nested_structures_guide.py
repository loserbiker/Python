"""
============================================================
PYTHON MASTERY V2 - DAY 7
KONU: NESTED LOOPS (İÇ İÇE DÖNGÜLER) VE İÇ İÇE YAPILAR
============================================================

Bu dosya, Python'da iç içe döngüler ve iç içe koşullar konusunu
en temelden, sıfır kafa karışıklığıyla anlamak için hazırlanmıştır.

Amaç:
- İç içe for döngüsünü anlamak
- İç içe while döngüsünü anlamak
- Döngü içinde koşul mantığını kavramak
- Koşul içinde döngü mantığını kavramak
- İç içe if yapısını anlamak
- Pattern (desen) sorularının mantığını görmek
- Satır / sütun düşüncesini oturtmak
- Nested yapılarda neden kafa karıştığını anlamak
- Kendi başına debug yapabilecek seviyeye gelmek

Bu dosya sadece kod değil.
Aynı zamanda öğretici rehberdir.

------------------------------------------------------------
İÇİNDEKİLER
------------------------------------------------------------
1. Nested yapı nedir?
2. Ön bilgi: for, while, if neden önemli?
3. İç içe for döngüsü mantığı
4. Adım adım çalışma mantığı
5. Satır - sütun düşüncesi
6. print(end="") neden kullanılır?
7. Döngü içinde koşul
8. Koşul içinde döngü
9. İç içe if yapısı
10. İç içe while
11. Pattern mantığı
12. Gerçek hayatta nested yapı örnekleri
13. Sık yapılan hatalar
14. Debug yöntemi
15. Mini örnekler
16. Alıştırmalar
17. Soru-cevap bölümü
18. Gün sonu özeti

Not:
Bu dosyayı çalıştırıp çıktılarını gözlemlemen de faydalı olur.
Ama asıl hedef, mantığı kafada oturtmaktır.
"""

# ============================================================
# 1) NESTED YAPI NEDİR?
# ============================================================

"""
Nested = iç içe demektir.

Programlamada nested yapı dediğimiz şey,
bir yapının içinde başka bir yapı olmasıdır.

Örnek:
- for içinde for
- while içinde while
- if içinde if
- for içinde if
- if içinde for

Yani tek katmanlı değil, çok katmanlı bir akış vardır.

Bunu günlük hayattan düşün:

Örnek 1:
Bir apartman düşün.
- apartman var
- her katta daireler var

Burada:
- apartman = dış yapı
- daireler = iç yapı

Örnek 2:
Bir okul düşün.
- öğrenciler var
- her öğrencinin dersleri var

Burada:
- öğrenciler = dış döngü
- her öğrencinin dersleri = iç döngü

Özet:
Bir şeyin içindeki başka şeyleri tek tek gezeceksen,
nested mantık genelde devreye girer.
"""

# ============================================================
# 2) ÖN BİLGİ: FOR, WHILE VE IF NEDEN ÖNEMLİ?
# ============================================================

"""
Nested yapılara geçmeden önce şunu net bilmeliyiz:

1) Döngü ne yapar?
   Bir işi tekrar tekrar yapar.

2) Koşul ne yapar?
   Karar verir.

3) Nested yapı ne yapar?
   Tekrar ve kararı katmanlı hale getirir.

Önce tek katmanlı hali tekrar görelim.
"""

print("============================================================")
print("2) TEK KATMANLI YAPILARI HATIRLAMA")
print("============================================================")

print("\nFOR örneği:")
for harf in "python":
    print(harf)

print("\nWHILE örneği:")
sayac = 0
while sayac < 3:
    print("sayac =", sayac)
    sayac += 1

print("\nIF örneği:")
yas = 20
if yas >= 18:
    print("Yetişkin")
else:
    print("Yetişkin değil")

"""
Burada önemli mantık:

FOR:
- elimizde bir akış, koleksiyon veya sıra varsa gezdirir

WHILE:
- koşul doğru olduğu sürece çalışır

IF:
- doğru / yanlış durumuna göre karar verir

Nested yapılarda bunlar birleşir.
"""

# ============================================================
# 3) İÇ İÇE FOR DÖNGÜSÜ
# ============================================================

"""
Şimdi esas konuya geliyoruz.

İç içe for döngüsü:
Bir for döngüsünün içinde başka bir for döngüsünün olmasıdır.

Genel şablon:

for dis in ...:
    for ic in ...:
        işlem

Buradaki kritik mantık:
İç döngü, dış döngünün HER turunda tekrar baştan çalışır.

Bu cümle çok önemli.
Yani iç döngü bir kez çalışıp bitmez.
Dış döngü her yeni tura geçtiğinde, iç döngü yeniden başlar.
"""

print("\n============================================================")
print("3) İÇ İÇE FOR DÖNGÜSÜ")
print("============================================================")

for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)

"""
Şimdi bunu yavaş yavaş düşünelim.

Dış döngü:
i = 0, 1, 2

İç döngü:
j = 0, 1

Ama bunlar karışık değil, sırayla çalışır.

Akış şöyle olur:

1. dış döngü başlar -> i = 0
   1.1 iç döngü başlar -> j = 0
   1.2 iç döngü devam -> j = 1
   1.3 iç döngü biter

2. dış döngü ikinci tura geçer -> i = 1
   2.1 iç döngü tekrar başlar -> j = 0
   2.2 iç döngü devam -> j = 1
   2.3 iç döngü biter

3. dış döngü üçüncü tura geçer -> i = 2
   3.1 iç döngü tekrar başlar -> j = 0
   3.2 iç döngü devam -> j = 1
   3.3 iç döngü biter

Yani çıktı:
i = 0 j = 0
i = 0 j = 1
i = 1 j = 0
i = 1 j = 1
i = 2 j = 0
i = 2 j = 1

Ana cümle tekrar:
İç döngü, dış döngünün her turunda yeniden baştan çalışır.
"""

# ============================================================
# 4) ADIM ADIM ÇALIŞMA MANTIĞI
# ============================================================

print("\n============================================================")
print("4) ADIM ADIM AKIŞI GÖRME")
print("============================================================")

for i in range(2):
    print("Dış döngü başladı -> i =", i)
    for j in range(3):
        print("   İç döngü çalışıyor -> j =", j)
    print("Dış döngünün bu turu bitti")

"""
Bu örnek nested loop'u görmek için çok değerlidir.

Çünkü çoğu öğrenci nested yapılarda şurada zorlanır:
Kod gözünde bir anda çalışıyor gibi görünür.

Ama aslında öyle değildir.
Python çok mekanik çalışır.
Satır satır, blok blok, sıra sıra ilerler.

Bu örnek sana şunu gösteriyor:
- önce dış döngü 1 tur başlatıyor
- sonra iç döngü tamamen bitiyor
- sonra dış döngü ikinci tura geçiyor
- sonra iç döngü tekrar tamamen bitiyor

Yani iç döngü parçalı değil, her dış turda tam çalışır.
"""

# ============================================================
# 5) SATIR - SÜTUN DÜŞÜNCESİ
# ============================================================

"""
Nested loop'u anlamanın en kolay yollarından biri
satır-sütun mantığıyla düşünmektir.

Dış döngü çoğu zaman SATIR gibi çalışır.
İç döngü çoğu zaman SÜTUN gibi çalışır.

Örnek:
3 satır ve her satırda 4 karakter yazdırmak istiyoruz.
"""

print("\n============================================================")
print("5) SATIR - SÜTUN MANTIĞI")
print("============================================================")

for satir in range(3):
    for sutun in range(4):
        print("*", end="")
    print()

"""
Çıktı:
****
****
****

Burada:
- dış döngü 3 kez döndü -> 3 satır oluştu
- iç döngü her satırda 4 kez döndü -> 4 yıldız oluştu

Zihinde şöyle gör:

1. satır:
****
2. satır:
****
3. satır:
****

Dış döngü satır sayısını belirledi.
İç döngü satırın içindeki eleman sayısını belirledi.

Bu düşünce çok önemli.
Çünkü sonra tablo, matris, harita, koordinat sistemi,
oyun alanı, pattern soruları hep bu mantığa bağlanır.
"""

# ============================================================
# 6) print(end="") NEDEN KULLANILIR?
# ============================================================

"""
Normal print() fonksiyonu yazdırdıktan sonra alt satıra geçer.

Yani:
print("*")
print("*")

çıktısı:
*
*

olur.

Ama biz bazen aynı satırda yan yana yazdırmak isteriz.
İşte bu durumda end="" kullanırız.
"""

print("\n============================================================")
print("6) print(end='') MANTIĞI")
print("============================================================")

print("Normal print kullanımı:")
print("*")
print("*")
print("*")

print("\nend='' ile kullanım:")
print("*", end="")
print("*", end="")
print("*", end="")
print()

"""
Neden sonuna ayrı print() koyduk?
Çünkü end="" alt satıra geçmiyor.
Satır tamamlanınca kendimiz yeni satır açıyoruz.

Nested loop ile birleşince bu çok kullanılır:

for satir in range(3):
    for sutun in range(4):
        print("*", end="")
    print()

İç döngü aynı satıra yazar.
Dış döngünün sonunda print() yeni satır açar.
"""

# ============================================================
# 7) DÖNGÜ İÇİNDE KOŞUL
# ============================================================

"""
Bu yapı çok çok önemlidir.
Çünkü gerçek hayatta en çok kullanılan temel kombinasyonlardan biridir.

Mantık:
- döngü verileri tek tek getirir
- koşul her veri için karar verir

Yani her turda bir filtreleme, sınıflandırma veya karar olur.
"""

print("\n============================================================")
print("7) DÖNGÜ İÇİNDE KOŞUL")
print("============================================================")

for sayi in range(1, 11):
    if sayi % 2 == 0:
        print(sayi, "çift")
    else:
        print(sayi, "tek")

"""
Burada ne oldu?

Döngü:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10 sayılarını tek tek verdi.

Koşul:
Her sayı için şunu sordu:
- 2'ye bölümünden kalan 0 mı?
- evetse çift
- değilse tek

Yani:
Döngü = tekrar
Koşul = karar

Bu iki yapının birleşimi:
"Tekrar eden karar verme mekanizması" oluşturur.

Bu yapı şu işlerde çok kullanılır:
- listedeki çift sayıları bulmak
- notları sınıflandırmak
- şifre karakterlerini kontrol etmek
- kullanıcı verilerini filtrelemek
- uygun olan kayıtları ayıklamak
"""

# ============================================================
# 8) KOŞUL İÇİNDE DÖNGÜ
# ============================================================

"""
Burada mantık ters tarafta:
Önce karar verilir, sonra döngü çalıştırılır.

Yani bir işlem sadece şart sağlanıyorsa tekrar eder.
"""

print("\n============================================================")
print("8) KOŞUL İÇİNDE DÖNGÜ")
print("============================================================")

izin_var = True

if izin_var:
    for i in range(3):
        print("İşlem yapılıyor:", i)
else:
    print("İzin yok, işlem yapılmadı.")

"""
Burada:
- önce izin var mı kontrol edildi
- varsa döngü çalıştı
- yoksa hiç çalışmadı

Bu yapı ne zaman mantıklıdır?
- kullanıcı giriş yaptıysa menüyü göster
- admin ise tüm kayıtları döndür
- yaş uygunsa başvuru seçeneklerini listele
- seçim doğruysa tekrar eden işlem yap

Yani:
Bazı tekrarlar, her zaman değil,
sadece belli bir durumda yapılır.
"""

# ============================================================
# 9) İÇ İÇE IF YAPISI
# ============================================================

"""
İç içe if, bir kararın içinde başka karar olmasıdır.

Bu özellikle çok katmanlı karar yapısında kullanılır.

Örnek:
Önce yaşa bak.
Sonra ehliyete bak.
"""

print("\n============================================================")
print("9) İÇ İÇE IF")
print("============================================================")

yas = 20
ehliyet = True

if yas >= 18:
    if ehliyet:
        print("Araba kullanabilir.")
    else:
        print("Yaşı uygun ama ehliyeti yok.")
else:
    print("Yaşı yetmiyor.")

"""
Buradaki mantığı iyi oku:

1. İlk soru:
   Bu kişinin yaşı yeterli mi?

2. Eğer evet ise ikinci soru:
   Ehliyeti var mı?

3. Eğer ilk soru hayırsa,
   ikinci soruyu sormanın zaten anlamı kalmaz.

İç içe if'in mantığı tam olarak budur:
Bazı kararlar, sadece önceki karar doğruysa kontrol edilir.

Gerçek hayatta çok kullanılır:
- kullanıcı mevcut mu?
  - evetse şifre doğru mu?
- ürün stokta mı?
  - evetse bakiye yeterli mi?
- yaş uygun mu?
  - evetse belge var mı?
"""

# ============================================================
# 10) İÇ İÇE WHILE
# ============================================================

"""
Nested yapılar sadece for ile olmaz.
While ile de yapılır.

Ama while'da dikkat daha çok gerekir.
Çünkü sayaçları elle yönetiyorsun.

En kritik nokta:
İç sayaç, dış döngünün her turunda sıfırlanmalıdır.
"""

print("\n============================================================")
print("10) İÇ İÇE WHILE")
print("============================================================")

i = 0
while i < 3:
    j = 0
    while j < 4:
        print("#", end="")
        j += 1
    print()
    i += 1

"""
Çıktı:
####
####
####

Burada neden j = 0 satırı dış döngünün içinde?

Çünkü:
Her yeni satıra geçtiğimizde iç döngünün baştan başlaması gerekiyor.

Eğer j'yi sadece bir kez tanımlarsan ne olur?
İlk tur sonunda j zaten 4 olmuş olur.
Sonraki turda while j < 4 yanlış olacağı için iç döngü çalışmaz.

Demek ki:
Nested while kullanırken sayaçların nerede sıfırlandığı çok önemlidir.
"""

# ============================================================
# 11) PATTERN (DESEN) MANTIĞI
# ============================================================

"""
Pattern soruları nested loop öğrenmenin en iyi yollarından biridir.

Çünkü sana iki şeyi aynı anda öğretir:
1) satır-sütun düşüncesi
2) tekrar sayısının nasıl değiştiği

Önce sabit desen:
"""

print("\n============================================================")
print("11) PATTERN ÖRNEKLERİ")
print("============================================================")

print("\nSabit dikdörtgen:")
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

"""
Burada her satır aynı.
Yani her satırda 5 yıldız var.
Toplam 4 satır var.
"""

print("\nArtan yıldız deseni:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

"""
Çıktı:
*
**
***
****
*****

Bu neden oldu?

Dış döngü:
i = 1, 2, 3, 4, 5

İç döngü:
Her satırda i kadar döndü.

Yani:
1. satır -> 1 yıldız
2. satır -> 2 yıldız
3. satır -> 3 yıldız
4. satır -> 4 yıldız
5. satır -> 5 yıldız
"""

print("\nAzalan yıldız deseni:")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

"""
Çıktı:
*****
****
***
**
*

Burada mantık ters.
Dış döngü 5'ten 1'e gidiyor.
Dolayısıyla iç döngü her satırda daha az çalışıyor.
"""

print("\nSayı deseni:")
for i in range(1, 4):
    for j in range(3):
        print(i, end="")
    print()

"""
Çıktı:
111
222
333

Burada:
- dış döngü satır numarasını / yazılacak sayıyı belirliyor
- iç döngü onu 3 kez yazdırıyor
"""

# ============================================================
# 12) GERÇEK HAYATTA NESTED YAPI ÖRNEKLERİ
# ============================================================

"""
Şimdi daha somut düşünelim.
Nested yapı sadece yıldız çizmek için değildir.

Gerçek kullanımlar:
- öğrenciler ve dersleri
- kullanıcılar ve siparişleri
- satranç tahtası / oyun grid sistemi
- dosyalar ve içindeki satırlar
- kelimeler ve harfler
- tablo üretme
- çarpım tablosu
- her kullanıcı için her görevi listeleme
"""

print("\n============================================================")
print("12) GERÇEK HAYAT ÖRNEKLERİ")
print("============================================================")

print("\nÖrnek 1: Öğrenciler ve dersler")
ogrenciler = ["Ali", "Ayşe"]
dersler = ["Matematik", "Fizik", "Python"]

for ogrenci in ogrenciler:
    for ders in dersler:
        print(ogrenci, "-", ders)

"""
Burada mantık:
Her öğrenci için bütün dersleri gez.

Ali - Matematik
Ali - Fizik
Ali - Python
Ayşe - Matematik
Ayşe - Fizik
Ayşe - Python
"""

print("\nÖrnek 2: Kelimeler ve harfleri")
kelimeler = ["python", "kod"]

for kelime in kelimeler:
    print("Kelime:", kelime)
    for harf in kelime:
        print("   Harf:", harf)

"""
Burada:
- dış döngü kelimeleri geziyor
- iç döngü her kelimenin harflerini geziyor

Bu çok gerçek nested mantıktır:
bir şeyin içindeki başka şeyler.
"""

print("\nÖrnek 3: Koordinat sistemi")
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

"""
Bu mantık özellikle:
- oyun geliştirme
- matris işlemleri
- grid sistemleri
- harita mantığı
- 2 boyutlu yerleşim sistemleri

gibi alanlarda çok önemlidir.
"""

print("\nÖrnek 4: Çarpım tablosu")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# ============================================================
# 13) SIK YAPILAN HATALAR
# ============================================================

"""
Nested yapılarda en sık düşülen hataları çok net bilelim.
"""

print("\n============================================================")
print("13) SIK YAPILAN HATALAR")
print("============================================================")

print("Bu bölüm açıklama amaçlıdır. Hataları aşağıda not olarak okuyun.")

"""
HATA 1) İç döngünün dış döngüyle birlikte tek tek ilerlediğini sanmak
------------------------------------------------------------
Yanlış düşünce:
i = 0 iken j = 0
i = 1 iken j = 1
i = 2 iken j = 2

Bu nested loop mantığı değildir.

Doğru düşünce:
i = 0 iken j baştan sona gider
i = 1 iken j tekrar baştan sona gider
i = 2 iken j tekrar baştan sona gider

HATA 2) print() yerini yanlış koymak
------------------------------------------------------------
Örnek yanlış:
for i in range(3):
    for j in range(4):
        print("*")

Bu ne üretir?
Her yıldızı ayrı satıra basar.

Doğru:
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

HATA 3) Girintiyi yanlış yapmak
------------------------------------------------------------
Python'da girinti sadece görüntü değildir.
Mantığın kendisidir.

Bir satırın hangi bloğa ait olduğunu girinti belirler.

HATA 4) while içinde sayacı artırmayı unutmak
------------------------------------------------------------
while yanlış sayaç yönetilirse sonsuz döngü olur.

HATA 5) Nested while'da iç sayacı sıfırlamayı unutmak
------------------------------------------------------------
Bu çok klasik hatadır.

HATA 6) Değişken isimleri karıştırmak
------------------------------------------------------------
i, j, k kullanırken neyin ne olduğunu unutursan kafan karışır.
Başlangıçta daha anlamlı isimler kullanmak iyidir:
satir, sutun, ogrenci, ders gibi.

HATA 7) Kodu bir anda anlamaya çalışmak
------------------------------------------------------------
Nested yapıyı anlamanın yolu:
akışı yavaşlatmak ve adım adım izlemektir.
"""

# ============================================================
# 14) DEBUG YÖNTEMİ
# ============================================================

"""
Nested yapılarda debug yapmayı öğrenmek çok değerlidir.

Aşağıdaki yöntemleri kullan.
"""

print("\n============================================================")
print("14) DEBUG YÖNTEMİ")
print("============================================================")

print("\nYöntem 1: Değerleri yazdır")
for i in range(2):
    print("Dış tur başladı -> i =", i)
    for j in range(2):
        print("   İç tur -> j =", j)

"""
Bu yöntem sana akışı gösterir.
Kod kafanda görünmüyorsa ekrana dök.
"""

print("\nYöntem 2: Büyük sayıları küçült")
for i in range(2):
    for j in range(3):
        print(i, j)

"""
Mesela range(100) yerine önce range(2) kullan.
range(50) yerine önce range(3) kullan.

Büyük örnekler kafayı karıştırır.
Küçük örnekle mantığı yakala.
"""

"""
Yöntem 3: Kağıda tablo çiz
------------------------------------------------------------
Senin öğrenme stiline çok uygun.

Örnek tablo:

Dış Tur | İç Tur | Çıktı
------------------------
i=0     | j=0    | 0 0
i=0     | j=1    | 0 1
i=1     | j=0    | 1 0
i=1     | j=1    | 1 1

Bu tabloyu elinle çizmek nested mantığı taş gibi oturtur.
"""

# ============================================================
# 15) MİNİ ÖRNEKLER
# ============================================================

print("\n============================================================")
print("15) MİNİ ÖRNEKLER")
print("============================================================")

print("\nÖrnek A: 1 ile 3 arası sayıları 2 kez yazdır")
for i in range(1, 4):
    for j in range(2):
        print(i)

print("\nÖrnek B: 1 ile 10 arası çift sayılar")
for sayi in range(1, 11):
    if sayi % 2 == 0:
        print(sayi)

print("\nÖrnek C: 3 satır, 5 sütun")
for satir in range(3):
    for sutun in range(5):
        print("X", end="")
    print()

print("\nÖrnek D: Küçük çarpım tablosu")
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

print("\nÖrnek E: Pozitif mi, negatif mi?")
sayilar = [3, -1, 0, 8, -5]
for sayi in sayilar:
    if sayi > 0:
        print(sayi, "pozitif")
    elif sayi < 0:
        print(sayi, "negatif")
    else:
        print(sayi, "sıfır")

# ============================================================
# 16) ALIŞTIRMALAR
# ============================================================

"""
Aşağıdaki alıştırmaları kendin çözmeye çalış.
Cevaplara hemen bakma.
Önce mantığı kur.
Sonra çalıştır.
"""

print("\n============================================================")
print("16) ALIŞTIRMALAR")
print("============================================================")

# ------------------------------------------------------------
# ALIŞTIRMA 1
# ------------------------------------------------------------
"""
Aşağıdaki çıktıyı üret:

111
222
333
"""

print("\nAlıştırma 1 çözümü:")
for i in range(1, 4):
    for j in range(3):
        print(i, end="")
    print()

# ------------------------------------------------------------
# ALIŞTIRMA 2
# ------------------------------------------------------------
"""
Aşağıdaki çıktıyı üret:

*
**
***
****
*****
"""

print("\nAlıştırma 2 çözümü:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# ------------------------------------------------------------
# ALIŞTIRMA 3
# ------------------------------------------------------------
"""
1 ile 10 arasındaki çift sayıları yazdır.
"""

print("\nAlıştırma 3 çözümü:")
for sayi in range(1, 11):
    if sayi % 2 == 0:
        print(sayi)

# ------------------------------------------------------------
# ALIŞTIRMA 4
# ------------------------------------------------------------
"""
1 ile 3 arasında küçük çarpım tablosu yap.

Beklenen mantık:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
...
"""

print("\nAlıştırma 4 çözümü:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# ------------------------------------------------------------
# ALIŞTIRMA 5
# ------------------------------------------------------------
"""
Bir listedeki tek sayıları bul.
"""

print("\nAlıştırma 5 çözümü:")
veriler = [2, 5, 8, 11, 14, 17]
for sayi in veriler:
    if sayi % 2 != 0:
        print(sayi)

# ------------------------------------------------------------
# ALIŞTIRMA 6
# ------------------------------------------------------------
"""
2 satır ve 6 sütundan oluşan bir şekil yazdır.
"""

print("\nAlıştırma 6 çözümü:")
for satir in range(2):
    for sutun in range(6):
        print("-", end="")
    print()

# ------------------------------------------------------------
# ALIŞTIRMA 7
# ------------------------------------------------------------
"""
Azalan pattern yazdır:

*****
****
***
**
*
"""

print("\nAlıştırma 7 çözümü:")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# ============================================================
# 17) SORU - CEVAP BÖLÜMÜ
# ============================================================

"""
Soru 1) Nested loop neden zor geliyor?
Cevap:
Çünkü tek katmanlı düşünmeye alışkınız.
Bir döngünün içinde başka döngü görünce beyin hepsini aynı anda
çalışıyormuş gibi algılıyor.
Halbuki sırayla çalışıyor.

Soru 2) İç döngü ne zaman başa döner?
Cevap:
Dış döngü her yeni tura geçtiğinde.

Soru 3) Dış döngü neyi temsil eder?
Cevap:
Çoğu zaman satır, grup, ana kategori, ana eleman.
Ama bu zorunlu değil. Mantığa göre değişir.

Soru 4) İç döngü neyi temsil eder?
Cevap:
Çoğu zaman sütun, detay, alt eleman, iç yapı.

Soru 5) for içinde if ile if içinde for farkı nedir?
Cevap:
- for içinde if: her turda karar verirsin
- if içinde for: koşul doğruysa döngüyü çalıştırırsın

Soru 6) Nested while neden daha riskli?
Cevap:
Çünkü sayaçları elle sen yönetirsin.
Yanlış yerde artırırsan veya sıfırlamazsan mantık bozulur.

Soru 7) Pattern soruları neden önemli?
Cevap:
Çünkü satır-sütun mantığını ve tekrar sayısının nasıl değiştiğini öğretir.

Soru 8) Bu konu ileride nerede işime yarayacak?
Cevap:
- algoritma sorularında
- veri işlerken
- matris / tablo mantığında
- oyun geliştirmede grid sistemlerinde
- dosya işleme mantığında
- çok katmanlı veri yapılarda
"""

# ============================================================
# 18) GÜN SONU ÖZETİ
# ============================================================

"""
Bugün öğrendiğin ana taşlar şunlar:

1) Nested = iç içe yapı demektir.
2) İç içe for döngüsünde iç döngü,
   dış döngünün her turunda baştan çalışır.
3) Dış döngü çoğu zaman satır,
   iç döngü çoğu zaman sütun mantığında düşünülür.
4) print(end="") aynı satıra yazmak için kullanılır.
5) Döngü içinde koşul:
   her turda karar verme sağlar.
6) Koşul içinde döngü:
   şart sağlanırsa tekrar eden işlem yapar.
7) İç içe if:
   bir kararın içinde başka karar anlamına gelir.
8) Nested while:
   sayaç yönetimi yüzünden daha dikkat ister.
9) Pattern soruları nested mantığını güçlendirir.
10) Kafan karışınca debug et:
    - küçük örnek kur
    - değerleri yazdır
    - kağıda tablo çiz

Bugünün gerçek kazanımı:
Nested loop görünce panik olmamak.

Bu konuyu oturtursan:
- algoritmalarda daha az bocalarsın
- pattern sorularında daha hızlı olursun
- ileride 2 boyutlu mantıklarda daha rahat ilerlersin

Day 7 burada tamamlandı.
"""