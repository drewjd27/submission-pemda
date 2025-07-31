# Proyek ETL Data Produk Fashion

Proyek ini adalah sebuah pipeline ETL (Extract, Transform, Load) yang dirancang untuk mengumpulkan data produk dari situs web e-commerce fashion, membersihkan dan mentransformasikannya, lalu menyimpannya ke dalam berbagai format data, termasuk CSV, database PostgreSQL, dan Google Sheets.

## Fitur Utama

- **Ekstraksi Data**: Mengambil data produk secara otomatis dari beberapa halaman situs web.
- **Transformasi Data**: Membersihkan data mentah, mengonversi tipe data (misalnya, harga dan rating), menghapus duplikat, dan memperkaya data dengan informasi tambahan seperti timestamp.
- **Pemuatan Data**: Menyimpan data yang telah ditransformasi ke dalam tiga tujuan berbeda:
    1.  Berkas CSV untuk analisis data sederhana.
    2.  Tabel pada database PostgreSQL untuk penyimpanan yang terstruktur dan skalabel.
    3.  Google Sheets untuk kolaborasi dan visualisasi yang mudah.

## Struktur Proyek

```
.
├── utils/
│   ├── extract.py      # Modul untuk mengambil data dari sumber
│   ├── transform.py    # Modul untuk membersihkan dan mentransformasi data
│   └── load.py         # Modul untuk menyimpan data ke tujuan
├── tests/
│   ├── test_extract.py   # Unit test untuk modul ekstraksi
│   ├── test_transform.py # Unit test untuk modul transformasi
│   └── test_load.py      # Unit test untuk modul pemuatan
├── .env.example        # Contoh berkas untuk variabel lingkungan
├── .gitignore          # Berkas yang diabaikan oleh Git
├── google-sheets-api.json # Kredensial API Google (tidak di-commit)
├── main.py             # Skrip utama untuk menjalankan pipeline ETL
├── requirements.txt    # Daftar dependensi Python
└── README.md           # Dokumentasi proyek
```

## Panduan Instalasi dan Konfigurasi

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

### 1. Kloning Repositori

```bash
git clone <URL_REPOSITORI_ANDA>
cd <NAMA_DIREKTORI_PROYEK>
```

### 2. Buat dan Aktifkan Lingkungan Virtual

Sangat disarankan untuk menggunakan lingkungan virtual (virtual environment) untuk mengisolasi dependensi proyek.

```bash
# Membuat lingkungan virtual
python -m venv venv

# Mengaktifkan di Windows
venv\Scripts\activate

# Mengaktifkan di macOS/Linux
source venv/bin/activate
```

### 3. Instal Dependensi

Instal semua pustaka Python yang dibutuhkan yang tercantum dalam `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Variabel Lingkungan

Proyek ini memerlukan beberapa variabel lingkungan untuk koneksi ke database.

1.  Buat salinan dari `.env.example` dan beri nama `.env`.
2.  Isi berkas `.env` dengan kredensial database PostgreSQL Anda:

    ```env
    DB_USER=nama_user_anda
    DB_PASSWORD=kata_sandi_rahasia_anda
    DB_NAME=nama_database_anda
    ```

### 5. Konfigurasi Google Sheets API

Untuk menyimpan data ke Google Sheets, Anda memerlukan kredensial API.

1.  Ikuti panduan resmi Google untuk membuat akun layanan (service account) dan membuat kunci JSON. [Panduan Google Cloud](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
2.  Pastikan Anda mengaktifkan **Google Sheets API** dan **Google Drive API** di proyek Google Cloud Anda.
3.  Bagikan (share) Google Sheet Anda dengan alamat email akun layanan (`client_email` yang ada di dalam berkas JSON).
4.  Simpan berkas kredensial JSON yang telah Anda unduh di direktori utama proyek dengan nama `google-sheets-api.json`. Berkas ini sudah otomatis diabaikan oleh Git melalui `.gitignore`.

## Cara Menjalankan Proyek

### Menjalankan Pipeline ETL

Untuk menjalankan keseluruhan proses ETL dari awal hingga akhir, jalankan skrip `main.py`.

```bash
python main.py
```

Skrip ini akan melakukan proses ekstraksi, transformasi, dan memuat data ke CSV, PostgreSQL, dan Google Sheets secara berurutan.

### Menjalankan Unit Test

Untuk memastikan semua fungsi berjalan sesuai harapan, Anda dapat menjalankan unit test yang telah disediakan.

```bash
python -m pytest tests/
```

### Mengecek Cakupan Kode (Test Coverage)

Untuk melihat seberapa banyak kode Anda yang dicakup oleh unit test, jalankan perintah berikut:

```bash
# Menjalankan coverage
coverage run -m pytest tests/

# Menampilkan laporan di terminal
coverage report

# Membuat laporan dalam format HTML
coverage html
```

Untuk melihat laporan HTML, buka berkas `htmlcov/index.html` di browser Anda.
