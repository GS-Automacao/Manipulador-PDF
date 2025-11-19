from PyPDF2 import PdfReader
from tqdm import tqdm
import re
import os


def pegar_numeros(texto: str):
    return ''.join(re.findall(r'\d+', str(texto)))


def f27() -> int:
    files = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    n_arqs = len(files)
    for file in tqdm(files):
        with open(file, 'rb') as file_bin:
            pdf = PdfReader(file_bin)
            page = pdf.pages[0]
            text = page.extract_text().split()
            
            
            data_antiga = text[13].split('/')
            data_antiga = data_antiga[1:3]
            data_nova = ' ' .join(data_antiga)
                
                
                
            nome_antigo = text[81:85]
            nome_novo = " ".join(nome_antigo)
            n_nf = pegar_numeros(text[118])
            
        novo_nome = f'{data_nova} - {nome_novo} - {n_nf}.pdf'

        os.rename(file, novo_nome)
    
