#parameter biasa
def luas_persegi_panjang(panjang, lebar):
    print("Luas:", panjang * lebar)
    
luas_persegi_panjang(8, 5) #argumen posisional
luas_persegi_panjang(lebar=4, panjang=6) #keyword argumen

#nilai default
def sapa(nama, salam='halo'):
    print(salam + ", " + nama + "!")
    
sapa('Budi') #output: halo, budi
sapa('Ani', 'selamat pagi') #output: selamat pagi, ani!