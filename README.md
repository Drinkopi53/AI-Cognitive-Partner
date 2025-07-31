# AI Cognitive Partner (MVP)

![Cognitive Partner](https://img.shields.io/badge/AI%20Cognitive%20Partner-MVP-blue)
![Language](https://img.shields.io/badge/Language-Python-orange)
![Status](https://img.shields.io/badge/Status-Complete-green)

## Deskripsi

**AI Cognitive Partner** adalah sebuah program kecerdasan buatan (AI) yang dirancang untuk menjadi mitra berpikir pribadi Anda. Berbeda dari asisten biasa, program ini bertujuan untuk meningkatkan kemampuan kognitif Anda dengan cara yang unik:

*   **Berdebat untuk Mempertajam Ide:** Anda dapat terlibat dalam sesi debat konstruktif dengan AI untuk menguji, menantang, dan memperdalam pemahaman Anda tentang suatu topik.
*   **Mengidentifikasi Bias Kognitif:** Selama berdebat, AI akan memberikan umpan balik *real-time* jika mendeteksi adanya bias kognitif umum (seperti Pemikiran Hitam-Putih atau Bias Konfirmasi) dalam argumen Anda.
*   **Membangun Model Mental:** Setelah sesi debat, AI akan memberikan ringkasan untuk membantu Anda memvisualisasikan bagaimana ide-ide Anda berkembang.

Versi ini adalah Produk Minimum yang Layak (MVP) yang dibangun sebagai aplikasi baris perintah (*command-line*) untuk memvalidasi konsep inti dari proyek ini.

## Fitur Utama (MVP)

*   **Pelatihan AI Personal:** Latih AI dengan memasukkan ide, argumen, dan gaya berpikir Anda. Semakin banyak Anda berlatih, semakin personal respons AI.
*   **Mode Debat Interaktif:** Mulai sesi debat kapan saja untuk mengeksplorasi suatu topik. AI akan menggunakan data pelatihan Anda untuk memberikan perspektif yang relevan.
*   **Deteksi Bias Kognitif:** Dapatkan umpan balik instan tentang bias kognitif yang mungkin memengaruhi argumen Anda, lengkap dengan penjelasan singkat.
*   **Ringkasan Debat:** Terima ringkasan terstruktur di akhir setiap sesi untuk membantu Anda merefleksikan alur diskusi.

## Instalasi

Proyek ini dibuat dengan Python 3 dan tidak memerlukan dependensi eksternal di luar pustaka standar.

1.  **Pastikan Anda memiliki Python 3 terinstal.** Anda dapat memeriksanya dengan menjalankan:
    ```bash
    python --version
    # atau
    python3 --version
    ```

2.  **Unduh atau kloning repositori ini.**
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```
    Atau, cukup unduh file `cognitive_partner.py`.

## Cara Menggunakan

Untuk menjalankan aplikasi, navigasikan ke direktori tempat file `cognitive_partner.py` berada dan jalankan perintah berikut di terminal Anda:

```bash
python cognitive_partner.py
```

Anda akan disambut dengan menu utama:

```
--- AI Cognitive Partner (MVP) ---
1. Latih AI dengan ide-ide Anda
2. Mulai sesi debat dengan AI
3. Keluar
Pilih opsi (1-3):
```

### Opsi 1: Latih AI

*   Pilih opsi `1` untuk masuk ke mode pelatihan.
*   Masukkan teks, ide, atau argumen Anda.
*   Ketik `SELESAI` pada baris baru dan tekan Enter untuk menyimpan teks dan kembali ke menu utama.
*   Data pelatihan Anda akan disimpan dalam file `user_data.json`.

### Opsi 2: Mulai Debat

*   Pilih opsi `2` untuk memulai sesi debat.
*   Ketik argumen Anda dan tekan Enter. AI akan merespons.
*   Jika AI mendeteksi potensi bias kognitif, ia akan memberikan umpan balik sebelum memberikan responsnya.
*   Untuk mengakhiri sesi, ketik `AKHIRI DEBAT` dan tekan Enter.
*   Setelah sesi berakhir, sebuah ringkasan akan ditampilkan.

### Opsi 3: Keluar

*   Pilih opsi `3` untuk keluar dari aplikasi.

## Kontribusi

Saat ini, proyek ini masih dalam tahap awal. Namun, jika Anda tertarik untuk berkontribusi di masa depan, harap perhatikan pedoman berikut:

*   **Laporkan Bug:** Jika Anda menemukan bug, silakan buka *issue* dengan deskripsi yang jelas dan langkah-langkah untuk mereproduksinya.
*   **Permintaan Fitur:** Punya ide untuk fitur baru? Buka *issue* untuk mendiskusikannya.
*   **Pull Request:** *Pull request* dipersilakan. Pastikan kode Anda bersih, terdokumentasi dengan baik, dan mengikuti gaya kode yang ada.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.