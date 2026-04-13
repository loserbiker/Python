# ============================================================
# PYTHON KAMP
# Gün 1–6 Hatırlatma / Özet Rehberi
# Dosya adı önerisi: day1_to_day6_recap_guide.py
# ============================================================

"""
Bu dosya, Gün 1 ile Gün 6 arasında çalışılan temel konuları
tek yerde toparlamak için hazırlanmış detaylı bir hatırlatma rehberidir.

Bu rehberin amacı:
- ilk 6 günü tekrar etmek
- kritik mantıkları yeniden netleştirmek
- birbirine bağlı konuları bir arada görmek
- unutulan yerleri hızlıca yakalamak
- yeni güne geçmeden önce temel zemini sağlamlaştırmak

Bu dosya "ilk kez öğretme" kadar detaylı,
ama aynı zamanda "hatırlatma rehberi" gibi kullanılabilecek şekilde yazılmıştır.

Kapsam:
1) Değişken mantığı + referans
2) Bellek modeli + id()
3) Veri tipleri derin kullanım
4) Operatörler + truthy/falsy
5) if / elif / else ileri kullanım
6) Karar ağacı egzersizleri + koşul akışı

Bu ilk 6 gün neden çok önemli?

Çünkü programlamada sonraki her konu:
- döngüler
- listeler
- fonksiyonlar
- OOP
- veri işleme
- mini projeler

bu ilk taşların üstüne kurulacak.

Yani bu rehber aslında senin temel omurgandır.
"""


# ============================================================
# GUN 1 — DEGISKEN MANTIGI + REFERANS
# ============================================================

"""
Gün 1'in ana fikri şuydu:

Değişken bir "kutu" değildir.
Değişken, bir objeye bağlanan isimdir.

Yani Python'da:

a = 5

yazdığında, "a isimli kutunun içine 5 koymak" gibi düşünmek
başlangıç için işe yarasa da tam doğru model değildir.

Daha doğru model:

- 5 diye bir obje var
- a ismi bu objeye bağlanıyor
"""

a = 5

# Bunu zihinde şöyle canlandır:
#
# a ─────► 5

"""
Buradaki en kritik düşünce:
assignment (=), matematikteki "eşittir" gibi değil;
bağlama / ilişkilendirme işlemidir.
"""

b = a

# Şimdi:
#
# a ─────► 5
# b ─────► 5

"""
Burada a ile b aynı integer objesini referans edebilir.
Bu "a ile b aynı değişken oldu" demek değildir.
Sadece aynı objeye bakıyorlar.

Sonra:
"""

a = 10

# Artık:
#
# a ─────► 10
# b ─────► 5

"""
Buradaki en kritik sonuç:

a'yı değiştirince b otomatik değişmedi.

Neden?
Çünkü sen 5 objesini değiştirmedin.
a ismini yeni bir objeye bağladın.

Bu fark çok önemli:
- objeyi değiştirmek (mutation)
- ismi başka objeye bağlamak (rebinding)

ilk günün ana kazanımı buydu.
"""


# ============================================================
# GUN 1 — ANA CUMLELER
# ============================================================

"""
Hatırlamak için kısa cümleler:

- Değişken = isim / referans etiketi
- "=" = atama değil, bağlama gibi düşün
- Aynı obje birden fazla isim tarafından referans edilebilir
- Bir ismin başka objeye bağlanması, diğer ismi zorunlu olarak etkilemez
"""


# ============================================================
# GUN 1 — MINI ORNEKLER
# ============================================================

x = 100
y = x
x = 200

print(x)  # 200
print(y)  # 100

"""
Neden?
Çünkü x yeniden bağlandı.
y eski objeyi göstermeye devam etti.
"""

isim1 = "Can"
isim2 = isim1
isim1 = "Harley"

print(isim1)  # Harley
print(isim2)  # Can

"""
Mantık yine aynı.
İsim1 yeni string objesine bağlandı.
İsim2 eski objeyi gösterdi.
"""


