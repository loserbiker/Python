content = r'''# ============================================================
# PYTHON KAMP
# Gün 6 — Karar Ağacı Egzersizleri + Koşul Akışı Okuma
# Dosya adı önerisi: day6_decision_tree_exercises_guide.py
# ============================================================

"""
Bu dosya, Python'da karar ağacı mantığını ve koşullu akış okumayı
çok net oturtmak için hazırlanmış detaylı bir rehberdir.

Bu günün amacı yeni bir sözdizimi öğrenmek değil;
zaten öğrendiğin if / elif / else yapılarının nasıl düşündüğünü
gerçekten anlamaktır.

Yani bu dosyanın ana hedefleri:

1) Kodun hangi sırayla çalıştığını anlamak
2) Hangi else'in hangi if'e bağlı olduğunu görmek
3) Koşulların sırasının neden önemli olduğunu kavramak
4) Nested if mantığını dallanma olarak okumak
5) Kod görmeden önce akış kurabilmek
6) Karar ağacı şeklinde algoritma düşünebilmek

Bu konu neden önemli?

Çünkü ileride:
- kullanıcı giriş kontrolü
- menülü CLI sistemleri
- oyun akışı
- skor / yetki / doğrulama kontrolleri
- veri filtreleme
- fonksiyon içi karar yapıları

gibi her yerde aynı mantık kullanılacak.

Kısacası:
Karar ağacı = programın "hangi durumda hangi yolu seçtiği" mantıktır.
"""


# ============================================================
# 1) KARAR AĞACI NEDIR?
# ============================================================

"""
Karar ağacı, programın bir koşulu kontrol edip sonuca göre farklı
yollara gitmesi demektir.

En basit haliyle:

- bir soru sorulur
- cevap True ise bir yol seçilir
- cevap False ise başka bir yol seçilir

Bu yapı birden fazla koşulla genişlediğinde dallanır.
İşte buna karar ağacı gibi bakarız.
"""

yas = 20

if yas >= 18:
    print("Girebilir")
else:
    print("Giremez")

# Bu kodun karar ağacı mantığı:
#
# yas >= 18 ?
# ├── Evet  -> Girebilir
# └── Hayır -> Giremez


# ============================================================
# 2) if / else = TEK KARAR NOKTASI
# ============================================================

"""
if / else yapısı bir yol ayrımıdır.

Python burada tek bir soru sorar:
"Bu koşul doğru mu?"

Doğruysa if bloğu,
yanlışsa else bloğu çalışır.
"""

sayi = 7

if sayi > 5:
    print("5'ten büyük")
else:
    print("5'ten büyük değil")

# Akış:
# sayi > 5 ?
# ├── True  -> "5'ten büyük"
# └── False -> "5'ten büyük değil"


# ============================================================
# 3) elif = IKINCI / UCUNCU KARAR KAPISI
# ============================================================

"""
elif, ilk koşul sağlanmadığında yeni bir koşul denememizi sağlar.

Burada önemli nokta:
Python koşulları yukarıdan aşağıya sırayla kontrol eder.
İlk doğru olan blok çalışır.
Sonrakilere artık bakılmaz.
"""

notu = 72

if notu >= 85:
    print("Pekiyi")
elif notu >= 70:
    print("İyi")
else:
    print("Geliştirilmeli")

# Akış:
#
# notu >= 85 ?
# ├── Evet  -> "Pekiyi"
# └── Hayır
#     notu >= 70 ?
#     ├── Evet  -> "İyi"
#     └── Hayır -> "Geliştirilmeli"


# ============================================================
# 4) EN KRITIK MANTIK: KOŞULLARIN SIRASI ONEMLIDIR
# ============================================================

"""
Koşullar yukarıdan aşağıya sırayla çalıştığı için,
daha genel koşulu üste koyarsan daha özel koşul hiç çalışmayabilir.
"""

puan = 95

if puan >= 50:
    print("Geçti")
elif puan >= 90:
    print("Mükemmel")
else:
    print("Kaldı")

# Burada çıktı "Geçti" olur.
# Neden?
# Çünkü Python önce puan >= 50 kontrolünü yapar.
# 95 için bu True'dur.
# İlk doğru blok çalışınca işlem biter.

"""
Bu yüzden yukarıdaki yapı mantıksal olarak kusurludur.

Doğru sıralama genelde daha özel / daha yüksek şarttan
daha genel şarta doğrudur.
"""

puan = 95

if puan >= 90:
    print("Mükemmel")
elif puan >= 50:
    print("Geçti")
else:
    print("Kaldı")

# Şimdi çıktı "Mükemmel" olur.


# ============================================================
# 5) KARAR AĞACINI METIN OLARAK OKUMA ALIŞKANLIĞI
# ============================================================

"""
Bir if bloğu gördüğünde doğrudan koda bakıp ezberleme.
Şunu sor:

1. İlk soru ne?
2. True ise ne oluyor?
3. False ise nereye gidiyor?
4. Sonraki soru ne?
5. Bu akış nerede bitiyor?

Bu alışkanlık seni ezberden çıkarır ve mantığa taşır.
"""

hava = "yağmurlu"

if hava == "güneşli":
    print("Dışarı çık")
elif hava == "yağmurlu":
    print("Şemsiye al")
else:
    print("Evde kal")

# Metin olarak okuma:
#
# İlk soru:
# hava == "güneşli" ?
# Hayır.
#
# İkinci soru:
# hava == "yağmurlu" ?
# Evet.
#
# Sonuç:
# "Şemsiye al"


# ============================================================
# 6) HANGI else HANGI if'E BAGLI?
# ============================================================

"""
Bu konu özellikle yeni başlayanlarda çok karışır.
Cevap:
else, aynı hizadaki (aynı indentation seviyesindeki) if'e bağlıdır.

Yani girinti seviyesi burada belirleyicidir.
"""

x = 3

if x > 2:
    if x < 5:
        print("A")
    else:
        print("B")
else:
    print("C")

# Burada:
# içteki else -> if x < 5'e bağlı
# en alttaki else -> if x > 2'ye bağlı

"""
Karar ağacı şeklinde:
x > 2 ?
├── Hayır -> C
└── Evet
    x < 5 ?
    ├── Evet -> A
    └── Hayır -> B
"""

# x = 3 için:
# x > 2 ? -> True
# x < 5 ? -> True
# çıktı -> A


# ============================================================
# 7) NESTED IF NEDIR?
# ============================================================

"""
Nested if = if bloğunun içinde başka bir if olmasıdır.

Bu yapı, bir koşul sağlandıktan sonra yeni bir alt kontrol yapılmasını sağlar.
"""

yas = 22
ehliyet = True

if yas >= 18:
    if ehliyet:
        print("Araç kullanabilir")
    else:
        print("Yaşı uygun ama ehliyeti yok")
else:
    print("Yaşı yetmiyor")

# Karar ağacı:
#
# yas >= 18 ?
# ├── Hayır -> "Yaşı yetmiyor"
# └── Evet
#     ehliyet var mı?
#     ├── Evet -> "Araç kullanabilir"
#     └── Hayır -> "Yaşı uygun ama ehliyeti yok"


# ============================================================
# 8) NESTED IF ILE elif AYNI SEY MIDIR?
# ============================================================

"""
Hayır, aynı şey değildir.

elif:
- alternatif yol sunar

nested if:
- bir yolun İÇİNDE ek kontrol yapar

Özet:
elif = "başka seçenek"
nested if = "önce bunu geç, sonra içeride bunu da kontrol et"
"""

# elif örneği:
notu = 80

if notu >= 90:
    print("A")
elif notu >= 70:
    print("B")
else:
    print("C")

# nested if örneği:
giris_yapildi = True
admin = False

if giris_yapildi:
    if admin:
        print("Admin paneli")
    else:
        print("Normal kullanıcı paneli")
else:
    print("Önce giriş yap")


# ============================================================
# 9) KOD AKIŞI SATIR SATIR NASIL DUSUNULUR?
# ============================================================

"""
Python kodu yukarıdan aşağıya çalıştırır.
if bloğunda ise sadece koşulu doğru olan dala girer.

Yani akış:
- satır satır ilerler
- koşul görür
- karar verir
- uygun bloğa girer
- diğer dalı atlar
"""

sayi = 10

if sayi % 2 == 0:
    print("çift")
    print("bu blok çalıştı")
else:
    print("tek")
    print("bu blok çalışmadı")

print("devam")

# Burada:
# sayi % 2 == 0 -> True
# if bloğundaki iki print çalışır
# else bloğu atlanır
# sonra program devam eder


# ============================================================
# 10) KOŞUL ICINDE KOŞUL OKUMA TEKNIGI
# ============================================================

"""
Nested yapılarda panik yapma.
Katman katman çöz:

1) dış koşulu çöz
2) o dala girdiysen içeriyi çöz
3) o dal çalışmıyorsa içi zaten önemli değildir

Bu çok önemli bir tekniktir.
"""

puan = 88
devam_durumu = True

if puan >= 70:
    if devam_durumu:
        print("Dersi geçti")
    else:
        print("Not yeterli ama devamsız")
else:
    print("Not yetersiz")

# Çözüm sırası:
#
# 1. puan >= 70 ? -> True
# 2. iç bloğa girdik
# 3. devam_durumu ? -> True
# 4. çıktı -> "Dersi geçti"


# ============================================================
# 11) KOŞULLARIN KAPSAMI: HER ŞEY HER ZAMAN KONTROL EDILMEZ
# ============================================================

"""
Bazı öğrenciler tüm koşulların her zaman sırayla kontrol edildiğini sanır.
Bu yanlış.

Python sadece ihtiyaç duyduğu kadar kontrol eder.
İlk doğru elif bulunduysa geri kalan elif'lere bakmaz.
Nested if'te dış koşul false ise iç koşula hiç girmez.
"""

sayi = 5

if sayi > 10:
    if sayi < 20:
        print("arada")
else:
    print("ilk koşul false olduğu için içe hiç girilmedi")

# sayi > 10 -> False
# içteki if'e hiç bakılmaz


# ============================================================
# 12) MANTIK HATASI VS SOZDIZIM HATASI
# ============================================================

"""
Bir kod çalışıyor olabilir ama mantığı yanlış olabilir.

Bu ayrımı bilmek çok önemli:

Syntax Error:
- Python kodu okuyamaz

Logic Error:
- Python kodu çalıştırır ama sonuç istediğin gibi değildir
"""

# Logic error örneği:
puan = 95

if puan >= 50:
    print("Geçti")
elif puan >= 90:
    print("Mükemmel")

# Bu kod hata vermez.
# Ama mantıksal olarak bozuk olabilir.
# Çünkü 95 için "Mükemmel" bekliyorsan sıralama yanlış.


# ============================================================
# 13) KARAR AĞACI CIZER GIBI DUSUNME
# ============================================================

"""
Kod yazmadan önce karar ağacı düşünebilirsin.

Örnek problem:
- Kullanıcı 18 yaşından küçükse giriş yok
- 18 ve üstüyse
    - üyelik varsa içeri al
    - üyelik yoksa kayıt olmalı
"""

# Metin tabanlı karar ağacı:
#
# yaş >= 18 ?
# ├── Hayır -> Giriş yok
# └── Evet
#     üyelik var mı?
#     ├── Evet -> İçeri al
#     └── Hayır -> Önce kayıt ol


# ============================================================
# 14) AYNI PROBLEMI KODA DOKME
# ============================================================

yas = 20
uyelik = False

if yas >= 18:
    if uyelik:
        print("İçeri al")
    else:
        print("Önce kayıt ol")
else:
    print("Giriş yok")


# ============================================================
# 15) AKIŞ OKUMA EGZERSIZI 1
# ============================================================

"""
Aşağıdaki kodu zihninde çalıştır:
"""

x = 8

if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")

# Çözüm:
# x > 10 ? -> False
# x > 5 ? -> True
# çıktı -> B


# ============================================================
# 16) AKIŞ OKUMA EGZERSIZI 2
# ============================================================

y = 12

if y % 2 == 0:
    if y > 10:
        print("çift ve büyük")
    else:
        print("çift ama küçük")
else:
    print("tek")

# Çözüm:
# y % 2 == 0 ? -> True
# içeri gir
# y > 10 ? -> True
# çıktı -> "çift ve büyük"


# ============================================================
# 17) AKIŞ OKUMA EGZERSIZI 3
# ============================================================

sifre = "python123"
girilen = "python"

if girilen == sifre:
    print("Giriş başarılı")
else:
    print("Giriş başarısız")

# girilen == sifre ? -> False
# çıktı -> "Giriş başarısız"


# ============================================================
# 18) AKIŞ OKUMA EGZERSIZI 4
# ============================================================

sicaklik = 5

if sicaklik > 30:
    print("çok sıcak")
elif sicaklik > 20:
    print("ılık")
elif sicaklik > 10:
    print("serin")
else:
    print("soğuk")

# 5 için:
# >30 False
# >20 False
# >10 False
# else -> "soğuk"


# ============================================================
# 19) AKIŞ OKUMA EGZERSIZI 5
# ============================================================

puan = 60
bonus = True

if puan >= 70:
    print("geçti")
else:
    if bonus:
        print("bonus ile değerlendir")
    else:
        print("kaldı")

# Çözüm:
# puan >= 70 ? -> False
# else bloğuna gir
# bonus ? -> True
# çıktı -> "bonus ile değerlendir"


# ============================================================
# 20) PSEUDOCODE NEDIR VE NEDEN FAYDALIDIR?
# ============================================================

"""
Pseudocode = gerçek kod değil, mantığın düz metin veya yarı-kod hali.

Amaç:
- problem çözümünü koda dökmeden önce düşünmek
- akışı netleştirmek
- kodu aceleye getirmemek

Karar ağacı konularında pseudocode çok faydalıdır.
"""

# Örnek pseudocode:
#
# eğer yaş 18'den küçükse:
#     "giremez" yaz
# değilse:
#     eğer bileti varsa:
#         "girebilir" yaz
#     değilse:
#         "bilet almalı" yaz


# ============================================================
# 21) PSEUDOCODE'DAN KODA GECIS
# ============================================================

yas = 19
bilet = True

if yas < 18:
    print("Giremez")
else:
    if bilet:
        print("Girebilir")
    else:
        print("Bilet almalı")


# ============================================================
# 22) KARAR AĞACI PROBLEM KURMA EGZERSIZI
# ============================================================

"""
Problem:
Bir sistemde kullanıcıdan yaş ve öğrenci olup olmadığı bilgisi var.

Kurallar:
- 12 yaş altı -> ücretsiz
- 12 ve üstü:
    - öğrenci ise indirimli
    - öğrenci değilse tam bilet
"""

yas = 16
ogrenci = True

if yas < 12:
    print("Ücretsiz")
else:
    if ogrenci:
        print("İndirimli")
    else:
        print("Tam bilet")


# ============================================================
# 23) AYNI PROBLEMI elif ILE DUSUNME
# ============================================================

"""
Her nested yapı elif'e çevrilmez.
Ama bazı durumlarda alternatif sınıflar varsa elif daha temiz olabilir.
"""

notu = 45

if notu >= 85:
    print("Pekiyi")
elif notu >= 70:
    print("İyi")
elif notu >= 50:
    print("Geçti")
else:
    print("Kaldı")

# Bu kullanım, birbirini dışlayan sınıflar için uygundur.


# ============================================================
# 24) KOSUL SIRASI YANLIŞSA NE OLUR? DERIN ORNEK
# ============================================================

yas = 70

if yas >= 18:
    print("Yetişkin")
elif yas >= 65:
    print("Emekli yaş kategorisi")
else:
    print("Çocuk/genç")

# Burada 70 için "Yetişkin" yazdırır.
# Çünkü ilk koşul zaten True.
# Bu mantık bozuk olabilir eğer özel kategoriyi görmek istiyorsan.

yas = 70

if yas >= 65:
    print("Emekli yaş kategorisi")
elif yas >= 18:
    print("Yetişkin")
else:
    print("Çocuk/genç")

# Şimdi daha anlamlı.


# ============================================================
# 25) "ONCE GENEL MI, ONCE OZEL MI?" KURALI
# ============================================================

"""
Sınıflandırma yapıyorsan genelde:
önce daha özel / daha dar koşul,
sonra daha genel koşul yazılır.

Örnek:
90 üstü özel bir durumsa önce onu yakala.
50 üstü daha genel ise sonra yaz.
"""

puan = 91

if puan >= 90:
    print("A seviye")
elif puan >= 80:
    print("B seviye")
elif puan >= 50:
    print("Geçti")
else:
    print("Kaldı")


# ============================================================
# 26) BOOLEAN DEGERLERLE KARAR AKIŞI
# ============================================================

"""
Bazen koşullar sayı karşılaştırması olmaz.
Doğrudan True / False değerleriyle karar verirsin.
"""

giris_yapildi = True
premium = False

if giris_yapildi:
    if premium:
        print("Premium içerik")
    else:
        print("Standart içerik")
else:
    print("Önce giriş yap")


# ============================================================
# 27) BIRDEN FAZLA KOŞULU AYNI SATIRDA KULLANMA
# ============================================================

"""
and ve or ile daha karmaşık kararlar kurulabilir.
Ama önce temel akışı oturtmak daha önemlidir.
Yine de küçük bir örnek görmek faydalı olabilir.
"""

yas = 20
ehliyet = True

if yas >= 18 and ehliyet:
    print("Araba kullanabilir")
else:
    print("Kullanamaz")

# Burada iki şart aynı anda sağlanmalı.


# ============================================================
# 28) KARAR AĞACI + KULLANICI DENEYIMI MANTIGI
# ============================================================

"""
Karar ağacı sadece teknik konu değil;
kullanıcıya hangi durumda hangi mesajı verdiğini düzenler.

Bu yüzden iyi bir karar yapısı:
- net olur
- boşluk bırakmaz
- mantık hatası içermez
- her durumu kapsar
"""

kullanici_adi = "can"
sifre = "1234"

girilen_ad = "can"
girilen_sifre = "1234"

if girilen_ad == kullanici_adi:
    if girilen_sifre == sifre:
        print("Giriş başarılı")
    else:
        print("Şifre yanlış")
else:
    print("Kullanıcı adı yanlış")


# ============================================================
# 29) SIK YAPILAN HATALAR
# ============================================================

"""
1) else'in hangi if'e bağlı olduğunu kaçırmak
2) girintiyi yanlış okumak
3) koşul sırasını yanlış kurmak
4) tüm koşulların her zaman kontrol edildiğini sanmak
5) elif yerine nested if gerektiğini fark etmemek
6) mantık hatasını syntax error sanmak
7) sonucu tahmin etmeden kodu yazmak
"""

# Hatalı düşünme örneği:
puan = 100

if puan >= 50:
    print("Geçti")
elif puan >= 90:
    print("Mükemmel")

# Çalışır ama beklentiye göre yanlış olabilir.


# ============================================================
# 30) MINI COZUM STRATEJISI
# ============================================================

"""
Bir karar ağacı sorusunda şu adımları izle:

1. Değişkenlerin değerlerini yaz
2. İlk if koşulunu değerlendir
3. True/False de
4. Girilen bloğu takip et
5. Diğer gereksiz dalları at
6. Çıktıyı belirle

Nested ise:
- önce dış katman
- sonra iç katman
"""

# Örnek:
a = 4

if a > 0:
    if a % 2 == 0:
        print("pozitif çift")
    else:
        print("pozitif tek")
else:
    print("pozitif değil")

# Çözüm:
# a > 0 ? -> True
# içeri gir
# a % 2 == 0 ? -> True
# çıktı -> "pozitif çift"


# ============================================================
# 31) EGZERSIZ SETI 1 — CIKTIYI TAHMIN ET
# ============================================================

"""
Soru 1:
x = 1

if x > 5:
    print("A")
else:
    print("B")

Beklenen çıktı: B
"""

"""
Soru 2:
x = 10

if x >= 10:
    print("A")
elif x >= 5:
    print("B")
else:
    print("C")

Beklenen çıktı: A
"""

"""
Soru 3:
x = 7

if x % 2 == 0:
    print("çift")
else:
    print("tek")

Beklenen çıktı: tek
"""

"""
Soru 4:
yas = 17
izin = True

if yas >= 18:
    if izin:
        print("Girebilir")
    else:
        print("İzin yok")
else:
    print("Yaş yetmiyor")

Beklenen çıktı: Yaş yetmiyor
"""


# ============================================================
# 32) EGZERSIZ SETI 2 — HANGI DALA GIRER?
# ============================================================

"""
Soru:
puan = 82

if puan >= 90:
    print("A")
elif puan >= 80:
    print("B")
elif puan >= 70:
    print("C")
else:
    print("D")

Cevap:
ikinci dala girer -> B
"""

"""
Soru:
hava = "bulutlu"

if hava == "güneşli":
    print("Dışarı çık")
elif hava == "yağmurlu":
    print("Şemsiye al")
else:
    print("Duruma göre hareket et")

Cevap:
else dalına girer
"""


# ============================================================
# 33) EGZERSIZ SETI 3 — PSEUDOCODE YAZ
# ============================================================

"""
Problem:
- sayı negatifse "negatif"
- sayı 0 ise "sıfır"
- pozitifse "pozitif"

Pseudocode:
eğer sayı < 0 ise:
    negatif yaz
değilse eğer sayı == 0 ise:
    sıfır yaz
değilse:
    pozitif yaz
"""

sayi = -3

if sayi < 0:
    print("negatif")
elif sayi == 0:
    print("sıfır")
else:
    print("pozitif")


# ============================================================
# 34) EGZERSIZ SETI 4 — KODU OKU, AGACI CIZ
# ============================================================

"""
Kod:
uyelik = True
bakiye = 50

if uyelik:
    if bakiye >= 100:
        print("Satın alabilir")
    else:
        print("Bakiye yetersiz")
else:
    print("Üyelik gerekli")

Karar ağacı:
uyelik var mı?
├── Hayır -> Üyelik gerekli
└── Evet
    bakiye >= 100 ?
    ├── Evet -> Satın alabilir
    └── Hayır -> Bakiye yetersiz
"""


# ============================================================
# 35) GERCEK HAYAT SENARYOLARI
# ============================================================

"""
Karar ağacının kullanıldığı gerçek örnekler:

1) Giriş sistemi
   - kullanıcı adı doğru mu?
   - şifre doğru mu?

2) Yaş kontrolü
   - 18 üstü mü?
   - belge var mı?

3) Oyun sistemi
   - oyuncu canlı mı?
   - mermisi var mı?
   - saldırı izni var mı?

4) E-ticaret
   - stok var mı?
   - bakiye yeterli mi?
   - üyelik aktif mi?

5) CLI uygulama
   - menü seçimi doğru mu?
   - veri boş mu?
   - tekrar isteniyor mu?
"""


# ============================================================
# 36) BIR TIK DAHA ZOR ORNEK
# ============================================================

yas = 22
giris_karti = True
yasakli = False

if yas >= 18:
    if giris_karti:
        if yasakli:
            print("Giremez")
        else:
            print("Girebilir")
    else:
        print("Kart gerekli")
else:
    print("Yaş yetmiyor")

# Çözüm:
# yaş >= 18 -> True
# kart var mı -> True
# yasaklı mı -> False
# çıktı -> Girebilir

"""
Karar ağacı çok dallı olduğunda yine aynı teknik:
en dıştan başla, doğru dala gir, içeriyi çöz.
"""


# ============================================================
# 37) COK ONEMLI AYRIM: BAGIMSIZ if vs elif ZINCIRI
# ============================================================

"""
Bazı durumlarda if-if-if kullanırsın,
bazı durumlarda if-elif-else kullanırsın.

if-elif-else:
- alternatif sınıflar için
- sadece bir tanesi çalışsın diye

bağımsız if'ler:
- birden fazla koşul aynı anda çalışabilsin diye
"""

puan = 95

if puan >= 50:
    print("Geçti")

if puan >= 90:
    print("Onur listesi")

# Burada ikisi de çalışabilir.

puan = 95

if puan >= 90:
    print("Onur listesi")
elif puan >= 50:
    print("Geçti")

# Burada sadece ilk uygun blok çalışır.


# ============================================================
# 38) SIKISIK YAPILARDA GIRINTI OKUMA
# ============================================================

"""
Girinti = blok sınırı

Şunu unutma:
Python'da girinti görsel süs değil, mantığın kendisidir.
Kim kimin içinde, girintiden anlaşılır.
"""

deger = 4

if deger > 0:
    print("pozitif")
    if deger % 2 == 0:
        print("çift")
    else:
        print("tek")
print("bitti")

# "bitti" satırı en dışarıda olduğu için her durumda çalışır.


# ============================================================
# 39) BUGUNUN ANA ZIHIN KAZANIMI
# ============================================================

"""
Bugünün asıl kazanımı şudur:

Kod gördüğünde artık sadece satırları değil,
akışı ve dalları göreceksin.

Yani:
- soru ne?
- hangi yol seçildi?
- diğer yol neden çalışmadı?
- hangi koşul önce kontrol edildi?
- hangi else kime bağlı?

Bunları çözebiliyorsan karar ağacı mantığı oturuyor demektir.
"""


# ============================================================
# 40) OZET
# ============================================================

"""
Bugün öğrenilen temel noktalar:

- Karar ağacı, koşullu akışın dallanma mantığıdır.
- if / else tek karar noktasıdır.
- elif alternatif dallar kurar.
- Koşullar yukarıdan aşağıya sırayla kontrol edilir.
- İlk doğru koşuldan sonra elif zincirinde devam edilmez.
- nested if, bir koşulun içinde ek kontrol yapmaktır.
- else aynı hizadaki if'e bağlıdır.
- Girinti, Python'da mantığın parçasıdır.
- Koşul sırası yanlışsa kod çalışsa bile mantık bozulabilir.
- Pseudocode ve metin tabanlı ağaç çizimi, kodu daha iyi anlamayı sağlar.
"""


# ============================================================
# 41) KENDI KENDINE PRATIK ICIN GOREVLER
# ============================================================

"""
Aşağıdaki mini görevleri kendin çözmeyi dene:

1) Bir not sistemi yaz:
   - 85 ve üstü -> Pekiyi
   - 70 ve üstü -> İyi
   - 50 ve üstü -> Geçti
   - altı -> Kaldı

2) Bir yaş sistemi yaz:
   - 0-12 -> çocuk
   - 13-17 -> genç
   - 18+ -> yetişkin

3) Kullanıcı giriş kontrolü yaz:
   - kullanıcı adı doğru mu?
   - şifre doğru mu?

4) Nested karar sistemi yaz:
   - yaş uygunsa
   - belge varsa
   - girişe izin ver

5) Bir sayının:
   - negatif / sıfır / pozitif olduğunu bulan yapı yaz
"""

# ============================================================
# DOSYA SONU
# ============================================================
'''
path = "/mnt/data/day6_decision_tree_exercises_guide.py"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Saved to {path}")