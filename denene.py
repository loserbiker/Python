# # # # # # # # def kontrol(sayi):
# # # # # # # #     if sayi > 0:
# # # # # # # #         print("Pozitif")
# # # # # # # #     elif sayi < 0:
# # # # # # # #         print("Negatif")
# # # # # # # #     else:
# # # # # # # #         print("Sıfır")
# # # # # # # # print(kontrol(5))
# # # # # # # # print(kontrol(-2))
# # # # # # # # print(kontrol(0))

# # # # # # # def cift_mi(sayi):
# # # # # # #     if sayi % 2 == 0:
# # # # # # #         return "Çift"
# # # # # # #     else:
# # # # # # #         return "Tek"

# # # # # # # print(cift_mi(4))
# # # # # # # print(cift_mi(7))

# # # # # # def buyuk_mu(sayi):
# # # # # #     if sayi > 10:
# # # # # #         return "Büyük"
# # # # # #     else:
# # # # # #         return "Küçük veya eşit"

# # # # # # print(buyuk_mu(15))
# # # # # # print(buyuk_mu(10))

# # # # # def not_durumu(notu):
# # # # #     if notu >= 85:
# # # # #         return "Pekiyi"
# # # # #     elif notu >= 50:
# # # # #         return "Geçti"
# # # # #     else:
# # # # #         return "Kaldı"

# # # # # print(not_durumu(90))
# # # # # print(not_durumu(70))
# # # # # print(not_durumu(30))

# # # # # def puan_durumu(puan):
# # # # #     if puan >= 85:
# # # # #         return "Çok iyi"
# # # # #     elif puan >= 50:
# # # # #         return "Geçti"
# # # # #     else:
# # # # #         return "Kaldı"
# # # # # print(puan_durumu(90))
# # # # # print(puan_durumu(60))
# # # # # print(puan_durumu(20))

# # # # # def cift_tek(sayi):
# # # # #     if sayi % 2 == 0:
# # # # #         return "Çift"
# # # # #     else:
# # # # #         return "Tek"
# # # # # print(cift_tek(8))
# # # # # print(cift_tek(11))

# # # # def isaret(sayi):
# # # #     if sayi > 0:
# # # #         return "Pozitif"
# # # #     elif sayi < 0:
# # # #         return "Negatif"
# # # #     else:
# # # #         return "Sıfır"
# # # # print(isaret(5))
# # # # print(isaret(-2))
# # # # print(isaret(0))

# # # def selam_ver(isim):
# # #     print ("Merhaba" , isim)
# # # selam_ver("Can")

# # def ikiyle_carp(sayi):
# #     return sayi * 2
# # sonuc = ikiyle_carp(5)
# # print (sonuc)

# # def cift_tek(sayi):
# #     if sayi % 2 == 0:
# #         return "Çift"
# #     else:
# #         return "Tek"
# # print(cift_tek(8))
# # print(cift_tek(11))

# # def isaret(sayi):
# #     if sayi > 0:
# #         return "Pozitif"
# #     elif sayi < 0:
# #         return "Negatif"
# #     else:
# #         return "Sıfır"
# # print(isaret(5))
# # print(isaret(-2))
# # print(isaret(0))

# # def not_durumu(notu):
# #     if notu >= 50:
# #         return "Geçti"
# #     else:
# #         return "Kaldı"
# # print(not_durumu(90))
# # print(not_durumu(45))

# # def buyuk_mu(sayi):
# #     if sayi > 10:
# #         return "Büyük"
# #     else:
# #         return "Küçük veya eşit"
# # print(buyuk_mu(15))
# # print(buyuk_mu(10))

# # def kullanici_kontrol(isim):
# #     if not isim:
# #         return "Geçersiz Kullanıcı Adı"
# #     else:
# #         return "Kullanıcı adı kabul edildi"
# # print(kullanici_kontrol(""))
# # print(kullanici_kontrol("Can"))

# # def mutlak_deger(sayi):
# #     if sayi < 0:
# #         return -sayi
# #     else:
# #         return sayi
# # print (mutlak_deger(5))
# # print (mutlak_deger(-3))
# # print (mutlak_deger(0))

# # def en_buyuk(a,b):
# #     if a > b:
# #         return a
# #     else:
# #         return b
# # print(en_buyuk(7,3))
# # print(en_buyuk(2,9))
# # print(en_buyuk(5,5))

