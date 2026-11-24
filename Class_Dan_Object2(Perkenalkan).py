class karyawan:
    nomor = 12345
    posisi = "Kasir & Ticketing"
    nama = "Harley"

    def perkenalkan(self):
        print(f"Halo nama saya {self.nama}, saya karyawan baru")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")


karyawan = karyawan()
karyawan.nama = "Harley"
karyawan.perkenalkan()
karyawan.hello("Arthur")

