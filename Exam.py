from math import *

# begin9
# a=int(input("a soni: "))
# b=int(input("b soni: "))
# print(f"o'rta geometrigi: {sqrt(a*b)}")

# integer16
# son=int(input("uch xonali son kiriting: "))
# yuzlik=son//100*100
# onlik=son%10*10
# birlik=son%100//10
# print(f"Natija: {yuzlik+onlik+birlik}")

# boolean12
# a=int(input("a soni: "))
# b=int(input("b soni: "))
# c=int(input("c soni: "))
# d=a>0 and b>0 and c>0
# print(f"Natija: {d}")

# if28
# yil=int(input("Yilni kiriting: "))
# if yil%100%4==0 and yil//100%4==0:
#         print("Kabisa yil 366 kun.")
# else:
#         print("365")

# case8
# d=int(input("Kunni kiriting: "))
# m=int(input("Oyni kiriting: "))
# match m:
#     case 1:
#         if d>0 and d<=31:
#             natija = f"Yanvar {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 2:
#         if d>0 and d<=28:
#             natija = f"Fevral {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 3:
#         if d>0 and d<=31:
#             natija = f"Mart {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 4:
#         if d>0 and d<=28:
#             natija = f"Aprel {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 5:
#         if d>0 and d<=28:
#             natija = f"May {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 6:
#         if d>0 and d<=28:
#             natija = f"Iyun {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 7:
#         if d>0 and d<=28:
#             natija = f"Iyul {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 8:
#         if d>0 and d<=28:
#             natija = f"Avgust {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 9:
#         if d>0 and d<=28:
#             natija = f"Sentyabr {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 10:
#         if d>0 and d<=28:
#             natija = f"Oktyabr {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 11:
#         if d>0 and d<=28:
#             natija = f"Noyabr {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case 12:
#         if d>0 and d<=28:
#             natija = f"Dekabr {d} kun"
#         else:
#             natija = 'Bunaqa kun yo\'q'
#     case _:
#         natija = "Bunaqa oy yo'q"