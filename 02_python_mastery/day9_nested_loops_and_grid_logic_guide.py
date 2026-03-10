"""
Day 9 - Nested Loops and Grid Logic
==================================

Bugünün konusu:
- Nested loop nedir?
- Outer loop / inner loop farkı
- Pattern mantığı
- Artan / azalan yapı kurma
- Sayı patternleri
- Grid mantığı
- Liste içinde liste yapısı
- Grid traversal (satır ve eleman gezme)

Bu dosya öğretici rehber olarak hazırlanmıştır.
Amaç:
Sadece kod ezberlemek değil, mantığı gerçekten oturtmak.

--------------------------------------------------------------------
1) NESTED LOOP NEDİR?
--------------------------------------------------------------------

Nested loop = döngü içinde döngü demektir.

Yani bir for döngüsünün içinde başka bir for döngüsü vardır.

Genel mantık:

- Dış döngü (outer loop) -> satırları kontrol eder
- İç döngü (inner loop) -> o satırın içini doldurur

En temel düşünce şekli:

"Kaç satır olacak?"
sorusunu dış döngü cevaplar.

"Her satırın içinde kaç şey olacak?"
sorusunu iç döngü cevaplar.

Örnek düşünce:

3 satır olsun.
Her satırda 4 yıldız olsun.

Bu durumda:
- dış döngü 3 kez döner
- iç döngü her satırda 4 kez döner

--------------------------------------------------------------------
2) OUTER LOOP VE INNER LOOP FARKI
--------------------------------------------------------------------

Outer loop:
- satır sayısını belirler
- yeni satır mantığını taşır

Inner loop:
- o satırın içeriğini üretir
- karakterleri, sayıları, elemanları yan yana basar

Şunu asla unutma:

Dış döngü tek başına genelde "kaç satır" bilgisini verir.
İç döngü ise "bir satırın içi nasıl dolacak?" sorusunu çözer.

Mini örnek:

for satir in range(3):
    for sutun in range(3):
        print("*", end="")
    print()

Burada:
- satir -> 3 satır üretir
- sutun -> her satıra 3 yıldız koyar
- print() -> satır bitince alt satıra geçer

Çıktı:
***
***
***

--------------------------------------------------------------------
3) EN TEMEL NESTED LOOP ÖRNEĞİ
--------------------------------------------------------------------
"""

for satir in range(3):
    for sutun in range(3):
        print("*", end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Yukarıdaki kodun mantığı:

1. dış döngü başlar
2. iç döngü çalışır ve *** basar
3. satır bitince print() alt satıra geçirir
4. dış döngü tekrar eder
5. yine *** basılır
6. bu işlem 3 kez olur

--------------------------------------------------------------------
4) SABİT PATTERN
--------------------------------------------------------------------

Hedef:
****
****
****

Burada:
- 3 satır var
- her satırda 4 yıldız var
"""

for satir in range(3):
    for sutun in range(4):
        print("*", end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
--------------------------------------------------------------------
5) ARTAN YILDIZ PATTERNİ
--------------------------------------------------------------------

Hedef:
*
**
***
****

Burada mantık değişiyor:
- satır ilerledikçe yıldız sayısı artıyor

Yani:
1. satır -> 1 yıldız
2. satır -> 2 yıldız
3. satır -> 3 yıldız
4. satır -> 4 yıldız

Dikkat:
İç döngünün dönüş sayısı sabit değil.
satir değişkenine bağlı.

Kod:
"""

for satir in range(1, 5):
    for sutun in range(satir):
        print("*", end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
range(1, 5) -> 1, 2, 3, 4 üretir

satir = 1 iken:
iç döngü 1 kez döner -> *

satir = 2 iken:
iç döngü 2 kez döner -> **

satir = 3 iken:
iç döngü 3 kez döner -> ***

satir = 4 iken:
iç döngü 4 kez döner -> ****

--------------------------------------------------------------------
6) AZALAN YILDIZ PATTERNİ
--------------------------------------------------------------------

Hedef:
****
***
**
*

Burada iç döngü bu kez her satırda azalır.
"""

for satir in range(4, 0, -1):
    for sutun in range(satir):
        print("*", end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 4 -> 4 yıldız
satir = 3 -> 3 yıldız
satir = 2 -> 2 yıldız
satir = 1 -> 1 yıldız

--------------------------------------------------------------------
7) AYNI SAYIYI TEKRAR EDEN PATTERN
--------------------------------------------------------------------

Hedef:
111
222
333

Burada:
- dış döngü satırın değerini belirler
- iç döngü o değeri tekrar eder
"""

