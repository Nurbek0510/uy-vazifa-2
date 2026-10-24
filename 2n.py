nomi = input("Mahsulot nomi: ")
narxi = input("Narxi: ")
miqdori = input("Miqdori: ")

with open("mahsulot.txt", "w", encoding="utf-8") as fayl:
    fayl.write(nomi + "\n")
    fayl.write(narxi + "\n")
    fayl.write(miqdori)