from PyPDF2 import PdfReader
from tqdm import tqdm
import os


def f15() -> int:
    files = [file for file in os.listdir() if '.pdf' in file.lower()]
    n_pags = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            rows = page.extract_text().split('\n')
        for i, row in enumerate(rows):
            if 'Competência' in row:
                nome = row[:row.find('Competência')]
            elif row.startswith('Insc.Municipal'):
                cnpj = ''.join(char for char in rows[i+1] if char.isnumeric())
                break
        new_path = f'NF {nome}-{cnpj}.pdf'
        os.rename(file, new_path)

    return n_pags
