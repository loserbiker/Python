# # # ######### SAYI TEK Mİ ÇİFT Mİ #############
# # # # sayi = int(input("Bir sayı gir: "))

# # # # if sayi % 2 == 0:
# # # #     print(sayi,"Sayısı Çifttir")
# # # # else:
# # # #     print(sayi,"Sayısı Tektir") 

# # # ###########################################


# # # while True:
# # #     sayi = int(input("Sayı Girin: "))
# # #     if sayi == 0:
# # #         print("Program Bitti")
# # #         break
# # #     else:
# # #         print("Yazılan Sayı:" , sayi)

# # ##############################################

# # toplam = 0 
# # while True:
# #     sayi = int(input("Sayı Gir: "))
# #     if sayi == 0:
# #         print(f"Toplam: {toplam}")
# #         break
# #     else: 
# #         toplam += sayi

# # ##############################################
# # toplam = 0
# # adet = 0

# # while True:
# #     sayi = int(input("Sayı Gir: "))
# #     toplam += sayi
# #     adet += 1
# #     ortalama = toplam / adet

# #     if sayi == 0:
# #         print("Program Bitti")
# #         print(f"Toplam: {toplam}")
# #         print(f"Adet: {adet}")
# #         print(f"Ortalama: {ortalama}")
# #         break


# toplam = 0
# adet = 0

# while True:
#     sayi = int(input("Sayı Gir: "))

#     if sayi == 0:
#         print("Program Bitti")
#         break

#     toplam += sayi
#     adet += 1

# if adet == 0:
#     print("Sayı Girilmedi!")
# else:
#     ortalama = toplam / adet

# print(f"Toplam: {toplam}")
# print(f"Adet: {adet}")
# print(f"Ortalama: {ortalama}")


for i in range(10 , 0 , -1):
    print(i)