# ============================================================
# GUN 2 — BELLEK MODELI + id()
# ============================================================

"""
Gün 2'de odak şuydu:

Python'da objeler bellekte yaşar.
Değişkenler ise bu objelere bağlanan isimlerdir.

Bu düşünceyi daha somut görmek için id() kullanılır.
"""

a = 5
b = a

print(id(a))
print(id(b))

"""
Eğer aynı objeyi referans ediyorlarsa id değerleri aynı olabilir.

id() ne verir?

Basit düşünceyle:
- objenin kimliği
- o anda onu ayırt eden benzersiz kimlik

Bunu "bellekteki tam adres" gibi öğretmek bazen fazla kaba olabilir,
ama başlangıç seviyesinde "kimlik" mantığı yeterlidir.
"""


# ============================================================
# GUN 2 — BELLEKTE NE OLUYOR?
# ============================================================

"""
Örnek:
"""

a = 5
b = a

# Muhtemel düşünce modeli:
#
# a ─────► (5 objesi)  id: X
# b ─────► (5 objesi)  id: X

a = 10

# Sonra:
#
# a ─────► (10 objesi) id: Y
# b ─────► (5 objesi)  id: X

"""
Burada dikkat:
id() sana "şu an hangi objeye bağlı olduğunu" anlamada yardımcı olur.
Ama asıl amaç id() ezberlemek değil;
bellek modelini kavramaktır.
"""


# ============================================================
# GUN 2 — IMMUTABLE MANTIK GIRISI
# ============================================================

"""
Bu günün bir alt kazanımı da immutable mantığa girişti.

int, str gibi tiplerde çoğu zaman
"objeyi yerinde değiştirme" değil,
"yeni obje oluşturma ve yeniden bağlama" görürüz.

Örnek:
"""

s = "python"
print(id(s))

s = s + "3"
print(id(s))

"""
id değişebilir.
Bu da çoğu durumda yeni obje oluştuğunu düşündürür.

Burada ana fikir:
Python'da her şeyi yüzeysel kopyalama gibi düşünme.
Bağlantı / obje / kimlik mantığını anlamaya çalış.
"""


# ============================================================
# GUN 2 — ANA CUMLELER
# ============================================================

"""
- Objeler bellekte yaşar
- Değişkenler objelere bağlanan isimlerdir
- id() obje kimliğini görmeye yardım eder
- Aynı id -> aynı obje olma ihtimali
- Yeniden bağlama ile obje değiştirme farklı şeylerdir
"""


# ============================================================
# GUN 3 — VERI TIPLERI DERIN KULLANIM
# ============================================================

"""
Gün 3'te konu sadece "int, str, bool nedir" değildi.
Asıl hedef:
veri tiplerinin davranışlarını anlamaktı.

Başlangıç veri tipleri:
- int
- float
- str
- bool
- NoneType (None mantığına giriş)
"""

sayi = 10
ondalik = 3.14
isim = "Can"
durum = True
bos = None

print(type(sayi))
print(type(ondalik))
print(type(isim))
print(type(durum))
print(type(bos))

"""
Bu günün önemli noktası:
Her veri tipinin davranışı farklıdır.
Aynı operatör farklı tiplerde farklı anlam taşıyabilir.
"""


# ============================================================
# GUN 3 — STR ONEMLIDIR
# ============================================================

"""
String sadece "yazı" değildir.
Programlamada veri taşıyan çok önemli bir yapıdır.
"""

ad = "Python"
print(ad[0])     # P
print(len(ad))   # 6

"""
Henüz listelere geçmeden bile şunu gördün:
bazı veri tipleri üzerinde işlem yapılabilir,
uzunluk alınabilir,
indeks mantığı olabilir.
"""

"""
Str ile int farkı:
"""

yas = "20"
gercek_yas = 20

print(type(yas))        # str
print(type(gercek_yas)) # int

"""
Görüntü olarak benzeseler bile davranışları farklıdır.
"""


# ============================================================
# GUN 3 — BOOL MANTIGI
# ============================================================

