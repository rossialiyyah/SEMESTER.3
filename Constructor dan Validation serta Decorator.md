# PROJECT Constructor dan Validation serta Decorartor

## 1. Deskripsi Project

Project Bank Account merupakan program sederhana yang menerapkan konsep Object-Oriented Programming (OOP) menggunakan bahasa Python. Program ini membahas penggunaan Constructor, Validation, dan Decorator untuk mengelola informasi rekening bank Dalam project ini, Constructor digunakan untuk memberikan nilai awal pada Object ketika dibuat. Validation digunakan untuk memeriksa apakah saldo yang dimasukkan memenuhi ketentuan. Sementara itu, Decorator digunakan untuk memberikan fungsi tambahan pada Method melalui penggunaan `@classmethod.`

## 2. Source Code Python

A. Constructor dan Validation

Nama file: `Constructor.py`

    class BankAccount:
        no = ""
        saldo = 0
    
        # Constructor
        def __init__(self, no, saldo=0):
            # Validation
            if saldo < 0:
                raise ValueError("Saldo tidak boleh negatif")
    
            self.no = no
            self.saldo = saldo
    
    
    # Membuat Object
    budi = BankAccount("1234567890", 1000)
    
    # Menampilkan informasi rekening
    print("Nomor Rekening:", budi.no)
    print("Saldo:", budi.saldo)
    
Hasil Output:

`Nomor Rekening: 1234567890
Saldo: 1000`

Apabila saldo diberikan nilai negatif, misalnya:

`eko = BankAccount("0987654321", -1000)`

Maka program akan menghasilkan error:

`ValueError: Saldo tidak boleh negatif`

B. Decorator
Nama file: `Decorator.py`

    class BankAccount:
        no = ""
        balance = 0
        active = True
    
        def __init__(self, no, balance=0):
            self.no = no
            self.balance = balance
    
        # Class Method Decorator
        @classmethod
        def disabled(cls, no, balance=0):
            result = cls(no, balance)
            result.active = False
            return result
    
    
    # Membuat Object rekening aktif
    bank_account1 = BankAccount("1", 10000)
    
    # Membuat Object rekening nonaktif
    bank_account2 = BankAccount.disabled("2", 20000)
    
    
    # Menampilkan informasi rekening
    print(f"Bank account {bank_account1.no} has balance {bank_account1.balance} and status {bank_account1.active}")

Hasil Output:

    Bank account 1 has balance 10000 and status True
    Bank account 2 has balance 20000 and status False

## 3. Penjelasan Materi

A. Constructor

1. Pengertian Constructor

Constructor merupakan metode khusus dalam sebuah Class yang secara otomatis dijalankan ketika sebuah Object dibuat. Constructor digunakan untuk memberikan nilai awal atau melakukan inisialisasi terhadap Attributes yang dimiliki oleh Object.

Dalam Python, Constructor menggunakan metode khusus bernama `__init__()`.

Contoh coding:

    class BankAccount:
        def __init__(self, no, saldo=0):
            self.no = no
            self.saldo = saldo

Penjelasan:
- `class BankAccount` merupakan Class yang digunakan untuk membuat Object rekening bank.
- `__init__()` merupakan Constructor yang dijalankan secara otomatis ketika Object dibuat.
- `self` digunakan untuk mengacu pada Object yang sedang dibuat.
- `no` merupakan Parameter untuk menerima nomor rekening.
- `saldo=0` merupakan Parameter dengan nilai default atau nilai bawaan sebesar 0.
- `self.no` dan `self.saldo` digunakan untuk menyimpan informasi ke dalam Attributes Object.

Contoh pemanggilan:

    budi = BankAccount("1234567890", 1000)

Pada contoh tersebut, Object budi dibuat dengan nomor rekening `1234567890` dan saldo awal `1000`.

Kesimpulan: Constructor digunakan untuk menginisialisasi atau memberikan nilai awal pada Attributes ketika sebuah Object dibuat sehingga tidak perlu mengisi atribut satu per satu secara manual.

B. Validation

1. Pengertian Validation

Validation merupakan proses pemeriksaan atau pengecekan terhadap data yang dimasukkan ke dalam program. Validation bertujuan untuk memastikan bahwa data yang diberikan sesuai dengan ketentuan sebelum digunakan atau disimpan oleh program.