# # def kisa_mi(metin):
# #     if len(metin) < 5:
# #         return "Kısa"
# #     else:
# #         return "Uzun"
# # print(kisa_mi("Ali"))
# # print(kisa_mi("Merhaba"))

# # def not_harf(notu):
# #     if notu >= 90:
# #         return "A"
# #     elif notu >= 70:
# #         return "B"
# #     elif notu >= 50:
# #         return "C"
# #     else:
# #         return "Kaldı"
# # print(not_harf(95))
# # print(not_harf(75))
# # print(not_harf(55))
# # print(not_harf(30))

# def parola_kontrol(parola):
#     if not parola:
#         return "Parola boş olamaz"
#     elif len(parola) < 8:
#         return "Parola çok Kısa"
#     else:
#         return "Parola kabul edildi"
# print(parola_kontrol(""))
# print(parola_kontrol("12345"))
# print(parola_kontrol("12345678"))

# def yas_uygun_mu(yas):
#     if yas < 18:
#         return "Uygun değil"
#     else:
#         return "Uygun"
# print(yas_uygun_mu(16))
# print(yas_uygun_mu(18))
# print(yas_uygun_mu(25))

# def sicaklik_durumu(derece):
#     if derece < 0:
#         return "Donuyor"
#     elif derece >= 20:
#         return "Sıcak"
#     else:
#         return "Serin"
# print(sicaklik_durumu(-5))
# print(sicaklik_durumu(10))
# print(sicaklik_durumu(25))

# def indirim_var_mi(tutar):
#     if tutar >= 100:
#         return "İndirim uygulandı"
#     else:
#         return "İndirim yok"
# print(indirim_var_mi(80))
# print(indirim_var_mi(100))
# print(indirim_var_mi(150))

# def bolunebilir_mi(sayi):
#     if sayi % 3 == 0:
#         return "Bölünür"
#     else:
#         return "Bölünmez"
# print(bolunebilir_mi(9))
# print(bolunebilir_mi(10))
# print(bolunebilir_mi(12))

# def metin_var_mi(metin):
#     if not metin:
#         return "Metin yok"
#     else:
#         return "Metin var"
# print(metin_var_mi(""))
# print(metin_var_mi("Python"))

# def sayi_kontrol(sayi):
#     if sayi > 0 and sayi % 2 == 0:
#         return "Çift ve pozitif"
#     else:
#         return "Uygun değil"
# print(sayi_kontrol(4))
# print(sayi_kontrol(-2))
# print(sayi_kontrol(3))

# def giris_izni(yas , uye_mi):
#     if yas >= 18 and uye_mi == True:
#         return "Giriş izni var"
#     else: 
#         return "Giriş izni yok"
# print(giris_izni(20, True))
# print(giris_izni(17, True))
# print(giris_izni(22, False))

# def indirim_hakki(yas,ogrenci_mi):
#     if yas < 18 or ogrenci_mi == True:
#         return "İndirim var"
#     else:
#         return "İndirim yok"
# print(indirim_hakki(16, False))
# print(indirim_hakki(25, True))
# print(indirim_hakki(25, False))

# def sistem_girisi(yas,sifre_dogru_mu):
#     if yas >= 18 and sifre_dogru_mu == True:
#         return "Giriş başarılı"
#     else:
#         return "Giriş başarısız"
# print(sistem_girisi(20, True))
# print(sistem_girisi(17, True))
# print(sistem_girisi(20, False))

# def kampanya_hakki(alisveris, kupon_var_mi):
#     if alisveris >= 200 or kupon_var_mi == True:
#         return "Kampanya aktif"
#     else:
#         return "Kampanya yok"
# print(kampanya_hakki(250, False))
# print(kampanya_hakki(150, True))
# print(kampanya_hakki(100, False))

# def uygun_mu(yas,kimlik_var_mi,uye_mi):
#     if yas >= 18 and kimlik_var_mi and uye_mi:
#         return "Uygun"
#     else:
#         return "Uygun değil"
# print(uygun_mu(20, True, True))
# print(uygun_mu(17, True, True))
# print(uygun_mu(20, False, True))
# print(uygun_mu(20, True, False))
