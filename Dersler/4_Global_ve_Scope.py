"""
GLOBAL VE LOCAL SCOPE
"""

text = "Hello"

def my_function():
    print("Say " + text)

my_function()

# ------------------------------
# Local Variable
# ------------------------------

text = "Merhaba"

def benim_fonksiyonum():
    text = "sa"
    print("as " + text)

benim_fonksiyonum()
print(text)

# ------------------------------
# Global Anahtar Kelimesi
# ------------------------------

def yeni_fonksiyon():
    global a
    a = "Selam"

yeni_fonksiyon()
print("Merhaba " + a)

# Not:
# Global değişkenler büyük projelerde dikkatli kullanılmalıdır.
