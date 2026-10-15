
# togri_parol = "12345"
#
# while True:
#     parol = input("Parolni kiriting: ")
#
#     if parol == togri_parol:
#         print("Parol to'g'ri! Dastur tugadi.")
#         break
#     else:
#         print("Parol noto'g'ri! Qayta kiriting.")

# matn = input("Matn kiriting: ")
#
# sozlar = matn.split()
#
# for soz in sozlar:
#     if soz.lower().startswith("a"):
#         print(soz)

# matn = input("Matn kiriting: ")
#
# unlilar = "aeiouoʻo‘AEIOUOʻO‘"
# son = 0
#
# for harf in matn:
#     if harf in unlilar:
#         son += 1
#
# print("Unli harflar soni:", son)




# matn = input("Matn kiriting: ")
#
# natija = matn.replace("i", "j")
#
# print("Natija:", natija)


# kun = int(input("Kun kiriting: "))
# oy = int(input("Oy kiriting (1-12): "))
# yil = int(input("Yil kiriting: "))
#
# oylar = [
#     "yanvar", "fevral", "mart", "aprel",
#     "may", "iyun", "iyul", "avgust",
#     "sentabr", "oktabr", "noyabr", "dekabr"
# ]
#
# if 1 <= oy <= 12 and 1 <= kun <= 31 and yil > 0:
#     print(f"{kun}-{oylar[oy - 1]}, {yil} yil")
# else:
#     print("Sana noto'g'ri kiritildi!")


# matn = input("Matn kiriting: ")
#
# katta = 0
# kichik = 0
# raqam = 0
# belgi = 0
#
# for harf in matn:
#     if harf.isupper():
#         katta += 1
#     elif harf.islower():
#         kichik += 1
#     elif harf.isdigit():
#         raqam += 1
#     elif not harf.isspace():
#         belgi += 1
#
# print("Katta harflar soni:", katta)
# print("Kichik harflar soni:", kichik)
# print("Raqamlar soni:", raqam)
# print("Belgilar soni:", belgi)



# matn = input("Matn kiriting: ")
#
# sozlar = matn.split()
#
# print("So'zlar:", sozlar)
# print("So'zlar soni:", len(sozlar))


import re

matn = input("Matn kiriting: ")
xato = False

# Matnda kamida 3 ta gap borligini tekshirish
gaplar = re.split(r'[.!?]+', matn)
gaplar = [gap.strip() for gap in gaplar if gap.strip()]

if len(gaplar) < 3:
    print("Xato: matn kamida 3 ta gapdan iborat bo'lishi kerak!")
    xato = True

# Har bir gap katta harf bilan boshlanishini tekshirish
for gap in gaplar:
    if not gap[0].isupper():
        print("Xato: gap katta harf bilan boshlanmagan:", gap)
        xato = True

# Nuqta va vergul oldi-ketidagi bo'sh joylarni tekshirish
for i in range(len(matn)):
    if matn[i] in ".,":
        if i > 0 and matn[i - 1] == " ":
            print("Xato: tinish belgisidan oldin bo'sh joy bor!")
            xato = True

        if i < len(matn) - 1 and matn[i + 1] != " ":
            print("Xato: tinish belgisidan keyin bo'sh joy yo'q!")
            xato = True

if not xato:
    print("Matn to'g'ri yozilgan!")
else:
    print("Matnda xatolar aniqlandi.")