for satir in range(1, 4):
    for sutun in range(3):
        print(satir, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 1 -> 111
satir = 2 -> 222
satir = 3 -> 333

Burada önemli detay:
Basılan şey sutun değil, satir.

Çünkü her satırda aynı sayı tekrar ediliyor.

--------------------------------------------------------------------
8) AYNI SAYI DİZİSİNİ TEKRAR ETME
--------------------------------------------------------------------

Hedef:
123
123
123

Burada:
- dış döngü 3 satır üretir
- iç döngü her satırda 1 2 3 basar
"""

for satir in range(3):
    for sutun in range(1, 4):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Burada basılan şey sutun değişkenidir.
Çünkü her satırda 1'den 3'e kadar gitmek istiyoruz.

--------------------------------------------------------------------
9) ARTAN SAYI PATTERNİ
--------------------------------------------------------------------

Hedef:
1
12
123
1234

Burada mantık:
- satır büyüdükçe
- iç döngü daha fazla sayı üretir
"""

for satir in range(1, 5):
    for sutun in range(1, satir + 1):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Açıklama:
satir = 1 -> range(1, 2) -> 1
satir = 2 -> range(1, 3) -> 1 2
satir = 3 -> range(1, 4) -> 1 2 3
satir = 4 -> range(1, 5) -> 1 2 3 4

Buradaki kilit nokta:
range(1, satir + 1)

Eğer yanlışlıkla hep range(1, 5) yazarsan:
her satır aynı olur ve 1234 tekrar tekrar basılır.

--------------------------------------------------------------------
10) AZALAN SAYI PATTERNİ
--------------------------------------------------------------------

Hedef:
1234
123
12
1
"""

for satir in range(4, 0, -1):
    for sutun in range(1, satir + 1):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 4 -> 1 2 3 4
satir = 3 -> 1 2 3
satir = 2 -> 1 2
satir = 1 -> 1

--------------------------------------------------------------------
11) TERS AZALAN SAYI PATTERNİ
--------------------------------------------------------------------

Hedef:
4321
321
21
1

Burada:
- satır uzunluğu azalıyor
- ama içerik büyükten küçüğe yazılıyor
"""

for satir in range(4, 0, -1):
    for sutun in range(satir, 0, -1):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 4 -> 4 3 2 1
satir = 3 -> 3 2 1
satir = 2 -> 2 1
satir = 1 -> 1

--------------------------------------------------------------------
12) HER SATIRDA AYNI SAYI, SAYI KADAR BASILSIN
--------------------------------------------------------------------

Hedef:
1
22
333
4444
"""

for satir in range(1, 5):
    for sutun in range(satir):
        print(satir, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 1 -> 1 tane 1
satir = 2 -> 2 tane 2
satir = 3 -> 3 tane 3
satir = 4 -> 4 tane 4

Tersi de mümkündür.

Hedef:
4444
333
22
1
"""

for satir in range(4, 0, -1):
    for sutun in range(satir):
        print(satir, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
--------------------------------------------------------------------
13) BAŞLANGIÇ DEĞERİ KAYAN PATTERN
--------------------------------------------------------------------

Hedef:
1234
234
34
4

Burada her satırın başlangıcı değişiyor.
"""

for satir in range(1, 5):
    for sutun in range(satir, 5):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 1 -> 1 2 3 4
satir = 2 -> 2 3 4
satir = 3 -> 3 4
satir = 4 -> 4

--------------------------------------------------------------------
14) TERS YÖNDE BÜYÜYEN PATTERN
--------------------------------------------------------------------

Hedef:
4
43
432
4321
"""

for satir in range(1, 5):
    for sutun in range(4, 4 - satir, -1):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Mantık:
satir = 1 -> 4
satir = 2 -> 4 3
satir = 3 -> 4 3 2
satir = 4 -> 4 3 2 1

Benzer başka bir örnek:

Hedef:
1
21
321
4321
"""

for satir in range(1, 5):
    for sutun in range(satir, 0, -1):
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
--------------------------------------------------------------------
15) GRID NEDİR?
--------------------------------------------------------------------

Grid = satır ve sütun mantığıyla düşünülen yapı.

Python'da bunun en temel hali:
liste içinde liste yapısıdır.

Örnek:
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Grid yapısı:")
print(grid)

print("\n" + "=" * 60 + "\n")

"""
Bu yapı şunu temsil eder:

[1, 2, 3] -> 1. satır
[4, 5, 6] -> 2. satır
[7, 8, 9] -> 3. satır

Buna tablo gibi bakabiliriz:

1 2 3
4 5 6
7 8 9

Yani:
- 3 satır var
- her satırda 3 eleman var

--------------------------------------------------------------------
16) GRID NEDEN LİSTE İÇİNDE LİSTE?
--------------------------------------------------------------------

Çünkü tek bir düz liste sadece sırayla eleman tutar.

Ama grid'de ihtiyacımız olan şey:
- satır bilgisi
- sütun bilgisi

Mesela:
grid[0] -> ilk satır
grid[1] -> ikinci satır
grid[2] -> üçüncü satır

Ve daha derine inersek:
grid[0][0] -> 1
grid[0][1] -> 2
grid[0][2] -> 3

grid[1][0] -> 4
grid[1][1] -> 5
grid[1][2] -> 6

grid[2][0] -> 7
grid[2][1] -> 8
grid[2][2] -> 9

--------------------------------------------------------------------
17) GRID'DE TEK DÖNGÜ İLE SATIRLARI YAZDIRMA
--------------------------------------------------------------------
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in grid:
    print(satir)

print("\n" + "=" * 60 + "\n")

"""
Çıktı:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Burada:
- satir değişkeni tek tek alt listeleri alır

Yani sırayla:
satir = [1, 2, 3]
satir = [4, 5, 6]
satir = [7, 8, 9]

--------------------------------------------------------------------
18) GRID'DE NESTED LOOP İLE ELEMANLARI YAZDIRMA
--------------------------------------------------------------------

Hedef:
123
456
789
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in grid:
    for sutun in satir:
        print(sutun, end="")
    print()

print("\n" + "=" * 60 + "\n")

"""
Burada:
- dış döngü satırları gezer
- iç döngü satırın içindeki elemanları gezer

Bu nested loop'un grid üzerindeki en temiz kullanımlarından biridir.

--------------------------------------------------------------------
19) GRID'DEKİ HER ELEMANI AYRI SATIRDA YAZDIRMA
--------------------------------------------------------------------
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in grid:
    for sutun in satir:
        print(sutun)

print("\n" + "=" * 60 + "\n")

"""
Çıktı:
1
2
3
4
5
6
7
8
9

Burada iç döngüde end="" kullanmadık.
Bu yüzden her eleman ayrı satıra düştü.

--------------------------------------------------------------------
20) SATIRLARI ETİKETLEYEREK YAZDIRMA
--------------------------------------------------------------------
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in grid:
    print("Satır:", satir)

print("\n" + "=" * 60 + "\n")

"""
Çıktı:
Satır: [1, 2, 3]
Satır: [4, 5, 6]
Satır: [7, 8, 9]

Bu örnek, dış döngünün gerçekten "satırları" gezdiğini net gösterir.

--------------------------------------------------------------------
21) ELEMANLARI ETİKETLEYEREK YAZDIRMA
--------------------------------------------------------------------
"""

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in grid:
    for sutun in satir:
        print("Eleman:", sutun)

print("\n" + "=" * 60 + "\n")

"""
Bu örnek de iç döngünün elemanları gezdiğini net gösterir.

--------------------------------------------------------------------
22) GRID'DE SATIR VE SÜTUN MANTIĞI
--------------------------------------------------------------------

Genel kural:
grid[satir_index][sutun_index]

Örnek:
grid[1][2]

Adım adım:
- grid[1] -> ikinci satır -> [4, 5, 6]
- [2] -> onun üçüncü elemanı -> 6

Yani:
grid[1][2] = 6

Başka örnekler:
grid[0][2] = 3
grid[2][0] = 7
grid[1][1] = 5

Bu mantık ileride şunlarda çok önemlidir:
- oyun haritaları
- 2D yapı
- tablo işleme
- matris mantığı
- koordinat sistemi

--------------------------------------------------------------------
23) NEDEN TEK DÖNGÜ BAZEN YETMEZ?
--------------------------------------------------------------------

Çünkü grid iki katmanlıdır.

Tek döngü ile:
- satırların tamamını görebilirsin

Ama satır içindeki elemanları tek tek işlemek için:
- ikinci döngü gerekir

Örnek:
for satir in grid:
    print(satir)

