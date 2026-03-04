# # # # ######### SAYI TEK Mİ ÇİFT Mİ #############
# # # # # sayi = int(input("Bir sayı gir: "))

# # # # # if sayi % 2 == 0:
# # # # #     print(sayi,"Sayısı Çifttir")
# # # # # else:
# # # # #     print(sayi,"Sayısı Tektir") 

# # # # ###########################################


# # # # while True:
# # # #     sayi = int(input("Sayı Girin: "))
# # # #     if sayi == 0:
# # # #         print("Program Bitti")
# # # #         break
# # # #     else:
# # # #         print("Yazılan Sayı:" , sayi)

# # # ##############################################

# # # toplam = 0 
# # # while True:
# # #     sayi = int(input("Sayı Gir: "))
# # #     if sayi == 0:
# # #         print(f"Toplam: {toplam}")
# # #         break
# # #     else: 
# # #         toplam += sayi

# # # ##############################################
# # # toplam = 0
# # # adet = 0

# # # while True:
# # #     sayi = int(input("Sayı Gir: "))
# # #     toplam += sayi
# # #     adet += 1
# # #     ortalama = toplam / adet

# # #     if sayi == 0:
# # #         print("Program Bitti")
# # #         print(f"Toplam: {toplam}")
# # #         print(f"Adet: {adet}")
# # #         print(f"Ortalama: {ortalama}")
# # #         break


# # toplam = 0
# # adet = 0

# # while True:
# #     sayi = int(input("Sayı Gir: "))

# #     if sayi == 0:
# #         print("Program Bitti")
# #         break

# #     toplam += sayi
# #     adet += 1

# # if adet == 0:
# #     print("Sayı Girilmedi!")
# # else:
# #     ortalama = toplam / adet

# # print(f"Toplam: {toplam}")
# # print(f"Adet: {adet}")
# # print(f"Ortalama: {ortalama}")

# #############################################

# # for i in range(10 , 0 , -1):
# #     print(i)

# # for i in range (2 , 21 , 2):
# #     print(i)

# #############################################

# # toplam = 0
# # adet = 0

# # while True:
# #     sayi = int(input("Sayı gir:"))
# #     if sayi == 0:
# #         print("Program Bitti")
# #         break
# #     else:
# #         toplam += sayi
# #         adet += 1
# # print (f"Toplam:{toplam}")
# # print (f"Adet:{adet}")

# ##########################################

# i = 0
# enbuyuk = None

# while i < 5:
#     sayi = int(input("Sayı Gir: "))

#     if enbuyuk is None or sayi > enbuyuk:
#         enbuyuk = sayi
#     i += 1

# print("En Büyük Sayı:" , enbuyuk)

# ###########################################

en_buyuk = None

while True:

    sayi = int(input("Sayı: "))

    if sayi == 0:
        break

    if en_buyuk is None or sayi > en_buyuk:
        en_buyuk = sayi

print("En büyük sayı:", en_buyuk)