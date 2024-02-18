# PDF Cutter.py

Script Python untuk membagi file PDF menjadi beberapa file berdasarkan jumlah halaman yang ditentukan dan untuk mengkompresi ukuran file pdf sehingga mudah ketika ingin menerjemahkanya di Google Translate.

## Penggunaan PDF Cutter.py

1. Pastikan Python 3.x telah terinstal.

2. Unduh / salin Script dari repositori ini.

3. Buka terminal atau command prompt di direktori tempat Anda menyimpan script.

4. Jalankan skrip dengan perintah berikut:

    ```bash
    python PDF Cutter.py
    ```

6. Ikuti petunjuk yang muncul di terminal untuk memotong & mengkompres file PDF sesuai kebutuhan.

## Catatan

- Pastikan Anda telah menginstal dependensi yang diperlukan, seperti PyPDF2, sebelum menjalankan script ini. Anda dapat menginstalnya dengan menjalankan `pip install PyPDF2` di terminal.

- Tempatkan Script dan File PDF di dalam satu folder yang sama.

# add_hosts.py

Script Python untuk menambahkan, menghapus, atau menampilkan daftar host di file /etc/hosts pada lingkungan Linux dan macOS.

## Persyaratan

- Python 3.x

## Penggunaan add_hosts.py

1. Pastikan Python 3.x telah terinstal di sistem Anda.

2. Buka terminal di lingkungan Linux atau macOS.

3. Unduh skrip dengan menjalankan perintah berikut:

    ```bash
    https://github.com/alvinhayy/MageR-Scripts.git
    ```
    
4. Pindah ke direktori skrip:

    ```bash
    cd MageR-Scripts
    ```

5. Jalankan skrip dengan argumen yang sesuai. Contoh penggunaan:

    - Menampilkan list hosts:
        ```bash
        python add_hosts.py -l
        ```

    - Menambahkan host baru:
        ```bash
        python add_hosts.py -ip 192.168.1.1 -hn example.com
        ```

    - Menghapus host berdasarkan nama:
        ```bash
        python add_hosts.py -d -hn example.com
        ```

6. Perlu diketahui bahwasanya perlu hak akses Root untuk menjalankan scripts ini.

## Catatan

- Skrip ini hanya dapat dijalankan di lingkungan Linux dan macOS. Jika Anda menggunakan Windows, pastikan Anda memiliki emulator terminal yang mendukung lingkungan Linux.

- Jika skrip tidak berjalan dengan benar, pastikan bahwa Anda menjalankannya di terminal yang memiliki izin administratif dan memiliki hak akses ke file hosts.

## Lisensi

Skrip ini dilisensikan di bawah [MIT License](LICENSE).
