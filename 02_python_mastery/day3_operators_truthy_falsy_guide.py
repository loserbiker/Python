"""
day3_operators_truthy_falsy_guide.py
DAY 3 — OPERATÖRLER + TRUTHY/FALSY (DERİN REHBER)

Amaç:
- Aritmetik, karşılaştırma, mantıksal operatörleri gerçek kullanımda öğrenmek
- Operatör önceliğini (precedence) ve parantez kullanımını oturtmak
- == vs is, in operatörü, short-circuit mantığı
- Truthy/Falsy ile if yazma refleksi

Bu gün bittiğinde:
- Koşul yazarken saçma bug üretme ihtimalin ciddi düşer.
"""

# ============================================================
# 1) Aritmetik Operatörler
# ============================================================
print("\n--- 1) Aritmetik ---")

a = 10
b = 3

print("a+b =", a + b)
print("a-b =", a - b)
print("a*b =", a * b)
print("a/b =", a / b)     # float
print("a//b =", a // b)   # floor division
print("a%b =", a % b)     # modulo
print("a**b =", a ** b)   # üs

# ============================================================
# 2) Karşılaştırma Operatörleri
# ============================================================
print("\n--- 2) Karşılaştırma ---")

x = 10
print("x == 10:", x == 10)
print("x != 5 :", x != 5)
print("x >  7 :", x > 7)
print("x >= 10:", x >= 10)

# Comparison chaining
print("\nComparison chaining:")
print("10 < x < 20:", 10 < x < 20)

# ============================================================
# 3) Operatör Önceliği (Precedence) ve Parantez
# ============================================================
print("\n--- 3) Precedence ---")

"""
Sık hata:
a > 10 and b < 5 or c == 3

Burada parantez yoksa okunabilirlik düşer.
Kural: koşullar büyüdükçe parantez koy.
"""

a = 11
b = 100
c = 3

expr1 = a > 10 and b < 5 or c == 3
expr2 = (a > 10 and b < 5) or (c == 3)

print("expr1:", expr1)
print("expr2:", expr2)

# ============================================================
# 4) Mantıksal Operatörler: and / or / not
# ============================================================
print("\n--- 4) and/or/not ---")

age = 20
has_license = True
is_drunk = False

print("age>=18 and has_license:", age >= 18 and has_license)
print("has_license or is_drunk :", has_license or is_drunk)
print("not is_drunk            :", not is_drunk)

# ============================================================
# 5) Short-circuit mantığı (kısa devre)
# ============================================================
print("\n--- 5) Short-circuit ---")

def check():
    print("check() çalıştı!")
    return True

print("False and check():")
result = False and check()
print("result:", result)

print("\nTrue or check():")
result = True or check()
print("result:", result)

"""
Neden önemli?
- Hata önlersin
- Gereksiz hesaplamayı engellersin

Örnek: None kontrolü
"""

user = None
if user and "name" in user:
    print(user["name"])
else:
    print("user yok veya name yok (güvenli)")

# ============================================================
# 6) Üyelik operatörü: in / not in
# ============================================================
print("\n--- 6) in / not in ---")

text = "python"
print("py" in text)
print("java" not in text)

lst = [1, 2, 3]
print(2 in lst)

# Set ile “var mı?” kontrolü çok hızlıdır
s = {1, 2, 3}
print(2 in s)

# ============================================================
# 7) Eşitlik vs Kimlik: == ve is
# ============================================================
print("\n--- 7) == vs is ---")

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)   # içerik aynı mı?
print("a is b:", a is b)   # aynı obje mi?

x = None
print("x is None:", x is None)

"""
Genel pratik:
- Değer karşılaştırması: ==
- None kontrolü: is None
"""

# ============================================================
# 8) Truthy / Falsy
# ============================================================
print("\n--- 8) Truthy/Falsy ---")

values = [0, 1, "", "x", [], [0], {}, {"a": 1}, None, False, True]

for v in values:
    if v:
        print(f"{v!r:>10} -> truthy")
    else:
        print(f"{v!r:>10} -> falsy")

"""
Falsy (en bilinenler):
0, 0.0, "", [], {}, set(), None, False

Bu şu demek:
if my_list:  -> liste boş değilse
if not my_list: -> liste boşsa
"""

# ============================================================
# 9) Mantıksal operatörlerin “değer döndürmesi”
# ============================================================
print("\n--- 9) and/or değer döndürür ---")

"""
Python'da and/or sadece True/False döndürmek zorunda değil.
İfadelerden birini döndürür.

- A and B: A falsy ise A döner, yoksa B döner
- A or  B: A truthy ise A döner, yoksa B döner
"""

print("" or "varsayilan")          # "varsayilan"
print("deger" or "varsayilan")     # "deger"
print(0 and 999)                   # 0
print(1 and 999)                   # 999

# Bu pattern bazen “varsayılan değer” için kullanılır ama
# None ile daha güvenli yazmak istersen:
value = ""
defaulted = value if value != "" else "varsayilan"
print("defaulted:", defaulted)

# ============================================================
# 10) Egzersizler
# ============================================================
print("\n--- 10) Egzersizler ---")

# Egz1: Bir sayı al, 10 ile 20 arasında mı?
n = 15
print("Egz1:", 10 < n < 20)

# Egz2: Kullanıcı login kontrolü (basit)
username = "can"
password = "1234"
input_user = "can"
input_pass = "1234"

is_ok = (input_user == username) and (input_pass == password)
print("Egz2 login:", "OK" if is_ok else "FAIL")

# Egz3: Liste boş mu dolu mu? (truthy/falsy)
lst = []
print("Egz3:", "bos" if not lst else "dolu")

"""
DAY 3 CHECKLIST ✅
- aritmetik + floor + modulo
- comparison chaining
- precedence + parantez refleksi
- and/or/not + short-circuit
- == vs is + in
- truthy/falsy
"""