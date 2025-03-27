# libs
import logging
import pandas as pd
import os

# definição do diretorio de logs 
log_dir = os.path.join(os.getcwd(), 'logs')

# caminho completo do log de extração 
log_file = os.path.join(log_dir, 'log_extracao_olist_files_1.log')

# config do logger
logging.basicConfig(
    filename=log_file, # caminho do arquivo log
    level=logging.INFO, # nível do log
    format='%(asctime)s - %(levelname)s - %(message)s', # formato do log
    datefmt='%d-%m-%Y %H:%M:%S' # formato da data
)

# caminho arquivos 
caminho = r'C:\Users\Daniel\OneDrive\Ambiente de Trabalho\Projetos ETL\Olist brazil\ETL\data'

# log: inicio do processo
logging.info(f'Início leitura dos arquivos do diretorio: {caminho}')

try: 
    # listar arquivos no diretorio
    arquivos = os.listdir(caminho)
    logging.info("Arquivos no diretorio:", {arquivos})
    
    # verificar tipos de arquivos do diretorio
    formatos = set([arquivos.split('.')[1] for arquivos in arquivos if '.' in arquivos])
    logging("Extensões no diretorio:", {str(formatos)})

except Exception as e:
    logging.error(f'Ocorreu um erro: {str(e)}')

# log: fim do processo
logging.info('Processo finalizado')