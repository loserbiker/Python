"""
====================================
GLOBAL VE LOCAL SCOPE EĞİTİMİ
====================================

Python'da değişkenlerin geçerlilik alanı (scope) vardır.
Scope: bir değişkenin hangi kod blokları içinde erişilebilir olduğunu belirler.

1- Local Scope (Yerel Değişkenler)
2- Global Scope (Genel Değişkenler)
"""

# ------------------------------
# 1. GLOBAL SCOPE (Genel değişken)
# ------------------------------

# text değişkeni fonksiyon dışında tanımlandı -> global
text = "Hello"

def my_function():
    # Fonksiyon içinde global değişkeni kullanabiliriz
    print("Say " + text)

my_function()  # Çıktı: Say Hello

# ------------------------------
# 2. LOCAL SCOPE (Yerel değişken)
# ------------------------------

text = "Merhaba"

def benim_fonksiyonum():
    # text burada sadece fonksiyon içinde geçerli -> local
    text = "sa"
    print("as " + text)

benim_fonksiyonum()  # Çıktı: as sa

# Fonksiyon dışındaki global değişken etkilenmez
print(text)           # Çıktı: Merhaba

# Özet:
# - Local değişken fonksiyon içinde geçerlidir
# - Fonksiyon dışında global değişken etkilenmez

# ------------------------------
# 3. GLOBAL ANAHTAR KELİMESİ
# ------------------------------

def yeni_fonksiyon():
    global a  # Bu değişkeni global olarak tanımlıyoruz
    a = "Selam"

yeni_fonksiyon()      # Fonksiyonda global değişken oluşturuldu
print("Merhaba " + a) # Çıktı: Merhaba Selam

# NOT:
# Global değişkenler büyük projelerde dikkatli kullanılmalıdır,
# çünkü çok fazla global değişken kodun okunabilirliğini ve güvenliğini azaltır.