Bu satırları basar ama elemanları parçalamaz.

Elemanları tek tek işlemek için:
for satir in grid:
    for sutun in satir:
        print(sutun)

gibi bir yapı gerekir.

--------------------------------------------------------------------
24) SIK YAPILAN HATALAR
--------------------------------------------------------------------

1. Dış döngü ile iç döngüyü karıştırmak
Yanlış düşünce:
- iç döngü satır gezer

Doğrusu:
- dış döngü satır gezer
- iç döngü o satırın içini gezer

2. İç döngü sınırını sabit bırakmak
Örnek:
range(1, 5)

Bu sabit olduğu için her satırda aynı çıktıyı verir.
Eğer satıra göre büyüyen/azalan yapı istiyorsan,
sınır satira bağlı olmalıdır.

3. end="" unutmak
Yan yana yazılması gereken yapıda end="" unutulursa,
her şey alt alta basılır.

4. Satır bittikten sonra print() koymamak
Bu durumda tüm çıktı tek satıra yapışabilir.

5. Grid tanımında virgül unutmak
Yanlış:
grid = [
    [1, 2, 3]
    [4, 5, 6]
]

Doğru:
grid = [
    [1, 2, 3],
    [4, 5, 6]
]

6. print(grid) ile satır satır yazdırmayı karıştırmak
print(grid) tüm yapıyı tek parça gösterir.
Satır satır için döngü gerekir.

--------------------------------------------------------------------
25) MİNİ SORU - CEVAP
--------------------------------------------------------------------

Soru: Nested loop nedir?
Cevap: Döngü içinde döngüdür.

Soru: Outer loop ne yapar?
Cevap: Satırları kontrol eder.

Soru: Inner loop ne yapar?
Cevap: Satırın içini doldurur.

Soru: Grid nedir?
Cevap: Liste içinde liste yapısıyla temsil edilen satır-sütun mantığıdır.

Soru: Neden nested loop grid için önemlidir?
Cevap: Çünkü önce satıra, sonra satırın içindeki elemana ulaşmak gerekir.

Soru: 1 / 12 / 123 gibi patternlerde iç döngü neden sabit olamaz?
Cevap: Çünkü her satırda eleman sayısı değişir.

Soru: 111 / 222 / 333 ile 123 / 123 / 123 arasındaki temel fark nedir?
Cevap:
- İlkinde satıra göre basılan değer değişir
- İkincisinde satıra göre değişmeyen sabit dizi tekrar edilir

--------------------------------------------------------------------
26) BUGÜN NE ÖĞRENDİK?
--------------------------------------------------------------------

Bugün şunları öğrendik:

- Nested loop mantığı
- Outer loop / inner loop farkı
- Sabit pattern kurma
- Artan yıldız patterni
- Azalan yıldız patterni
- Aynı sayı tekrar patterni
- Artan sayı patterni
- Azalan sayı patterni
- Ters pattern mantığı
- Grid = liste içinde liste mantığı
- Grid satırlarını yazdırma
- Grid elemanlarını yazdırma
- Grid traversal

--------------------------------------------------------------------
27) KENDİ KENDİNE PRATİK GÖREVLERİ
--------------------------------------------------------------------

Aşağıdakileri yardım almadan yazmayı dene:

1)
**
**

2)
***
***
***
***

3)
1
12
123
1234

4)
1234
123
12
1

5)
111
222
333
444

6)
4444
333
22
1

7)
1234
234
34
4

8)
4321
321
21
1

9)
Grid:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Çıktı:
123
456
789

10)
Aynı grid ile:
Eleman: 1
Eleman: 2
...
Eleman: 9

--------------------------------------------------------------------
28) SON SÖZ
--------------------------------------------------------------------

Bugünün en önemli cümlesi şudur:

Dış döngü satırları gezer.
İç döngü satırın içini doldurur.

Eğer bu cümle gerçekten oturduysa,
nested loop konusu büyük ölçüde oturmuştur.

Pattern sorularında asıl mesele kod ezberlemek değildir.
Asıl mesele şunu görmektir:

- Kaç satır var?
- Her satırda kaç eleman var?
- Bu sayı sabit mi, artıyor mu, azalıyor mu?
- Basılan şey yıldız mı, sayı mı, o anki satır mı, o anki sütun mu?

Bu soruları doğru sorarsan,
pattern ve grid sorularının çoğunu çözebilirsin.
"""