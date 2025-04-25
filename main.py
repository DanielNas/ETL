import sys
import os

# adicionar a raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from source.utils.helpers import configurar_logger
from source.extract.extract_files_olist import extract_files_olist
from source.transform.transform_olist import transformar

# criar um logger para registrar o andamento dos processos
logger = configurar_logger('log_main_etl_olist.log')

# === EXECUÇAO ===

def main():
    logger.info('Iniciando pipeline ETL Olist')

    # === EXTRACT ===
    logger.info('Iniciando etapa de extracao')
    dataframes = extract_files_olist()
    logger.info('Extracao concluida com sucesso')
    print('Extracao concluida com sucesso!')

    # === TRANSFORM ===
    logger.info('Iniciando etapa de transformacoes')
    transformar(dataframes)
    logger.info('Transformacao concluida com sucesso')
    print('Transformacao concluida com sucesso!')

     # === LOAD ===

    
    logger.info('Pipeline ETL finalizado com sucesso')
    print('Pipeline ETL finalizado com sucesso')

if __name__ == '__main__':
   main()
    