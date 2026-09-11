print("=" * 40)
print("   SISTEM PENILAIAN SISWA")
print("=" * 40)
nama = input("Nama siswa          :")
nilai_uts = float(input("Nilai UTS (0-100): "))
nilai_uas = float(input("Nilai UAS (0-100): "))
nilai_tugas = float(input("Nilai TUgas    :"))

rata = (nilai_uts * 0.3) + (nilai_uas * 0.5) + (nilai_tugas * 0.2)

if rata >= 90:
    predikat = "A - Sangat baik"
elif rata >= 80:
    predikat= "B - Baik"
elif rata >= 70:
    predikat = "C - Cukup"
elif rata >= 60:
    predikat = "D - Kurang"
else:
    predikat = "E - Sangat Kurang"
    
lulus = rata >= 70

print()
print("=" * 40)
print("   HASIL PENILAIAN")
print("=" * 40)
print("Nama :", nama)
print("Rata-Rata :", round(rata, 2))
print("Predikat :", predikat)
print("Status :", "LULUS" if lulus else "TIDAK LULUS")
