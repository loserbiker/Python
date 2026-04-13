"""
DAY 8 - NESTED LOOPS (İÇ İÇE DÖNGÜLER) VE PATTERN MANTIĞI
========================================================

Bu dosyanın amacı:
- Nested loop nedir, temiz şekilde anlamak
- Dış döngü / iç döngü farkını oturtmak
- Pattern sorularına bakınca panik olmadan analiz yapabilmek
- "Kaç satır var, her satırda kaç eleman var, ne basılacak?"
  mantığını zihne yerleştirmek

ÖNEMLİ NOT:
Bu konu ilk görüldüğünde biraz bulanık gelir.
Bu normaldir.
Çünkü nested loop konusu ezber konusu değil, görsel mantık konusudur.

Başlangıçta insan:
- kodu görünce karışır
- hangi döngü neyi yönetiyor şaşırır
- pattern görünce direkt çözemeyebilir

Bu başarısızlık değildir.
Bu, beynin yeni bir düşünme biçimine alışmasıdır.

Bu dosyada her şeyi sıfırdan, sade ve sağlam kuracağız.
"""


# =========================================================
# 1) NESTED LOOP NEDİR?
# =========================================================

"""
Nested loop = döngü içinde döngü.

Yani bir for loop'un içinde başka bir for loop varsa,
orada nested loop vardır.

Örnek:
"""

for satir in range(3):
    for sutun in range(2):
        print("*", end="")
    print()

"""
Çıktı:
**
**
**

Bu kod neden böyle çıktı?

Çünkü:

Dış döngü:
for satir in range(3)

Bu kısım 3 kez döner.
Yani 3 satır üretir.

İç döngü:
for sutun in range(2)

Bu kısım her dış döngü turunda 2 kez döner.
Yani her satırın içine 2 tane yıldız koyar.

Sondaki print():
Alt satıra geçmek için kullanılır.

BİR CÜMLELİK ANA TANIM:
- Dış döngü satırı yönetir
- İç döngü satırın içini doldurur
"""

print("\n" + "=" * 50)
print("1. bölüm bitti")
print("=" * 50)


# =========================================================
# 2) EN KRİTİK MANTIK: PATTERN ANALİZ FORMÜLÜ
# =========================================================

"""
Bir pattern görünce direkt koda atlama.
Önce şu 3 soruyu sor:

1. Kaç satır var?
2. Her satırda kaç eleman var?
3. Ne basılacak?

Bu 3 soru nested loop konusunun omurgasıdır.

Pattern sorularında insanlar genelde direkt syntax'a atladığı için karışır.
Ama önce analiz yapılırsa kod çok daha rahat çıkar.

Şimdi birkaç örnekle görelim.
"""


# =========================================================
# 3) ÖRNEK 1 - ARTAN YILDIZ PATTERNİ
# =========================================================

"""
İstenen çıktı:

*
**
***

Analiz:
1. Kaç satır var?
   -> 3 satır

2. Her satırda kaç eleman var?
   -> 1, 2, 3 şeklinde artıyor

3. Ne basılacak?
   -> * basılacak

Kod:
"""

print("\nÖRNEK 1")
for satir in range(1, 4):
    for _ in range(satir):
        print("*", end="")
    print()

"""
Neden böyle?

Dış döngü:
range(1, 4) -> 1, 2, 3 üretir

Yani satir değişkeni sırayla:
1, sonra 2, sonra 3 olur.

İç döngü:
range(satir)

Bu da:
- satir = 1 iken 1 kez
- satir = 2 iken 2 kez
- satir = 3 iken 3 kez döner

Ve her dönüşte "*" basılır.

Buradaki önemli fikir:
İç döngünün kaç kez döneceğini dış döngüdeki değer belirliyor.
"""


# =========================================================
# 4) ÖRNEK 2 - AYNI SAYIYI TEKRAR ETME
# =========================================================

"""
İstenen çıktı:

1
22
333

Analiz:
1. Kaç satır var?
   -> 3

2. Her satırda kaç eleman var?
   -> 1, 2, 3

3. Ne basılacak?
   -> satırın kendisi basılacak

Kod:
"""

print("\nÖRNEK 2")
for satir in range(1, 4):
    for _ in range(satir):
        print(satir, end="")
    print()

"""
Burada yıldız yerine satir değişkenini bastık.

Yani:
- satir = 1 iken -> 1 bir kez
- satir = 2 iken -> 2 iki kez
- satir = 3 iken -> 3 üç kez

DEMek ki pattern değiştirmenin yollarından biri şu:
İç döngü aynı kalır, print içeriği değişir.

Önceki örnekte:
print("*", end="")

Bu örnekte:
print(satir, end="")
"""


# =========================================================
# 5) ÖRNEK 3 - HER SATIRDA AYNI DİZİYİ BASMA
# =========================================================

