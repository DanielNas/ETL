# libs
import pandas as pd
import os
from source.utils.helpers import configurar_logger, DIR_RAW_DATA

# ===== CONFIGURAÇÕES =====

# Config arquivos logs
logger = configurar_logger('log_extracao.log')

# ===== EXECUÇÃO =====

# funcão para ler os arquivos CSV
def ler_csv(caminho_arquivos):
    try:
        df = pd.read_csv(caminho_arquivos, encoding='utf-8')
        logger.info(f'Arquivo {os.path.basename(caminho_arquivos)} carregado com sucesso.')
        return df
    except Exception as e:
        logger.error(f'Erro ao ler o arquivo {caminho_arquivos}: {e}')
        return None
    
# função para carregar todos os arquivos do diretorio RAW e armazenar em um dicionario
def carregar_arquivos():
    dataframes = {}

    # verificar se o diretorio está ok e existe
    if not os.path.exists(DIR_RAW_DATA):
        logger.error(f'Diretorio de dados não encotrado: {DIR_RAW_DATA}')
        return dataframes
    
    arquivos = os.listdir(DIR_RAW_DATA)

    # verificar se o diretorio contém os arquivos
    if not arquivos:
        logger.warning(f'Nenhum arquivo foi encontrado no diretorio: {DIR_RAW_DATA}')
        return dataframes
    
    # verificar se todos arquivos tem extensão CSV
    arquivos_csv = [arquivo for arquivo in arquivos if arquivo.endswith('csv')]

    # loga todos os arquivos encontrados
    logger.info(f'Arquivos CSV encontrados: {arquivos_csv}')

    for arquivo in arquivos_csv:
        caminho_arquivo = os.path.join(DIR_RAW_DATA, arquivo)
        if os.path.isfile(caminho_arquivo):
            df = ler_csv(caminho_arquivo)
            if df is not None:
                nome = os.path.splitext(arquivo)[0]
                dataframes[nome] = df
            else:
                logger.warning(f'Falha ao ler arquivo {arquivo}')
    
    logger.info('Processo de extração concluído!')

    return dataframes   
        