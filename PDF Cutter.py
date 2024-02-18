import os
from PyPDF2 import PdfReader, PdfWriter
import sys

def get_num_pages(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        return len(pdf_reader.pages)

def split_pdf(input_pdf, output_folder, pages_per_file):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        num_files = num_pages // pages_per_file
        if num_pages % pages_per_file:
            num_files += 1

        for i in range(num_files):
            start_page = i * pages_per_file
            end_page = min((i + 1) * pages_per_file, num_pages)

            pdf_writer = PdfWriter()
            for page_num in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            output_pdf = os.path.join(output_folder, f'output_{i+1}.pdf')
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

def compress_pdf(input_pdf, output_pdf):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

def list_pdf_files():
    pdf_files = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    for idx, file in enumerate(pdf_files, start=1):
        print(f"[{idx}] {file}")
    return pdf_files

def main():
    print("PDF Cutter")
    pdf_files = list_pdf_files()
    choice = input("Masukan Nomor file yang akan di cut: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(pdf_files):
            print("Nomor file tidak valid.")
            sys.exit(1)
    except ValueError:
        print("Input harus berupa nomor.")
        sys.exit(1)

    input_pdf = pdf_files[choice - 1]

    num_pages = get_num_pages(input_pdf)
    print(f"Jumlah halaman pada file pdf: {num_pages}")

    split_option = input("Apakah ingin membagi halaman file (yes/no): ").lower()
    if split_option == "yes":
        num_files = int(input("Bagi menjadi berapa file: "))
        pages_per_file = int(input("Berapa halaman per file: "))
        output_folder = input_pdf.split('.')[0] + "_output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        split_pdf(input_pdf, output_folder, pages_per_file)
        print(f"File PDF telah dibagi menjadi {num_files} file dengan {pages_per_file} halaman per file.")

    compress_option = input("Apakah ingin mengkompres size file output (yes/no): ").lower()
    if compress_option == "yes":
        output_folder = input_pdf.split('.')[0] + "_output"
        for filename in os.listdir(output_folder):
            output_pdf = os.path.join(output_folder, filename)
            compressed_pdf = output_pdf.replace('.pdf', '_compressed.pdf')
            compress_pdf(output_pdf, compressed_pdf)
            os.remove(output_pdf)
            print(f"{filename} telah dikompres menjadi {compressed_pdf}")

    print("Selesai.")

if __name__ == "__main__":
    main()