"""
İstenen çıktı:

123
123
123

Analiz:
1. Kaç satır var?
   -> 3

2. Her satırda kaç eleman var?
   -> 3

3. Ne basılacak?
   -> 1, 2, 3

Kod:
"""

print("\nÖRNEK 3")
for satir in range(3):
    for sayi in range(1, 4):
        print(sayi, end="")
    print()

"""
Burada dış döngü sadece 3 satır oluşturuyor.
Asıl satır içeriğini iç döngü belirliyor.

İç döngü her seferinde:
1, 2, 3 üretip bastırıyor.

Önemli fark:
Bazı patternlerde eleman sayısı artar/azalır.
Bazılarında eleman sayısı sabittir.

Burada sabit:
Her satırda 3 eleman var.
"""


# =========================================================
# 6) SABİT / ARTAN / AZALAN ELEMAN SAYISI
# =========================================================

"""
Pattern çözerken eleman sayısının davranışını görmek çok önemlidir.

A) SABİT ELEMAN SAYISI
Örnek:
**
**
**

Her satırda 2 eleman var.
Değişmiyor.

B) ARTAN ELEMAN SAYISI
Örnek:
*
**
***

Her satırda eleman sayısı artıyor.
1, 2, 3...

C) AZALAN ELEMAN SAYISI
Örnek:
***
**
*

Her satırda eleman sayısı azalıyor.
3, 2, 1...

Bu ayrımı görmeden pattern çözmek zordur.
"""


# =========================================================
# 7) AZALAN PATTERN ÖRNEĞİ
# =========================================================

"""
İstenen çıktı:

4444
333
22
1

Analiz:
1. Kaç satır var?
   -> 4

2. Her satırda kaç eleman var?
   -> 4, 3, 2, 1

3. Ne basılacak?
   -> satır değeri basılacak

Kod:
"""

print("\nÖRNEK 4")
for satir in range(4, 0, -1):
    for _ in range(satir):
        print(satir, end="")
    print()

"""
Burada dış döngü tersten gidiyor:
4, 3, 2, 1

Bu yüzden hem:
- basılan sayı azalıyor
- tekrar sayısı azalıyor

range(4, 0, -1) ifadesi çok önemli.
Anlamı:
4'ten başla,
0'a kadar git ama 0 dahil olmasın,
her adımda 1 azalt.
"""


# =========================================================
# 8) RANGE HATIRLATMASI
# =========================================================

"""
range kullanımı nested loop'ta çok kritik.

range(3)
-> 0, 1, 2

range(1, 4)
-> 1, 2, 3

range(4, 0, -1)
-> 4, 3, 2, 1

En çok hata yapılan noktalardan biri budur.

Özellikle şu iki kullanım çok önemlidir:

Artan kullanım:
for satir in range(1, 5):

Azalan kullanım:
for satir in range(4, 0, -1):
"""


# =========================================================
# 9) "_" NE ZAMAN KULLANILIR?
# =========================================================

"""
Python'da "_" genelde şu anlamda kullanılır:
"Bu değişkenin ismi önemli değil, değerini kullanmıyorum."

Örnek:
"""

print("\nÖRNEK 5")
for _ in range(3):
    print("Merhaba")

"""
Burada _ mantıklı.
Çünkü sayaç değerini kullanmıyoruz.

Ama şunu yapıyorsan:

for _ in range(3):
    print(_, end="")

o zaman artık değeri kullanıyorsun.
Bu durumda "_" yerine anlamlı isim vermek daha temiz olur:

for sayi in range(3):
    print(sayi, end="")

Bu profesyonel yazım alışkanlığı açısından önemlidir.
"""


# =========================================================
# 10) NESTED LOOP'TA EN ÇOK KARIŞAN ŞEY
# =========================================================

"""
Başlangıçta en çok karışan şey şudur:

"Dış döngü ne yapıyor, iç döngü ne yapıyor?"

Bunu netleştirelim.

Örnek:
"""

print("\nÖRNEK 6")
for satir in range(3):
    for sutun in range(4):
        print("#", end="")
    print()

"""
Bu kodun anlamı:
- 3 satır oluştur
- her satıra 4 tane # koy

Yani:
Dış döngü = kaç satır?
İç döngü = satırın içine kaç şey?

Bu mantığı her soruda tekrar tekrar düşün.
"""


# =========================================================
# 11) BİR PATTERN'İ KODA ÇEVİRME ADIMLARI
# =========================================================

"""
Bir pattern gördüğünde şu adımları uygula:

ADIM 1:
Çıktıyı dikkatlice oku

ADIM 2:
Kaç satır var bul

ADIM 3:
Her satırda kaç eleman var bul

ADIM 4:
Neyin basıldığını bul
- yıldız mı?
- satır numarası mı?
- sayı dizisi mi?

ADIM 5:
Dış döngüyü kur
- satır sayısına göre

ADIM 6:
İç döngüyü kur
- tekrar sayısına göre

ADIM 7:
print içine doğru değeri koy

Bu yöntemle kafa karışıklığı ciddi azalır.
"""


