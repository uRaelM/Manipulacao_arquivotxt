def abrir(caminho):
    arquivo = open(caminho, 'r', encoding='utf-8')
    return arquivo


def numero_palavras(caminho):
    global palavras
    palavras = []
    palavra = []
    letras = []
    for linha in abrir(caminho):
        palavra = linha.split(' ')
        for p in palavra:
            palavras.append(p)
    contador =  0
    for word in palavras:
        contador += 1
    print(f'numero de palavras: {contador}')


def vogais():
    a = []
    e = []
    i = []
    o = []
    u = []
    for p in palavras:
        for letra in p:
            if letra == 'a':
                a.append(letra)
            elif letra == 'e':
                e.append(letra)
            elif letra == 'i':
                i.append(letra)
            elif letra == 'o':
                o.append(letra)
            elif letra == 'u':
                u.append(letra)
    tamanho = [len(a), len(e), len(i), len(o), len(u)]
    maior = max(tamanho)
    if maior == len(a):
        print(f'vogal que mais aparece é a letra A, ela aparece {maior} vezes')
    elif maior == len(e):
        print(f'vogal que mais aparece é a letra E, ela aparece {maior} vezes')
    elif maior == len(i):
        print(f'vogal que mais aparece é a letra I, ela aparece {maior} vezes')
    elif maior == len(o):
        print(f'vogal que mais aparece é a letra O, ela aparece {maior} vezes')
    elif maior == len(u):
        print(f'vogal que mais aparece é a letra U, ela aparece {maior} vezes')


def cao(caminho):
    linha = 0
    for line in abrir(caminho):
        palavra = line.split(' ')
        linha += 1
        for p in palavra:
            if 'ção' in p:
                print(f'primeira aparição de ÇÃO na linha {linha}')
        


def maiores():
    tuplas = []
    tamanhos = []
    maiores = []
    for p in palavras:
        tuplas.append((p, len(p)))
    tuplas.sort(key = lambda x: x[1], reverse=True)
    print(tuplas[0], tuplas[1], tuplas[2],  tuplas[3], tuplas[4])
    

global palavras
entrada = input()
numero_palavras(entrada)
maiores()
vogais()
cao(entrada)
