import logging
import os
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
root = file.parents[1]
sys.path.append(str(root))

# import das tabelas originais
from extract.extract_files import df_clientes, df_produtos

# Definindo o diretório de logs para a transformação
log_dir = os.path.join(os.getcwd(), 'logs_2')

# Arquivo de log para transformação
log_file_transform = os.path.join(log_dir, 'log_transform_olist_files.log')

# Configuração do Logger para Transformação
logging.basicConfig(
    filename=log_file_transform,  # Caminho do arquivo de log para transformação
    level=logging.INFO,  # Nível do log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato do log
    datefmt='%d-%m-%Y %H:%M:%S'  # Formato da data
)

# ==== TABELA DE CLIENTES =====

logging.info('Iniciando a transformacao da tabela de clientes')

# log do shape da tabela
df_shape = df_clientes
logging.info(f'Dataframe original carregado - Shape: {df_shape}')
print(f'Dataframe original carregado - Shape: {df_shape}')

# analise inicial
def analisar_tabela(df):
    """ Exibe as informações básicas do DataFrame"""
    logging.info(f'Colunas: {list(df.columns)}')
    logging.info(f'Valores nulos:\n{df.isnull().sum()}')

# chamar analise inicial
analisar_tabela(df_clientes)

# ==== LIMPEZA E TRANSFORMAÇÕES ====

# verficar linhas duplicadas

# normalizar nomes das colunas

# log final

# salvar tabela para fase de Load no banco

# ==== TABELA DE PRODUTOS =====

logging.info('Iniciando a transformacao da tabela de clientes')

# log do shape da tabela
df_shape = df_produtos
logging.info(f'Dataframe original carregado - Shape: {df_shape}')
print(f'Dataframe original carregado - Shape: {df_shape}')

# analise inicial
def analisar_tabela(df):
    """ Exibe as informações básicas do DataFrame"""
    logging.info(f'Colunas: {list(df.columns)}')
    logging.info(f'Valores nulos:\n{df.isnull().sum()}')

# chamar analise inicial
analisar_tabela(df_produtos)