# =========================================================
# 12) MİNİ KARŞILAŞTIRMA TABLOSU
# =========================================================

"""
PATTERN 1
---------
*
**
***

Analiz:
- 3 satır
- 1,2,3 eleman
- * basılacak


PATTERN 2
---------
1
22
333

Analiz:
- 3 satır
- 1,2,3 eleman
- satır değeri basılacak


PATTERN 3
---------
123
123
123

Analiz:
- 3 satır
- her satırda 3 eleman
- 1,2,3 basılacak


PATTERN 4
---------
4444
333
22
1

Analiz:
- 4 satır
- 4,3,2,1 eleman
- satır değeri basılacak
"""

# Kodlarla gösterelim:

print("\nPATTERN 1")
for satir in range(1, 4):
    for _ in range(satir):
        print("*", end="")
    print()

print("\nPATTERN 2")
for satir in range(1, 4):
    for _ in range(satir):
        print(satir, end="")
    print()

print("\nPATTERN 3")
for satir in range(3):
    for sayi in range(1, 4):
        print(sayi, end="")
    print()

print("\nPATTERN 4")
for satir in range(4, 0, -1):
    for _ in range(satir):
        print(satir, end="")
    print()


# =========================================================
# 13) AKAN SAYI PATTERN'LERİ NEDEN FARKLI?
# =========================================================

"""
Şu pattern'e bak:

12
34
56

Bu, önceki örneklerden biraz farklıdır.
Çünkü sayı her satırda başa dönmüyor.
Akıp devam ediyor.

Bu tür sorularda ekstra sayaç gerekir.

Örnek:
"""

print("\nÖRNEK 7 - AKAN SAYI")
sayi = 1

for satir in range(3):
    for _ in range(2):
        print(sayi, end="")
        sayi += 1
    print()

"""
Bu konu nested loop'un bir sonraki katmanıdır.

Yani:
- temel pattern mantığı ayrı
- akan sayaç gerektiren pattern ayrı

Bugün ana hedef temel mantıktı.
Bu yüzden akan sayı kısmı "bonus farkındalık" olarak görülmeli.
Kafa karıştırırsa sorun yok.
Zamanla oturur.
"""


# =========================================================
# 14) BAŞLANGIÇTA YAPILAN YAYGIN HATALAR
# =========================================================

"""
1) Satır sayısı ile eleman sayısını karıştırmak
Örnek:
12
12
12

Burada 3 satır vardır, 2 değil.

2) "_" değişkenini değeri kullanıldığı halde kullanmak
Eğer sayı basacaksan "_" yerine anlamlı isim kullan.

3) range'in 0'dan başladığını unutmak
range(3) -> 0,1,2
range(1,4) -> 1,2,3

4) print() ile print(..., end="") farkını unutmak
print(..., end="") aynı satırda devam eder
print() alt satıra geçirir

5) Analiz yapmadan direkt kod yazmaya çalışmak
Bu en büyük hatalardan biridir.
Önce pattern okunur, sonra kod yazılır.
"""


# =========================================================
# 15) BUGÜNÜN EN ÖNEMLİ CÜMLESİ
# =========================================================

"""
Nested loop konusunda bugünün en önemli cümlesi şudur:

DIŞ DÖNGÜ SATIRI YÖNETİR,
İÇ DÖNGÜ SATIRIN İÇİNİ DOLDURUR.

Bunu gerçekten anlarsan konu zamanla çok daha rahat oturur.
"""


# =========================================================
# 16) KISA KENDİNİ KONTROL SORULARI
# =========================================================

"""
Aşağıdaki patternleri analiz etmeye çalış:

1)
**
**
**

Sor:
- kaç satır var?
- her satırda kaç eleman var?
- ne basılacak?

2)
1
22
333

3)
1234
1234
1234

4)
444
33
2

5)
11
22
33

Koddan önce sadece analiz yap.
Bu çok önemli.
"""


# =========================================================
# 17) GÜN SONU ÖZETİ
# =========================================================

"""
Bugün öğrenilenler:

- Nested loop = döngü içinde döngü
- Dış döngü satırı yönetir
- İç döngü satırın içini doldurur
- Pattern analizinde 3 temel soru vardır:
    1. Kaç satır var?
    2. Her satırda kaç eleman var?
    3. Ne basılacak?
- Patternler sabit, artan veya azalan eleman sayısına sahip olabilir
- Bazı patternlerde sayı her satırda başa döner
- Bazılarında akarak devam eder (ileri seviye katman)

EN ÖNEMLİ GERÇEK:
Bu konu ilk günde tamamen taş gibi oturmak zorunda değildir.
Tekrarla ve örnekle netleşir.

Yani bugün eksik hissetmek normaldir.
Önemli olan mantık çekirdeğinin oluşmasıdır.
"""