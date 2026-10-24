marka = input("Marka: ")
yil = input("Yil: ")
narx = input("Narx: ")

with open("avtomobil.txt", "w", encoding="utf-8") as fayl:
    fayl.write(marka + "\n")
    fayl.write(yil + "\n")
    fayl.write(narx)