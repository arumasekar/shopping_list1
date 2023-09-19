- Nama: Wahyu Aji Aruma Sekar Puri
- NPM: 2206816115
- Kelas: B
- Kode Asdos: EDA


- TUGAS 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
Berikut adalah perbedaan dari form POST dan form GET:
# GET:
- Tombol kembali/muat ulang: Tidak berbahaya
- Bookmarked dapat ditandai
- Dapat di-chace
- Jenis pengkodean application/x-www-form-urlencoded
- Riwayat tetap ada dalam browser
- Batasan panjang data: Ya, saat mengirim data, metode GET menambahkan data ke URL; dan panjang URL dibatasi (panjang URL maksimum adalah 2048 karakter)
- Batasan tipe data hanya karakter ASCII yang diperbolehkan
- Keamanan: GET kurang aman dibandingkan POST karena data yang dikirim merupakan bagian dari URL
- Visibilitas: Data dapat dilihat oleh semua orang di URL
# POST:
- Tombol kembali/muat ulang: Data akan dikirim ulang (browser harus mengingatkan pengguna bahwa data akan dikirim ulang)
- Tidak dapat di-bookmark
- Tidak di-cache
- Jenis pengkodean application/x-www-form-urlencoded atau multipart/form-data. Menggunakan pengkodean multibagian untuk data biner
- Parameter tidak disimpan dalam riwayat browser
- Batasan panjang data: Tidak ada batasan
- Tidak ada batasan tipe data. Data biner juga diperbolehkan
- POST sedikit lebih aman daripada GET karena parameternya tidak disimpan dalam riwayat browser atau log server web
- Data tidak ditampilkan di URL

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
# JSON:
JSON adalah format file yang menggunakan teks dan dapat dibaca oleh manusia untuk menyimpan dan mengirimkan objek data berisi pasangan dan array nilai atribut. JSON digunakan untuk menyimpan informasi secara terorganisir dan mudah diakses.
- Notasi Objek JavaScript
- Berdasarkan bahasa JavaScript
- Cara merepresentasikan objek
- Tidak memberikan dukungan apa pun untuk namespace
- Mendukung array
- File-filenya sangat mudah dibaca dibandingkan dengan XML
- Tidak menggunakan tag akhir
- Kurang aman
- Tidak mendukung komentar
- Hanya mendukung pengkodean UTF-8
# XML:
XML adalah bahasa markup yang dapat diperluas yang dirancang untuk menyimpan data. XML memungkinkan Anda menentukan elemen markup dan menghasilkan bahasa markup yang disesuaikan. Elemen adalah unit dasar dalam bahasa XML.
- Bahasa markup yang dapat diperluas
- Berasal dari SGML
- Bahasa markup dan menggunakan struktur tag untuk mewakili item data
- Mendukung namespace
- Tidak mendukung array
- Dokumen relatif sulit untuk dibaca dan diinterpretasikan
- Memiliki tag awal dan akhir
- Lebih aman daripada JSON
- Mendukung komentar
- Mendukung berbagai pengkodean
# HTML:
HTML (Hyper Text Markup Language) digunakan untuk membuat halaman web dan aplikasi web. HTML digunakan untuk menampilkan data, bukan untuk mengangkut data. Bahasa markup digunakan untuk mendefinisikan dokumen teks dalam tag yang mendefinisikan struktur halaman web. Bahasa ini digunakan untuk membuat anotasi (membuat catatan untuk komputer) teks sehingga mesin dapat memahaminya dan memanipulasi teks yang sesuai.
- HTML adalah singkatan dari Hyper Text Markup Language
- HTML bersifat statis
- Ini dikembangkan oleh WHATWG
- Disebut sebagai bahasa presentasi
- HTML adalah bahasa markup
- HTML dapat mengabaikan kesalahan kecil
- Ini memiliki ekstensi .html dan .htm
- HTML tidak sensitif terhadap huruf besar-kecil
- Tag HTML adalah tag yang telah ditentukan sebelumnya
- Jumlah tag dalam HTML terbatas
- HTML tidak mempertahankan spasi putih
- HTML tidak membawa data, ia hanya menampilkannya

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Fleksibilitas dan kesederhanaan JSON menjadikannya bagian penting dari berbagai aplikasi dan layanan. API Web: JSON adalah format masuk untuk pertukaran data antara server web dan klien, memungkinkan interaksi yang lancar antara berbagai aplikasi web. JSON bersifat agnostik bahasa, artinya dapat digunakan dengan bahasa pemrograman apa pun, sehingga kompatibel secara universal.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Untuk mengatur routing:
Arah utama/ke/rute telah diubah untuk lebih cocok dengan konvensi proyek Django yang ada. Hal ini dilakukan dengan mengubah jalur di file urls.py.
- Membuat template dasar:
Buat templat dasar (base.html) yang akan digunakan sebagai kerangka umum untuk halaman web proyek lainnya. Template ini berisi elemen dasar seperti tag HTML, <head> dan <body> yang  digunakan di semua situs web.
- Buat formulir input data:
Buat formulir sederhana untuk memasukkan informasi barang ke dalam aplikasi. Formulir ini menggunakan formulir Django  (ProductForm) untuk memvalidasi dan menyimpan informasi produk baru.
- Menampilkan Data Produk pada HTML:
Buat formulir sederhana untuk memasukkan informasi barang ke dalam aplikasi. Formulir ini menggunakan formulir Django untuk memvalidasi dan menyimpan informasi produk baru.
- Mengembalikan data dalam format XML dan JSON:
Buat dua tampilan yang dapat mengembalikan informasi produk dalam format XML dan JSON. Ini digunakan untuk mengekspor data dari aplikasi.
- Mengembalikan Data Berdasarkan ID: 
Membuat view yang dapat mengembalikan data produk berdasarkan ID yang ditentukan. Dua versi tampilan dibuat, satu untuk XML dan satu lagi untuk JSON.
- Penggunaan Postman Sebagai Data Viewer: 
Menggunakan Postman sebagai alat untuk menguji endpoint-endpoint yang telah dibuat dalam proyek. Tukang pos digunakan untuk mengirim permintaan GET ke URL yang sesuai dan menerima respons dalam bentuk XML atau JSON.

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman






