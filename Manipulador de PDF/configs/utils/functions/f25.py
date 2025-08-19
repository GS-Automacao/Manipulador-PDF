from PyPDF2 import PdfReader
from tqdm import tqdm
import os


def f25() -> int:
    files = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    n_arqs = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            rows = pdf.pages[0].extract_text().split('\n')
        for row in rows:
            if 'Data de Emissão' in row:
                num_nf = row.split()[0]
                break
        for row in rows[::-1]:
            if 'Nome/Razão Social' in row:
                nome_cliente = row[18:]
                nome_cliente = nome_cliente.translate(str.maketrans({'/': '', '\\': '', '|': ''}))
                break
        novo_nome = f'{nome_cliente}-{num_nf}.pdf'

        os.rename(file, novo_nome)
