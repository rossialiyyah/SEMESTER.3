# PROJECT: PERKENALKAN

## 1. Deskripsi Project

Project Perkenalan Karyawan merupakan program sederhana menggunakan bahasa Python dengan konsep Object-Oriented Programming (OOP). Program ini bertujuan untuk memperkenalkan identitas seorang karyawan melalui informasi nomor karyawan, posisi pekerjaan, dan nama.

Dalam project ini, Class digunakan sebagai rancangan untuk membuat Object karyawan. Setiap Object memiliki Attributes yang menyimpan informasi karyawan serta Methods yang digunakan untuk menjalankan proses perkenalan.

## 2. Source Code Python

Nama file: `Class_Dan_Object.py`

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

## 3. Hasil Output Program

    Halo nama saya Harley, saya karyawan baru
    Halo Arthur, nama saya Harley

## 4. Penjelasan Materi

A. Class dan Object

1. Pengertian Class

Class merupakan cetak biru (blueprint) atau kerangka dasar yang digunakan untuk membuat Object dalam pemrograman berorientasi objek (OOP). Class berfungsi sebagai tempat untuk mendefinisikan Attributes dan Methods yang nantinya dapat digunakan oleh Object.

Dalam Python, Class dibuat menggunakan kata kunci class, kemudian diikuti dengan nama Class.

  Contoh coding:

    class Karyawan:
        nomor = 12345
        posisi = "Kasir & Ticketing"
        nama = "Harley"

Penjelasan:

- `class` merupakan kata kunci untuk membuat sebuah Class.
- `Karyawan` merupakan nama Class yang dibuat.
- Class Karyawan menjadi rancangan dasar untuk membuat Object karyawan.
- Informasi nomor, posisi, dan nama merupakan Attributes yang didefinisikan di dalam Class.

2. Pengertian Object

Object merupakan hasil pembentukan atau perwujudan dari sebuah Class. Object digunakan untuk mengakses Attributes dan menjalankan Methods yang telah didefinisikan di dalam Class.

  Contoh coding:

    karyawan1 = Karyawan()

Penjelasan:

- `karyawan1` merupakan nama variabel yang menyimpan Object.
- `Karyawan()` merupakan pemanggilan Class untuk membuat Object baru.
- Object `karyawan1` dibuat berdasarkan rancangan Class `Karyawan`.

Satu Class juga dapat digunakan untuk membuat beberapa Object dengan informasi yang berbeda.

Kesimpulan: Class merupakan rancangan untuk membuat suatu objek, sedangkan Object merupakan hasil pembuatan dari Class tersebut.

B. Class dan Attributes

1. Pengertian Attributes

Attributes merupakan variabel atau data yang digunakan untuk menyimpan informasi maupun karakteristik yang dimiliki oleh sebuah Class atau Object.

Attributes berfungsi untuk menggambarkan identitas suatu Object sehingga setiap Object dapat memiliki informasi sesuai dengan kebutuhan program.

  Contoh coding:

    class Karyawan:
        nomor = 12345
        posisi = "Kasir & Ticketing"
        nama = "Harley"

Penjelasan:

Pada Class `Karyawan`, terdapat tiga Attributes, yaitu:

| Attributes | Nilai | Keterangan |
| --- | --- | --- |
| `nomor` | 12345 | Nomor identitas karyawan |
| `posisi` | Kasir & Ticketing | Jabatan atau perkerjaan karyawan |
| `nama` | Harley | Nama Karyawan |

Ketiga Attributes tersebut didefinisikan langsung di dalam Class sehingga termasuk Class Attributes.

2. Pengertian Instance Attribute

Instance Attribute merupakan atribut yang dimiliki secara khusus oleh masing-masing Object. Setiap Object dapat memiliki nilai atribut yang berbeda meskipun berasal dari Class yang sama.

  Contoh coding:

    karyawan1 = Karyawan()
    karyawan1.nama = "Harley"

