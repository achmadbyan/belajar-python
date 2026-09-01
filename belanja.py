total = int(input("Masukkan Total Belanja:" ))

if (total >= 500000):
    diskon = 0.2
else:
    if (total >= 200000):
        diskon = 0.1
    else:
        diskon = 0

bayar = total - (total * diskon)
print("Total : Rp.", total)
print("diskon : ", diskon * 100 , "%")
print("bayar : Rp.", bayar)