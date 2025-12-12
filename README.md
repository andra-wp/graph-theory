# Penjelasan Program dan Formatting GitHub

Dokumen ini menjelaskan alur kerja, cara penggunaan, serta mekanisme formatting otomatis pada GitHub untuk dua program Python yang terdapat pada repository ini, yaitu **Knight’s Tour** dan **Largest Increasing Subsequence (LIS)**. Seluruh dokumentasi ditulis menggunakan Markdown agar dapat dirender otomatis oleh GitHub.

---

## 1. Program Knight’s Tour

### Deskripsi
Program Knight’s Tour bertujuan mencari lintasan bidak kuda pada papan catur berukuran 8×8 sehingga setiap petak dikunjungi tepat satu kali. Algoritma yang digunakan adalah heuristik Warnsdorff, yaitu memilih langkah dengan jumlah kemungkinan langkah lanjutan paling sedikit. Program juga mengklasifikasikan lintasan sebagai open tour atau closed tour.

### Alur Kerja
1. Papan catur diinisialisasi sebagai matriks 8×8 dengan nilai awal `-1`.
2. Posisi awal knight ditentukan berdasarkan input pengguna.
3. Pada setiap langkah, seluruh kemungkinan langkah knight yang valid dievaluasi.
4. Langkah dengan jumlah onward moves paling sedikit dipilih.
5. Proses diulang hingga seluruh petak dikunjungi atau tidak tersedia langkah valid.
6. Jenis tour ditentukan dan lintasan divisualisasikan menggunakan Matplotlib.

### Cara Menjalankan
```bash
python knight.py
```

### Input

Pengguna memasukkan:

- Baris awal knight (0–7)
- Kolom awal knight (0–7)

### Output

Jika lintasan berhasil ditemukan, program menampilkan:

- Status keberhasilan
- Jenis tour (OPEN atau CLOSED)
- Matriks papan berisi urutan langkah knight
- Visualisasi lintasan knight

Jika lintasan tidak ditemukan:

```
Tour gagal ditemukan dari posisi ini. Coba posisi start lain.

```

---

## 2. Program Largest Increasing Subsequence (LIS)

### Deskripsi

Program Largest Increasing Subsequence (LIS) digunakan untuk mencari subsequence naik terpanjang dari sebuah array bilangan. Subsequence tidak harus berurutan secara kontigu, tetapi harus mempertahankan urutan indeks dan bersifat meningkat. Pendekatan yang digunakan adalah dynamic programming.

### Alur Kerja

1. Array `dp` digunakan untuk menyimpan panjang LIS yang berakhir pada setiap indeks.
2. Array `prev` digunakan untuk menyimpan indeks elemen sebelumnya dalam subsequence.
3. Setiap elemen dibandingkan dengan seluruh elemen sebelumnya.
4. Panjang LIS maksimum ditentukan dari array `dp`.
5. Subsequence direkonstruksi menggunakan array `prev`.

### Cara Menjalankan
```bash
python LMIS.py
```

### Input

Array bilangan didefinisikan langsung di dalam kode:

```python
arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]

```

### Output

```
Panjang LIS: 4
LIS: [1, 2, 8, 11]

```

### Kompleksitas

- Kompleksitas waktu: O(n²)
- Kompleksitas ruang: O(n)
