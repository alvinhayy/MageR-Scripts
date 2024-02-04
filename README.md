# add_hosts.py

Skrip Python untuk menambahkan, menghapus, atau menampilkan entri host di file hosts pada lingkungan Linux dan macOS.

## Persyaratan

- Python 3.x

## Penggunaan

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
