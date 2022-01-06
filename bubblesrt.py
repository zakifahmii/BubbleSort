print("================================")
print("Program mengurut Bubble Sort")
print("================================")
#ascending
def bubble1(angka):
    for i in range(len(angka)-1,0,-1):
        post = 0
        for j in range(1,i+1):
            ps = angka[post]
            if ps < angka[j]:
                post = j
        angka[post],angka[i] = angka[i],angka[post]

#descanding
def bubble2(angka):
    for i in range(len(angka)-1,0,-1):
        post = 0
        for j in range(1,i+1):
            ps = angka[post]
            if ps < angka[j]:
                post = j
        angka[post],angka[i] = angka[i],angka[post]

back = print("")
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))
angka4 = int(input("Masukkan angka keempat: "))
angka5 = int(input("Masukkan angka kelima: "))
angka6 = int(input("Masukkan angka keenam: "))
angka7 = int(input("Masukkan angka ketujuh: "))
angka8 = int(input("Masukkan angka kedelapan: "))
angka9 = int(input("Masukkan angka kesembilan: "))
angka10 = int(input("Masukkan angka kesepuluh: "))

print("Pilih Metode: ")
print(f"1. Ascending\n2. Descending")
pilih = input("Metode yanng di pilih: ")

angka = [angka1, angka2, angka3, angka4, angka5, angka6, angka7, angka8, angka9, angka10]
print("=======================================")
print("Data sebelum di urutkan: ")
print(angka)
print("Data setelah di urutkan: ")
if pilih == ("1"):
    bubble1(angka)
    print(angka)
elif pilih == ("2"):
    bubble2(angka)
    print(angka)
else:
    print("Input Error! Mohon pilih angka 1 atau 2")
back