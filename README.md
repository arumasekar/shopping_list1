Nama: Wahyu Aji Aruma Sekar Puri
NPM: 2206816115
Kelas: B

1. Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Link: https://main.adaptable.app

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Membuat direktori baru yang akan dikonfigurasi dengan proyek django
b. Membuat virtual environment lalu diaktifkan
c. Membuat proyek django baru dengan perintah 'django-admin startproject <namaprojek>'
d. Membuat aplikasi bernama 'main' dengan perintah 'python manage.py startapp main'
e. Melakukan routing project dengan membuka berkas 'urls.py' dan menambahkan rute ke aplikasi 'main'
f. Membuat model bernama 'item' dengan membuka berkas 'models.py' pada aplikasi 'main' dan membuat model 'item' dengan minimal atribut name,amount,description
g. Membuat fungsi pada berkas 'views.py' yg mengembalikan data ke template HTML sehingga dapat menampilkan nama aplikasi, nama serta kelas
h. Melakukan routing aplikasi 'main' dengan membuka file 'urls.py' pada aplikasi main dan memetakan fungsi ke views.py
i. Melakukan deployment ke adaptable dan perlu mengunggah project Django ke server Adaptable sehingga dapat diakses ke internet
j. Membuat file README.md yang berisi link aplikasi yg dideploy pada adaptable serta menjawab pertanyaan-pertanyaan dari checklist

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Gambar Bagan Request Client Wahyu Aji Aruma](BaganRequest_WahyuAjiAruma.png) 

4. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jika kita menggunakan virtual environment, semua library akan diinstal secara default di direktori global tempat semua project akan mencari dependensi. Misalnya kita memulai proyek A. Kita memerlukan beberapa library seperti Django dan menginstall Django 2.2. Kemudian kita memulai proyek B. Lalu beberapa waktu kita menginstall Django versi 3.0. Apakah terdapat potensi masalah jika membuat aplikasi tanpa virtual environment? Hal tersebut bisa saja terjadi, karena proyek A tidak diperbarui ke Django. Permasalahannya adalah kita memiliki satu direktori tempat kita mengistall semua library, serta semua project kita akan mencari direktori tersebut untuk library yang kita butuhkan. Jika lita memperbarui salah satu perpustakaan tersebut, hal ini akan memengaruhi semua proyek kita yang memerlukan perpustakaan tersebut.


5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
a. MVC (Model View Controller)
merupakan pola desain perangkat lunak yang digunakan untuk mengimplementasikan antarmuka pengguna dan memberikan penekanan pada pemisahan representasi data dari komponen dalam memproses data.
b. MVT (Model View Template)
merupakan pola desain yang mirip dengan MVC. Implementasi yang dilakukan juga untuk antarmuka wes dan aplikasi, tetapi perbedaannya adalah pada bagian pengontrol ditangani oleh kerangka kerja itu sendiri.
c. MVVM (The Model — View — ViewModel)
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