Penjelasan:
- `karyawan1` merupakan Object dari Class `Karyawan`.
- `karyawan1.nama` merupakan atribut yang diberikan secara khusus kepada Object tersebut.
- `"Harley"` merupakan nilai yang disimpan ke dalam atribut nama.

Pada contoh ini, `nama` sudah didefinisikan sebagai Class Attribute. Ketika `karyawan1.nama` diberikan nilai baru, Python membuat Instance Attribute yang menimpa nilai Class Attribute ketika diakses melalui Object tersebut.

C. Class dan Methods

1. Pengertian Methods

Methods merupakan fungsi yang didefinisikan di dalam sebuah Class dan digunakan untuk menjalankan tindakan atau perilaku tertentu.

Methods berfungsi untuk mengolah data, menampilkan informasi, serta menjalankan perintah yang berhubungan dengan Object.

Dalam Python, Methods dibuat menggunakan kata kunci `def` yang ditulis di dalam Class.

  Contoh coding:

    def perkenalkan(self):
        print(f"Halo nama saya {self.nama}, saya karyawan baru")

Penjelasan:

- `def` merupakan kata kunci untuk membuat fungsi atau Method.
- `perkenalkan` merupakan nama Method yang dibuat.
- `self` mengacu pada Object yang sedang menjalankan Method.
- `self.nama` digunakan untuk mengambil nilai atribut nama dari Object.
- `print()` digunakan untuk menampilkan kalimat perkenalan.

Untuk menjalankan Method tersebut, digunakan perintah:
karyawan1.perkenalkan()

Hasil output:

`Halo nama saya Harley, saya karyawan baru`

D. Methods dan Parameters

1. Pengertian Parameters

Parameters merupakan variabel yang digunakan dalam sebuah Method untuk menerima nilai atau informasi dari luar ketika Method dipanggil. Dengan adanya Parameters, sebuah Method dapat menerima data tambahan sehingga penggunaannya menjadi lebih fleksibel

Contoh coding:
def hello(self, nama):
    print(f"Halo {nama}, nama saya {self.nama}")

Penjelasan:
- `hello` merupakan nama Method.
- `self` mengacu pada Object yang sedang menjalankan Method.
- `nama` merupakan Parameter yang digunakan untuk menerima nama orang lain.
- `{nama}` menampilkan nama yang diterima melalui Parameter.
- `{self.nama}` menampilkan nama karyawan yang tersimpan dalam Object.

2. Pengertian Arguments

Arguments merupakan nilai atau data yang diberikan ketika sebuah Method dipanggil untuk mengisi Parameter yang telah didefinisikan.

Contoh coding:

`karyawan1.hello("Arthur")`

Penjelasan:
- `karyawan1` merupakan Object yang memanggil Method.
- `hello()` merupakan Method yang dijalankan.
- `"Arthur"` merupakan Argument yang diberikan kepada Parameter `nama`.

Hasil output:

`Halo Arthur, nama saya Harley`

Pada hasil tersebut, program menampilkan nama Arthur sebagai orang yang disapa dan Harley sebagai karyawan yang memperkenalkan diri. Kesimpulan: Parameters digunakan untuk menerima data dalam Method, sedangkan Arguments merupakan nilai yang diberikan ketika Method dipanggil.

## 5. Kesimpulan Project

Berdasarkan Project Perkenalan Karyawan, dapat disimpulkan bahwa Class dan Object merupakan konsep dasar dalam pemrograman berorientasi objek (OOP). Class digunakan sebagai rancangan untuk membuat Object, sedangkan Object merupakan hasil pembentukan dari Class tersebut.

Attributes digunakan untuk menyimpan informasi karyawan, seperti nomor identitas, posisi pekerjaan, dan nama. Methods digunakan untuk menjalankan tindakan berupa proses perkenalan, sedangkan Parameters memungkinkan Method menerima informasi tambahan berupa nama orang yang ingin disapa.

Melalui project ini, konsep Class, Object, Attributes, Methods, dan Methods dengan Parameters dapat diterapkan secara sederhana menggunakan Python.