"""
Bool sadece True / False demek değildir.
Koşul sisteminin temelidir.
"""

aktif = True
print(type(aktif))

"""
İleride if yapılarını yöneten şey de çoğu zaman bool mantığıdır.
Karşılaştırmalar sonunda genelde bool elde ederiz.
"""

print(5 > 3)   # True
print(2 == 7)  # False


# ============================================================
# GUN 3 — NONE GIRISI
# ============================================================

"""
None, "hiçbir şey yok" ile "0" veya "" aynı şey değildir.

None genelde:
- değer henüz yok
- atanmamış
- özel boşluk durumu

gibi anlamlar taşır.
"""

veri = None
print(veri is None)  # True

"""
None ileride çok karşına çıkacak.
Şimdilik bunu "özel boş değer" gibi düşünmek yeterli.
"""


# ============================================================
# GUN 3 — ANA CUMLELER
# ============================================================

"""
- type() veri tipini gösterir
- Aynı görünen değerler farklı tiplerde olabilir
- String, sayı değildir
- Bool, koşul sisteminin temelidir
- None, özel boşluk/değer yokluğu halidir
"""


# ============================================================
# GUN 4 — OPERATORLER + TRUTHY / FALSY
# ============================================================

"""
Gün 4, iki temel parçadan oluşuyordu:
1) operatörler
2) truthy / falsy

Önce operatörler:
- aritmetik
- karşılaştırma
- mantıksal operatörler
"""

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3

"""
Özellikle:
%  -> kalan
// -> tam bölme
** -> üs alma

bu üçlü çok önemli.
"""


# ============================================================
# GUN 4 — KARŞILAŞTIRMA OPERATORLERI
# ============================================================

print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(4 <= 2)   # False
print(7 == 7)   # True
print(7 != 7)   # False

"""
Bu operatörler bool döndürür.
Yani if sisteminin yakıtıdır.
"""


# ============================================================
# GUN 4 — MANTIKSAL OPERATORLER
# ============================================================

"""
and, or, not
"""

print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

"""
Mini mantık:
- and -> iki taraf da doğru olmalı
- or  -> en az biri doğru olmalı
- not -> tersine çevirir
"""


# ============================================================
# GUN 4 — TRUTHY / FALSY NEDIR?
# ============================================================

"""
Python'da her şey doğrudan True/False yazmak zorunda değildir.
Bazı değerler koşul içinde True gibi,
bazıları False gibi davranır.

Falsy örnekler:
- 0
- 0.0
- ""
- []
- {}
- set()
- None
- False

Truthy örnekler:
- 1
- -5
- "a"
- " "
- [0]
- {"x": 1}
- True
"""

print(bool(0))     # False
print(bool(""))    # False
print(bool(" "))   # True
print(bool([]))    # False
print(bool([0]))   # True
print(bool(None))  # False

"""
Burada çok kritik tuzak:
" " boş string değildir.
İçinde bir boşluk karakteri vardır.
Bu yüzden truthy'dir.

Aynı şekilde [0] boş liste değildir.
İçinde eleman vardır.
Bu yüzden truthy'dir.
"""


# ============================================================
# GUN 4 — NEDEN ONEMLI?
# ============================================================

"""
Çünkü koşullarda şunu yazabilirsin:
"""

isim = ""

if isim:
    print("isim var")
else:
    print("isim boş")

"""
Burada Python isim değişkeninin truthy/falsy durumuna bakar.

Bu mantık ileride:
- input kontrolü
- boş liste kontrolü
- veri var mı yok mu
- dosya içeriği boş mu

gibi yerlerde çok işine yarayacak.
"""


# ============================================================
# GUN 4 — MODULO ILE TEK / CIFT
# ============================================================

"""
Gün 4'ün en pratik kaslarından biri de şuydu:
"""

sayi = 8

if sayi % 2 == 0:
    print("çift")
else:
    print("tek")

"""
% 2 == 0 -> çift kontrolü
% 2 != 0 -> tek kontrolü

Bu pattern algoritmalarda sürekli kullanılır.
"""


