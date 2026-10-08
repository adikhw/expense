# Expense Tracker (CLI)

Aplikasi terminal untuk mencatat pemasukan dan pengeluaran. Data disimpan di file JSON, jadi tidak hilang saat program ditutup.

> **Status: sedang dikerjakan (README sementara).**
> Ini Project #1 dari daftar latihan Python. Roadmap lengkap ada di [`EXPENSE.md`](EXPENSE.md), daftar project ada di [`Projects.md`](Projects.md).

## Fitur (target)

- Tambah transaksi (tanggal, tipe, jumlah, kategori, catatan)
- Lihat riwayat transaksi (terbaru di atas)
- Lihat total per kategori dan saldo akhir
- Hapus transaksi (dengan konfirmasi)
- Input salah dan file JSON kosong/rusak tidak bikin program crash

## Tech

- Python 3
- Hanya modul bawaan: `json`, `datetime`, `pathlib`
- Tidak perlu install apa-apa

## Cara Jalankan

```bash
python main.py
```

## Struktur Folder

```
expense/
├── main.py          # titik masuk program
├── cli.py           # menu dan input/output terminal
├── storage.py       # baca/tulis file JSON
├── tracker.py       # logika (tambah, hapus, hitung total)
├── data/
│   └── transactions.json
└── README.md
```

## Bentuk Data

Disimpan di `data/transactions.json` sebagai list:

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

| Field | Keterangan |
|---|---|
| `id` | Angka unik, naik terus (tidak dipakai ulang) |
| `date` | Format `YYYY-MM-DD` |
| `type` | `income` atau `expense` |
| `amount` | Bilangan bulat positif (rupiah) |
| `category` | Teks huruf kecil, misal `makan`, `transport`, `gaji` |
| `note` | Teks bebas, boleh kosong |

## Progres

Cek centang di [`EXPENSE.md`](EXPENSE.md) untuk status terbaru tiap phase.

## Di Luar Scope

GUI/web/API, database, grafik, budget, multi-mata-uang, login, dan `pytest` sengaja tidak dikerjakan di project ini.

## TODO

- [ ] Ganti README ini dengan versi final (apa ini, cara pakai, contoh tampilan) di Phase 8