Dalam Python, Validation dapat dilakukan menggunakan kondisi `if` dan menghasilkan kesalahan menggunakan `raise ValueError`.

Contoh coding:

    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
    
        self.no = no
        self.saldo = saldo

Penjelasan:
- `if saldo < 0` digunakan untuk memeriksa apakah saldo kurang dari nol.
- `raise ValueError()` digunakan untuk menghasilkan pesan kesalahan apabila saldo tidak memenuhi ketentuan.
- `"Saldo tidak boleh negatif"` merupakan pesan kesalahan yang ditampilkan.
- `self.no` dan `self.saldo` digunakan untuk menyimpan data apabila validasi berhasil dilewati.

Contoh penggunaan:

    budi = BankAccount("1234567890", 1000)

Kode tersebut berhasil dijalankan karena saldo tidak negatif. Sedangkan:

    eko = BankAccount("0987654321", -1000)

Kode tersebut menghasilkan error karena saldo memiliki nilai negatif.

Kesimpulan: Validation digunakan untuk memeriksa kebenaran dan kesesuaian data agar program dapat menghindari masukan yang tidak memenuhi ketentuan.

C. Decorator

1. Pengertian Decorator

Decorator merupakan fitur dalam Python yang digunakan untuk memberikan fungsi tambahan atau mengubah cara kerja suatu fungsi maupun Method tanpa harus mengubah isi utama fungsi tersebut Decorator ditandai dengan simbol @ yang ditulis sebelum definisi fungsi atau Method Salah satu jenis Decorator dalam pemrograman berorientasi objek adalah `@classmethod`.

    Contoh coding:
    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = False
        return result

Penjelasan:
- `@classmethod` merupakan Decorator yang menjadikan sebuah Method sebagai Class Method.
- `disabled` merupakan nama Method yang digunakan untuk membuat rekening dengan status nonaktif.
- `cls` mengacu pada Class yang bersangkutan.
- `result = cls(no, balance)` digunakan untuk membuat Object baru berdasarkan Class tersebut.
- `result.active = False` digunakan untuk mengubah status rekening menjadi nonaktif.
- `return result` digunakan untuk mengembalikan Object yang telah dibuat.

Contoh pemanggilan:

    bank_account1 = BankAccount("1", 10000)
    
    bank_account2 = BankAccount.disabled("2", 20000)

Penjelasan:
- `bank_account1` merupakan Object rekening yang dibuat secara normal sehingga statusnya tetap True.
- `bank_account2` merupakan Object yang dibuat menggunakan `Method disabled()` sehingga statusnya menjadi False.

Kesimpulan: Decorator digunakan untuk memberikan perilaku tambahan pada fungsi atau Method. Dalam contoh ini, `@classmethod` memungkinkan pembuatan Object melalui Method yang menggunakan Class sebagai acuannya.

## 4. Perbedaan Constructor, Validation, dan Decorator

| Materi | Pengertian | Fungsi dalam Project |
| --- | --- | --- |
| Constructor | Metode khusus yang dijalankan otomatis saat Object dibuat. | Memberikan nilai awal nomor rekening dan saldo. |
| Validation | Proses pemeriksaan data sebelum digunakan. | Memastikan saldo tidak bernilai negatif. |
| Decorator | Fitur untuk memberikan perilaku tambahan pada fungsi atau Method. | Membuat rekening dengan status nonaktif menggunakan `@classmethod`. |

## 5. Kesimpulan Project

Berdasarkan Project Bank Account, dapat disimpulkan bahwa Constructor, Validation, dan Decorator merupakan bagian dari konsep pemrograman Python yang membantu pengelolaan Object.

Constructor menggunakan metode `__init__()` untuk memberikan nilai awal pada Attributes ketika Object dibuat. Validation digunakan untuk memeriksa data yang dimasukkan agar sesuai dengan ketentuan, seperti memastikan saldo tidak bernilai negatif. Sementara itu, Decorator `@classmethod` digunakan untuk membuat Method yang berhubungan dengan Class dan dapat memberikan fungsi tambahan dalam proses pembuatan Object.

Melalui project ini, konsep Constructor, Validation, dan Decorator dapat dipahami melalui penerapan sederhana dalam sistem rekening bank.