# ============================================================
# GUN 4 — ANA CUMLELER
# ============================================================

"""
- Karşılaştırmalar bool üretir
- and / or / not koşulları birleştirir
- Her değer koşulda bool gibi davranabilir
- Boş yapılar genelde falsy'dir
- Dolu yapılar genelde truthy'dir
- " " ile "" aynı şey değildir
- [0] ile [] aynı şey değildir
"""


# ============================================================
# GUN 5 — if / elif / else ILERI KULLANIM
# ============================================================

"""
Gün 5'in ana konusu:
karar verme yapılarının daha sistemli kullanımıydı.

Temel yapı:
"""

notu = 75

if notu >= 85:
    print("Pekiyi")
elif notu >= 70:
    print("İyi")
else:
    print("Geliştirilmeli")

"""
Buradaki mantık:
- ilk koşulu kontrol et
- olmazsa elif'e geç
- o da olmazsa else

Çok önemli nokta:
elif zincirinde ilk doğru blok çalışır.
Devamı kontrol edilmez.
"""


# ============================================================
# GUN 5 — KOŞUL SIRASI COK ONEMLI
# ============================================================

"""
Bu günün en kritik mantık noktası buydu.
"""

puan = 95

if puan >= 50:
    print("Geçti")
elif puan >= 90:
    print("Mükemmel")
else:
    print("Kaldı")

"""
Bu kod çalışır.
Ama mantık hatası olabilir.

95 için ilk koşul zaten True.
Bu yüzden "Geçti" yazılır.
Alttaki özel durum hiç görülmez.

Demek ki:
daha özel koşullar çoğu zaman önce gelmelidir.
"""

puan = 95

if puan >= 90:
    print("Mükemmel")
elif puan >= 50:
    print("Geçti")
else:
    print("Kaldı")


# ============================================================
# GUN 5 — NESTED if GIRISI
# ============================================================

"""
Nested if = if içinde if
"""

x = 3

if x > 2:
    if x < 5:
        print("A")
    else:
        print("B")
else:
    print("C")

"""
Buradaki mantık:
önce dış koşul,
sonra iç koşul.

x = 3 için:
- x > 2 -> True
- içeri gir
- x < 5 -> True
- çıktı -> A
"""

"""
Bu örnek sana şunu öğretti:
Her else her if'e bağlı değildir.
Aynı girinti seviyesindeki else, o if'e bağlıdır.
"""


# ============================================================
# GUN 5 — BAĞIMSIZ if ILE elif ZINCIRI FARKI
# ============================================================

"""
Bağımsız if:
birden fazla blok çalışabilir.

if / elif / else:
alternatif sınıflandırmadır, genelde tek yol seçilir.
"""

puan = 95

if puan >= 50:
    print("Geçti")

if puan >= 90:
    print("Onur listesi")

"""
Burada ikisi de çalışabilir.
"""

puan = 95

if puan >= 90:
    print("Onur listesi")
elif puan >= 50:
    print("Geçti")

"""
Burada sadece ilk uygun blok çalışır.
"""


# ============================================================
# GUN 5 — ANA CUMLELER
# ============================================================

"""
- if / elif / else = karar zinciri
- İlk doğru blok çalışır
- Koşul sırası sonucu değiştirir
- Nested if, ek katmanlı karar yapısıdır
- Else'in hangi if'e bağlı olduğu girintiden anlaşılır
- Her if zinciri aynı mantıkta okunmaz
"""


# ============================================================
# GUN 6 — KARAR AĞACI EGZERSIZLERI + KOŞUL AKIŞI
# ============================================================

"""
Gün 6'nın ana fikri:
Dünkü if bilgisini "kod ezberi" seviyesinden çıkarıp
"akış okuma" seviyesine taşımaktı.

Karar ağacı dediğimiz şey:
programın bir koşula göre farklı yollara ayrılmasıdır.
"""

yas = 20

if yas >= 18:
    print("Girebilir")
else:
    print("Giremez")

