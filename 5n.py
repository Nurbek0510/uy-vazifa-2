n = int(input("Mahsulotlar soni: "))

with open("mahsulotlar.txt", "w", encoding="utf-8") as fayl:
    for i in range(n):
        malumot = input().split()

        nomi = malumot[0]
        narxi = malumot[1]
        miqdori = malumot[2]

        fayl.write(nomi + " " + narxi + " " + miqdori + "\n")