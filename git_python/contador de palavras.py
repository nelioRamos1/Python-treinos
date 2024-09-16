def contar_palavras(arquivo):
    with open (arquivo, 'r') as f:
        conteudo = f.read()
        palavras = conteudo.split ()
    return len(palavras)
    
arquivo = "texto.txt"
num_palavras = contar_palavras(arquivo)
print("numero de palavras no arquivo:", num_palavras)