"""
Bunu ağaç gibi düşün:

yas >= 18 ?
├── Evet  -> Girebilir
└── Hayır -> Giremez
"""


# ============================================================
# GUN 6 — KARAR AĞACI NASIL OKUNUR?
# ============================================================

"""
Bir koşul sorusunda şunu yap:

1. Değişken değerlerini belirle
2. İlk koşulu değerlendir
3. True/False de
4. Hangi bloğa girdiğini gör
5. Girmediğin dalları bırak
6. Nested ise içeriyi çöz
"""

x = 3

if x > 2:
    if x < 5:
        print("A")
    else:
        print("B")
else:
    print("C")

"""
Okuma şekli:
- x > 2 ? -> True
- dış bloğa gir
- x < 5 ? -> True
- çıktı -> A
"""

"""
Karar ağacı mantığı burada çok net:

x > 2 ?
├── Hayır -> C
└── Evet
    x < 5 ?
    ├── Evet -> A
    └── Hayır -> B
"""


# ============================================================
# GUN 6 — KOŞUL AKIŞI OKUMA
# ============================================================

"""
Bu günün asıl hedefi:
kodun hangi sırayla çalıştığını görmeyi öğrenmekti.

Python tüm dalları birden çalıştırmaz.
Gerekli olan dala gider.
"""

sicaklik = 5

if sicaklik > 30:
    print("çok sıcak")
elif sicaklik > 20:
    print("ılık")
elif sicaklik > 10:
    print("serin")
else:
    print("soğuk")

"""
Çözüm:
- >30 False
- >20 False
- >10 False
- else -> soğuk
"""

"""
Buradan çıkan ana düşünce:
koşullar yukarıdan aşağıya sırayla okunur.
"""


# ============================================================
# GUN 6 — PSEUDOCODE MANTIGI
# ============================================================

"""
Bu günün gizli ama çok değerli kası:
kodu yazmadan önce akış düşünmek.

Örnek problem:
- yaş 18'den küçükse giriş yok
- değilse
    - üyelik varsa içeri al
    - üyelik yoksa kayıt istensin

Pseudocode:
eğer yaş 18'den küçükse:
    giriş yok
değilse:
    eğer üyelik varsa:
        içeri al
    değilse:
        kayıt ol
"""

yas = 20
uyelik = False

if yas < 18:
    print("Giriş yok")
else:
    if uyelik:
        print("İçeri al")
    else:
        print("Kayıt ol")

"""
Bu beceri ileride fonksiyon ve proje yazarken çok değerli olacak.
Çünkü önce akış kurarsın, sonra kodlarsın.
"""


# ============================================================
# GUN 6 — ANA CUMLELER
# ============================================================

"""
- Karar ağacı, koşullu akışın dallanma mantığıdır
- Kod okurken önce dış koşulu çöz
- Gerekli olmayan dalları takip etme
- Koşullar yukarıdan aşağıya kontrol edilir
- Girinti, mantığın parçasıdır
- Pseudocode, akışı koda dökmeden önce düşünme aracıdır
"""


# ============================================================
# GUN 1–6 BAGLANTI HARITASI
# ============================================================

"""
İlk 6 gün aslında ayrı ayrı konular değil;
birbirine bağlı bir zincirdir.

Gün 1:
isim / referans mantığı

↓
Gün 2:
obje / bellek / kimlik mantığı

↓
Gün 3:
veri tiplerinin davranışları

↓
Gün 4:
operatörler + truthy/falsy ile koşul yakıtı

↓
Gün 5:
if / elif / else ile karar verme

↓
Gün 6:
karar akışını ağaç gibi okuyabilme

Yani:
"veri nedir?" → "nasıl davranır?" → "nasıl karşılaştırılır?" → "nasıl karar verilir?"
şeklinde çok mantıklı bir akış var.
"""


# ============================================================
# ILK 6 GUNUN EN KRITIK 20 NOKTASI
# ============================================================

