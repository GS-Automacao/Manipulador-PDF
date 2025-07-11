from PyPDF2 import PdfReader
from tqdm import tqdm
import os


def f22() -> int:
    files = [file for file in os.listdir() if '.pdf' in file.lower()]
    n_pags = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            rows = page.extract_text().split('\n')
        # Variável indicadora, para capturar apenas o segundo logradouro.
        segundo_logradouro = False
        for row in rows:
            if row.startswith('Logradouro:'):
                if segundo_logradouro:
                    cnpj = ''.join(char for char in row[11:26] if char.isnumeric())
                    nome = ''.join(char for char in row[29:] if not char.isnumeric())
                    new_path = f'NF {nome}-{cnpj}.pdf'
                    os.rename(file, new_path)
                    break
                else:
                    segundo_logradouro = True
    return n_pags
