import argparse
import platform
import os
import ctypes
import subprocess
import sys

def run_as_admin(command):
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            subprocess.run(command, shell=True)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", command, None, 1)
    except Exception as e:
        print(f"Gagal menjalankan sebagai administrator: {e}")

def get_hosts_path():
    system_platform = platform.system()
    if system_platform == "Linux" or system_platform == "Darwin":
        return '/etc/hosts'
    else:
        print("Sistem operasi tidak didukung.")
        return None

def baca_file_hosts():
    try:
        with open(get_hosts_path(), 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("File hosts tidak ditemukan.")
        return []

def tulis_file_hosts(lines):
    try:
        with open(get_hosts_path(), 'w') as file:
            file.writelines(lines)
        print("File hosts berhasil diperbarui.")
    except Exception as e:
        print(f"Gagal menulis ke file hosts: {e}")

def susun_ulang_entri(lines):
    # Pisahkan komentar dan entri
    komentar = [line for line in lines if line.startswith('#')]
    entri = [line for line in lines if not line.startswith('#')]

    # Urutkan entri-entri
    entri.sort()

    # Gabungkan kembali komentar dan entri
    hasil = komentar + entri

    return hasil

def tambahkan_host(entry, ip_address):
    lines = baca_file_hosts()

    try:
        # Tambahkan entri baru
        with open(get_hosts_path(), 'a') as file:
            file.write(f"\n{ip_address} {entry}\n")
        print(f"Host {entry} dengan IP {ip_address} berhasil ditambahkan ke file hosts.")
    except Exception as e:
        print(f"Gagal menambahkan host: {e}")

def hapus_host(entry):
    lines = baca_file_hosts()

    try:
        # Hapus entri berdasarkan nama host
        lines = [line for line in lines if entry not in line.split()]

        tulis_file_hosts(lines)

        print(f"Host dengan nama {entry} berhasil dihapus.")
    except Exception as e:
        print(f"Gagal menghapus host: {e}")

def tampilkan_list_hosts():
    lines = baca_file_hosts()

    try:
        print("List Hosts:")
        print("".join(lines))
    except Exception as e:
        print(f"Gagal menampilkan list hosts: {e}")

def main():
    if sys.platform not in ['linux', 'darwin']:
        print("Skrip ini hanya dapat dijalankan di lingkungan Linux dan macOS.")
        sys.exit()

    parser = argparse.ArgumentParser(description="Skrip untuk menambahkan, menghapus, atau menampilkan entri host ke/dari file hosts.")
    parser.add_argument("-ip", "--ip-address", help="Alamat IP host yang ingin ditambahkan atau dihapus.")
    parser.add_argument("-hn", "--hostname", help="Nama host yang ingin ditambahkan atau dihapus.")
    parser.add_argument("-l", "--list", help="Menampilkan list host.", action="store_true")
    parser.add_argument("-d", "--delete", help="Menghapus host berdasarkan nama.", action="store_true")

    args = parser.parse_args()

    if args.delete:
        if args.hostname:
            hapus_host(args.hostname)
        else:
            print("Argumen -hn/--hostname diperlukan untuk menghapus host.")
    elif args.ip_address and args.hostname:
        run_as_admin(f"\"{os.path.abspath(__file__)}\" -ip {args.ip_address} -hn {args.hostname}")
    elif args.list:
        tampilkan_list_hosts()
    else:
        print("Silakan berikan argumen yang benar. Gunakan -h untuk bantuan.")

if __name__ == "__main__":
    main()
