class bioskop:
    pass

class karyawan:
    pass

bioskop1 = bioskop()
bioskop2 = bioskop()

print(type(bioskop1))
print(type(bioskop2))

karyawan1 = karyawan()
karyawan2 = karyawan()

print(type(karyawan1))
print(type(karyawan2))

# instance attribute

karyawan1 = karyawan()
karyawan1.nomor = 12345
karyawan1.posisi = "Kasir & Ticketing"
karyawan1.nama = "Harley"

print(karyawan1.nomor)
print(karyawan1.posisi)
print(karyawan1.nama)

karyawan2 = karyawan()
karyawan2.nomor = 98765
karyawan2.posisi = "Operator Proyektor"
karyawan2.nama = "Arthur"

print(karyawan2.nomor)
print(karyawan2.posisi)
print(karyawan2.nama)
