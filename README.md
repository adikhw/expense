<div align="center">

# Expense Tracker

**Catat pemasukan dan pengeluaran langsung dari terminal.**
Tanpa install apa-apa, data aman tersimpan di file JSON.

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/storage-JSON-lightgrey)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
![Interface](https://img.shields.io/badge/interface-CLI-black)

[Fitur](#-fitur) · [Cara Menjalankan](#-cara-menjalankan) · [Cara Pakai](#-cara-pakai) · [Struktur Project](#-struktur-project) · [Catatan Penting](#-catatan-penting)

</div>

---

## 📖 Tentang Project

**Expense Tracker** adalah aplikasi terminal (CLI) untuk mencatat uang masuk dan uang keluar, melihat riwayat transaksi, dan melihat total pengeluaran per kategori beserta sisa saldo.

Project ini adalah **Project #1** dari rangkaian project belajar Python. Fokusnya: dasar Python yang kuat (input/output, list, dict, fungsi) dan menyimpan data ke file JSON. Sengaja dibuat sederhana: tanpa database, tanpa library eksternal, tanpa GUI.

## ✨ Fitur

| Fitur | Keterangan |
|---|---|
| ➕ **Tambah transaksi** | Catat tanggal, tipe (`income`/`expense`), jumlah, kategori, dan catatan |
| 📜 **Riwayat** | Semua transaksi, urut dari yang terbaru, kolom sejajar, angka pakai pemisah ribuan |
| 📊 **Ringkasan** | Total pemasukan, total pengeluaran, saldo, dan pengeluaran per kategori |
| 🗓️ **Filter bulan** | Ringkasan bisa dibatasi ke satu bulan (format `YYYY-MM`) |
| 🗑️ **Hapus transaksi** | Hapus berdasarkan ID, dengan konfirmasi `y/n` |
| 💾 **Data permanen** | Disimpan di `data/transactions.json`, tidak hilang saat program ditutup |
| 🛡️ **Tahan input salah** | Huruf di kolom angka, jumlah negatif, kategori kosong, sampai file JSON kosong/rusak tidak bikin program crash |

## 🚀 Cara Menjalankan

**Kebutuhan:** Python 3 saja. Modul yang dipakai semuanya bawaan (`json`, `datetime`, `pathlib`), jadi tidak ada yang perlu di-install.

```bash
# 1. Cek Python
python --version

# 2. Masuk ke folder project
cd expense

# 3. Jalankan
python main.py
```

> ⚠️ **Selalu jalankan dari dalam folder `expense/`.** Lokasi file data (`data/transactions.json`) dihitung relatif ke folder tempat program dijalankan. Kalau dijalankan dari folder lain, data bisa tersimpan di tempat yang salah.
>
> Di Windows, kalau `python` tidak dikenali, coba `py main.py`.

## 🎮 Cara Pakai

Setelah dijalankan, kamu akan masuk ke menu utama. Ketik angka pilihan lalu tekan Enter.

```
=========== EXPENSE TRACKER ============

1. Add transaction 
2. Show history 
3. Show summary 
4. Delete transaction 
5. Exit

Choose an option:
```

### 1. Tambah transaksi

Isi data satu per satu. **Tanggal boleh dikosongkan** (otomatis jadi hari ini) dan **catatan boleh dikosongkan**.

```
=========== ADD TRANSACTION ============

Date (YYYY-MM-DD, empty = today):
Type (income/expense): expense
Amount: 25000
Category: makan
Note (optional): makan siang

Transaction added
```

### 2. Lihat riwayat

Transaksi ditampilkan dari yang terbaru. Kalau tanggalnya sama, ID yang lebih besar ada di atas.

```
  ID  Date        Type            Amount  Category      Note
-----------------------------------------------------------------
   3  2026-10-10  expense         25,000  makan         makan siang
   2  2026-10-07  income       5,000,000  gaji          gaji bulanan
   1  2026-10-05  expense         15,000  transport     ojek
```

### 3. Lihat ringkasan

Kosongkan input bulan untuk melihat semua data, atau isi dengan format `YYYY-MM` (contoh: `2026-10`).

```
SUMMARY
----------------------------
Total income  :    5,000,000
Total expense :       40,000
Balance       :    4,960,000
----------------------------

Expense per category:
makan               25,000
transport           15,000
```

> Yang dihitung per kategori hanya **pengeluaran** (`expense`).

### 4. Hapus transaksi

Masukkan ID, lihat detail transaksinya, lalu konfirmasi dengan `y` atau `n`. ID yang tidak ada atau bukan angka akan ditolak dengan pesan yang jelas.

### 5. Keluar

Menutup program. Data sudah tersimpan sejak setiap transaksi ditambah atau dihapus. Menekan `Ctrl+C` juga aman: program pamit dengan rapi, bukan crash.

## 🧾 Aturan Input

Semua validasi dilakukan di `tracker.py`, jadi aturannya sama di mana pun fungsi dipanggil.

| Field | Aturan |
|---|---|
| `date` | Format `YYYY-MM-DD`, harus tanggal yang benar (`2026-02-30` ditolak). Kosong = hari ini |
| `type` | Hanya `income` atau `expense` (huruf besar/kecil dan spasi di pinggir tidak masalah) |
| `amount` | Bilangan bulat positif (rupiah). Desimal, nol, negatif, dan huruf ditolak |
| `category` | Tidak boleh kosong, otomatis diubah ke huruf kecil |
| `note` | Teks bebas, boleh kosong |
| `month` (filter) | Format ketat `YYYY-MM` (`2026-1` ditolak) |

## 🗂️ Bentuk Data

Data disimpan sebagai list di `data/transactions.json`:

```json
[
  {
    "id": 1,
    "date": "2026-10-07",
    "type": "expense",
    "amount": 25000,
    "category": "makan",
    "note": "makan siang"
  }
]
```

`id` dihitung dari **id terbesar + 1**.

## 🏗️ Struktur Project

```
expense/
├── main.py            # titik masuk program + penanganan Ctrl+C
├── cli.py             # menu dan input/output terminal
├── tracker.py         # logika: validasi, tambah, hapus, hitung total
├── storage.py         # baca/tulis file JSON
├── data/
│   └── transactions.json
└── README.md
```

Tiap file punya **satu tanggung jawab**, dan arah panggilannya satu arah:

```
main.py  ──▶  cli.py  ──▶  tracker.py  ──▶  storage.py  ──▶  transactions.json
(mulai)      (tampilan)     (logika)         (file)             (data)
```

| File | Boleh | Tidak boleh |
|---|---|---|
| `cli.py` | `input()`, `print()` | Baca/tulis file, hitung total sendiri |
| `tracker.py` | Logika dan validasi | `input()`, `print()` |
| `storage.py` | Baca/tulis JSON | `print()`, logika bisnis |

## ⚠️ Catatan Penting

- **`save_data` menimpa isi file.** Kalau `transactions.json` rusak, program menganggapnya kosong. Kalau setelah itu kamu menambah transaksi baru, isi lama yang rusak akan hilang. Backup dulu kalau ada data penting.
- **ID bisa dipakai ulang.** Kalau transaksi dengan ID terbesar dihapus, ID itu akan dipakai lagi oleh transaksi berikutnya. Ini keputusan desain yang disengaja, karena aplikasi ini untuk satu pengguna dan tidak ada yang mereferensikan ID dari luar.
- **Data tes.** Kalau kamu menyimpan project ini di Git, pertimbangkan memasukkan `data/` ke `.gitignore` supaya data pribadi tidak ikut ter-commit.

## 🔭 Ide Pengembangan

Di luar scope project ini, dicatat untuk nanti:

- Backup otomatis file JSON yang rusak sebelum ditimpa
- Penghitung ID terpisah (misal `data/meta.json`) supaya ID tidak pernah dipakai ulang

## 🎓 Yang Dipelajari dari Project Ini

- Input/output terminal (`input()`, `print()`, f-string formatting)
- Struktur data: list dan dict
- Fungsi: parameter dan return value
- Baca/tulis JSON (`json`) dan path file (`pathlib`)
- Tanggal dengan `datetime`
- Error handling (`try`/`except`, `ValueError`, `KeyboardInterrupt`)
- Memecah kode jadi beberapa file dengan tanggung jawab terpisah

---

<div align="center">

Dibuat sebagai latihan belajar Python. 🐍

</div>