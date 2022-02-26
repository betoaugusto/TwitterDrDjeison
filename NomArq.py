"""
A biblioteca NomArq auxilia a gerar nomes de arquivos em determinada pasta.
"""
import os
import datetime

def RetArquivo(dir: str= '.', 
                    prefix_data:bool= True,
                    radical_arquivo:str= 'arq',
                    dig_serial: int= 5,
                    extensao: str= 'dat',
                    incArq: int= 0,
                    ) -> str:
    """
    Gerar nomes de arquivos, com prefixo de data e um sequencial.
    É possível definir uma extensão específica para os arquivos.

    incArq, quando zero retorna o último arquivo já existente.
    Se incArq > 0, o sequencial do último registro será incrementado.
    Exemplo:
        Arquivos:
            arq00001.dat
            arq00002.dat
            arq00003.dat
        Se incArq for ZERO ou não informado, irá retornar 'arq00003.dat'
        Se incArq for 1, irá retornar 'arq00004.dat'

        Se não existir arquivos na pasta:
            Se incArq for ZERO ou não informado o nome do arquivo não sera retornado vazio
            Se incArq for 1, irá retornar com o serquencial igual a incArq


        
    """
    maiorArq = 0
    for arq in os.listdir(dir):
        pos = arq.find(radical_arquivo)
        # Ignora arquivos fora do padrão
        if pos > 0 and arq.endswith('.'+extensao):
            # Definie posição inicial e final do serial do arquivo
            tamRadicalArquivo = len(radical_arquivo)
            posIni = pos + tamRadicalArquivo
            posFim = posIni + dig_serial
            seqArq = int(arq[posIni:posFim])
            # Pegar o maior sequencial, já incrementado em 1
            maiorArq = maiorArq if seqArq < maiorArq else seqArq + incArq
            #print(f'Arquivo: {arq}; Valor Procurado {radical_arquivo}; Nro: {seqArq}; maiorArq: {maiorArq}')

    # Se não achou nenhum arquivo joga o valor de incArq
    maiorArq = maiorArq if maiorArq > 0 else incArq

    # Define o prefixo de data, quando solicitado
    data = '' if not prefix_data else f'{datetime.datetime.now():%Y%m%d}_'

    if maiorArq > 0:
        # TODO: Não consegui usar a constante DIGITOS_SERIAL para zeros à esquerda
        # TODO:  Tive que deixar 5 fixos em {maiorArq:05}, que coloca os zeros
        nomeArquivo = f'{data}{radical_arquivo}{maiorArq:05}.{extensao}'
    else:
        nomeArquivo = ''

    return nomeArquivo