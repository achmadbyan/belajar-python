# --- Fungsi tanpa parameter dan return ---
def garis_pemisah():
    print("-" * 35)

# --- Fungsi dengan parameter, tanpa return ---
def sapa_siswa(nama, kelas):
    print(f"Halo, {nama} dari kelas {kelas}!")

# --- Fungsi dengan parameter dan return ---
def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_keliling_persegi(sisi):
    return 4 * sisi

# --- Memanggil semua fungsi ---
garis_pemisah()
sapa_siswa("Byan", "X RPL 1")
sapa_siswa("Ulin", "X RPL 1")
garis_pemisah()

l_segitiga = hitung_luas_segitiga(10, 6)
print(f"Luas segitiga (alas=10, tinggi=6): {l_segitiga}")

k_persegi = hitung_keliling_persegi(7)
print(f"Keliling persegi (sisi=7): {k_persegi}")

# Fungsi langsung dalam ekspresi
print(f"Total luas + keliling = {l_segitiga + k_persegi}")