"""
1) Değişken kutu değil, isim/reference gibi düşünülmeli
2) "=" bağlama işlemidir
3) Aynı obje birden fazla isim tarafından referans edilebilir
4) Yeniden bağlama ile objeyi değiştirme aynı şey değildir
5) id() obje kimliğini görmeye yardım eder
6) int, float, str, bool farklı davranır
7) type() veri tipini gösterir
8) "20" ile 20 aynı şey değildir
9) None özel boş değer mantığıdır
10) Karşılaştırmalar bool üretir
11) and / or / not mantıksal akış kurar
12) Truthy / falsy koşullarda çok önemlidir
13) "" falsy iken " " truthy'dir
14) [] falsy iken [0] truthy'dir
15) % 2 == 0 çift kontrolüdür
16) if / elif / else sırayla değerlendirilir
17) İlk doğru elif bloğu çalışır
18) Koşul sırası sonucu değiştirir
19) Nested if katmanlı karar yapısıdır
20) Karar ağacı, kodun görsel mantığıdır
"""


# ============================================================
# KLASIK TUZAKLAR
# ============================================================

"""
İlk 6 günde yapılan tipik hatalar:

1) Değişkeni kutu gibi düşünüp reference mantığını kaçırmak
2) a değişince b'nin neden değişmediğini anlayamamak
3) type farkını önemsememek
4) " " ile "" farkını kaçırmak
5) [0] ile [] farkını kaçırmak
6) == ile = farkını karıştırmak
7) elif sırasını yanlış kurmak
8) nested if'te hangi else'in kime bağlı olduğunu kaçırmak
9) tüm koşulların her zaman çalıştığını sanmak
10) çalışan ama mantıksal olarak yanlış kodu doğru sanmak
"""


# ============================================================
# MINI HATIRLATMA SORULARI
# ============================================================

"""
Aşağıdaki soruları kafadan cevaplayabiliyorsan ilk 6 günün zemini iyidir:

1) a = 5, b = a, a = 10 sonrası b neden 5 kalır?
2) id() neyi görmene yardım eder?
3) "20" neden sayı değildir?
4) None neyi temsil eder?
5) " " neden truthy'dir?
6) [0] neden falsy değil?
7) % 2 == 0 neyi kontrol eder?
8) elif zincirinde neden sıra önemlidir?
9) Nested if nasıl okunur?
10) Karar ağacı ne demektir?
"""


# ============================================================
# KENDI KENDINE SOZLU ANLATIM CALIŞMASI
# ============================================================

"""
Bu rehberi okuduktan sonra şu 6 şeyi kendi sesinle anlatmayı dene:

1) Değişken ve referans mantığı
2) id() ile obje kimliği
3) temel veri tiplerinin farkı
4) truthy / falsy
5) if / elif / else sıralama mantığı
6) karar ağacı nasıl okunur?

Bir konuyu kendi cümlelerinle anlatabiliyorsan,
gerçek öğrenme orada başlar.
"""


# ============================================================
# COK KISA SUPER OZET
# ============================================================

"""
Gün 1:
Değişken = isim / referans

Gün 2:
Objeler bellekte yaşar, id() kimliği gösterir

Gün 3:
Veri tipleri davranışı belirler

Gün 4:
Operatörler karşılaştırma üretir, truthy/falsy koşulları besler

Gün 5:
if / elif / else karar zinciri kurar

Gün 6:
Karar ağacı, bu karar zincirinin akış olarak okunmasıdır
"""


# ============================================================
# SON SOZ
# ============================================================

"""
İlk 6 gün, dışarıdan basit görünür ama aslında bütün Python yolculuğunun
temel mantık katmanıdır.

Bu katman oturursa:
- döngüler daha kolay gelir
- listeler daha anlamlı görünür
- fonksiyonlar daha temiz oturur
- projelerde neden-sonuç ilişkisini daha rahat kurarsın

Bu yüzden bu rehber sadece tekrar dosyası değil,
temelini sağlamlaştıran ana omurga dosyası olarak görülmelidir.
"""

# ============================================================
# DOSYA SONU
# ============================================================
