class Karyawan:
    nama = ""
    posisi = ""
    nomor = ""

    def perkenalkan(self):
        print(f"Halo, nama saya {self.nama}.")
        print(f"Saya bekerja sebagai {self.posisi}.")

    def berbicara(self, pesan):
        print(f"{self.nama}: {pesan}")


# Membuat objek karyawan pertama
karyawan1 = Karyawan()
karyawan1.nama = "Anya"
karyawan1.posisi = "Kasir"
karyawan1.nomor = "K001"

# Membuat objek karyawan kedua
karyawan2 = Karyawan()
karyawan2.nama = "Arthur"
karyawan2.posisi = "Staf Bioskop"
karyawan2.nomor = "K002"

# Membuat objek karyawan ketiga
karyawan3 = Karyawan()
karyawan3.nama = "Leon"
karyawan3.posisi = "Petugas Keamanan"
karyawan3.nomor = "K003"

# Membuat objek karyawan keempat
karyawan4 = Karyawan()
karyawan4.nama = "Clara"
karyawan4.posisi = "Supervisor Bioskop"
karyawan4.nomor = "K004"


# Memulai program
print("======================================")
print("       SISTEM KARYAWAN BIOSKOP")
print("======================================")


# Perkenalan karyawan
print("\n--- Perkenalan Karyawan ---")

karyawan1.perkenalkan()
print()

karyawan2.perkenalkan()
print()

karyawan3.perkenalkan()
print()

karyawan4.perkenalkan()


# Percakapan salam pagi
print("\n--- Percakapan Pagi Hari ---")

karyawan1.berbicara("Selamat pagi semuanya!")
karyawan2.berbicara("Selamat pagi, Anya! Wah, kamu kelihatannya sangat bersemangat hari ini.")
karyawan1.berbicara("Karena ini hari pertama saya bekerja, makanya saya sangat bersemangat.")
karyawan3.berbicara("Pagi! Bagaimana kabar kalian semua hari ini?")
karyawan4.berbicara("Selamat pagi, semuanya. Saya harap kalian sudah siap untuk bekerja.")

karyawan1.berbicara("Saya baik-baik saja, Clara. Bagaimana dengan Anda?")
karyawan4.berbicara("Saya juga baik-baik saja, terima kasih.")
karyawan2.berbicara("Saya datang lebih awal hari ini untuk memeriksa ruangan bioskop.")
karyawan3.berbicara("Saya juga datang lebih awal. Saya sudah memeriksa pintu masuk utama.")
karyawan1.berbicara("Bagus sekali. Sepertinya semua orang sudah siap.")
karyawan4.berbicara("Bagus. Sekarang mari kita bahas jadwal film hari ini.")
