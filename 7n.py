malumot = input("Nomi, narxi va miqdorini kiriting: ").split()

nomi = malumot[0]
narxi = malumot[1]
miqdori = malumot[2]

with open("mahsulotlar.txt", "a", encoding="utf-8") as fayl:
    fayl.write(nomi + " " + narxi + " " + miqdori + "\n")