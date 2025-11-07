from PyPDF2 import PdfReader
import re


def teste():
    arquivos = ...
    
    if not arquivos:
        print("Nenhum arquivo encontrado na pasta.")
        return
    
    # Pega o primeiro arquivo encontrado
    caminho_arquivo = "Contracheques RPL102025.pdf"

    # Abre o PDF
    with open(caminho_arquivo, "rb") as file_bin:
        pdf = PdfReader(file_bin)
        page0 = pdf.pages[0]
        text = page0.extract_text().split("\n")
        for i in enumerate(text):
            print(i)

teste()
