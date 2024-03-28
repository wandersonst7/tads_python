import os
import re
from os import path

# Para utilizar é necessário que o script esteja dentro
# do diretório do arquivo o qual se quer renomear

def remover_espacos(string):
    return re.sub(r'\s+', " ", string.strip())

def main():
    
    # Defina aqui as palavras que você quer remover
    listaDePalavrasParaRemover = ["1080p", "720p", "WWW", "COM"]
    
    while True:
        
        nomeArquivo = input("Nome do arquivo: ")
        formato = input("Formato (ex: mp4, mp3, txt): ")
        nomeComFormato = nomeArquivo + "." + formato
    
        if path.exists(nomeComFormato):
            
            # Removendo sinais
            pattern = r'[-_.]'
            nomeArquivo = re.sub(pattern, " ", nomeArquivo)
            
            # Removendo palavras indesejadas
            for palavra in listaDePalavrasParaRemover:
                nomeArquivo = re.sub(palavra, "", nomeArquivo)
                
            # Removendo multiplos espaços em branco
            nomeArquivo = remover_espacos(nomeArquivo)
            
            # Novo nome do arquivo
            novoNomeDoArquivo = nomeArquivo + "." + formato

            os.rename(nomeComFormato, novoNomeDoArquivo) 
            print("Arquivo renomeado com sucesso!")
        else:
            print("Arquivo não encontrado!")
            
        continuar = input("Deseja continuar? [s/n]")
        
        if continuar == "s":
            continue
        else:
            break
        
main()