- TUGAS 2
1. Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Link: https://main.adaptable.app

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat direktori baru yang akan dikonfigurasi dengan proyek django
- Membuat virtual environment lalu diaktifkan
- Membuat proyek django baru dengan perintah 'django-admin startproject <namaprojek>'
- Membuat aplikasi bernama 'main' dengan perintah 'python manage.py startapp main'
- Melakukan routing project dengan membuka berkas 'urls.py' dan menambahkan rute ke aplikasi 'main'
- Membuat model bernama 'item' dengan membuka berkas 'models.py' pada aplikasi 'main' dan membuat model 'item' dengan minimal atribut name,amount,description
- Membuat fungsi pada berkas 'views.py' yg mengembalikan data ke template HTML sehingga dapat menampilkan nama aplikasi, nama serta kelas
- Melakukan routing aplikasi 'main' dengan membuka file 'urls.py' pada aplikasi main dan memetakan fungsi ke views.py
- Melakukan deployment ke adaptable dan perlu mengunggah project Django ke server Adaptable sehingga dapat diakses ke internet
- Membuat file README.md yang berisi link aplikasi yg dideploy pada adaptable serta menjawab pertanyaan-pertanyaan dari checklist

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Gambar Bagan Request Client Wahyu Aji Aruma](BaganRequest_WahyuAjiAruma.png) 

4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jika kita menggunakan virtual environment, semua library akan diinstal secara default di direktori global tempat semua project akan mencari dependensi. Misalnya kita memulai proyek A. Kita memerlukan beberapa library seperti Django dan menginstall Django 2.2. Kemudian kita memulai proyek B. Lalu beberapa waktu kita menginstall Django versi 3.0. Apakah terdapat potensi masalah jika membuat aplikasi tanpa virtual environment? Hal tersebut bisa saja terjadi, karena proyek A tidak diperbarui ke Django. Permasalahannya adalah kita memiliki satu direktori tempat kita mengistall semua library, serta semua project kita akan mencari direktori tersebut untuk library yang kita butuhkan. Jika lita memperbarui salah satu perpustakaan tersebut, hal ini akan memengaruhi semua proyek kita yang memerlukan perpustakaan tersebut.


5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC (Model View Controller)
merupakan pola desain perangkat lunak yang digunakan untuk mengimplementasikan antarmuka pengguna dan memberikan penekanan pada pemisahan representasi data dari komponen dalam memproses data.
- MVT (Model View Template)
merupakan pola desain yang mirip dengan MVC. Implementasi yang dilakukan juga untuk antarmuka wes dan aplikasi, tetapi perbedaannya adalah pada bagian pengontrol ditangani oleh kerangka kerja itu sendiri.
- MVVM (The Model — View — ViewModel)
merupakan arsitektur yang memfasilitasi pemisahan pengembangan antarmuka pengguna grafis dengan bantuan bahasa atau kode GUI. Selain itu, MVVM jua bertanggung jawab untuk mengekspos objek data dari model sedemikian rupa sehingga objek lebih mudah dikelola.
Perbedaan dari MVC, MVT, dan MVVM adalah:
# MVC:
- UI(View) dan mekanisme akses data(Model) berkaitan erat
- Controller dan View ada dengan hubungan satu-ke-banyak. Satu Controller dapat memilih View berbeda berdasarkan operasi yang diperlukan.
- Sulit untuk membuat perubahan dan memodifikasi fitur aplikasi karena lapisan kode saling terkait erat.
# MVT:
- MVT memiliki Tampilan untuk menerima permintaan HTTP dan mengembalikan respons HTTP.
- Bagian Controller dikelola oleh kerangka itu sendiri.
- Loosely coupled
# MVVM:
- Pola arsitektur ini lebih didorong oleh peristiwa karena menggunakan pengikatan data sehingga memudahkan pemisahan logika bisnis inti dari View.
- Beberapa Tampilan dapat dipetakan dengan satu ViewModel dan dengan demikian, hubungan satu-ke-banyak terjadi antara View dan ViewModel.
- Mudah untuk melakukan perubahan pada aplikasi. Namun, jika logika pengikatan data terlalu rumit, debug aplikasi akan sedikit lebih sulit.
