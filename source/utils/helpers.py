import os
from dotenv import load_dotenv
import logging

# carrega as variaveis do .env
load_dotenv()

# variáveis de ambiente
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DIR_RAW_DATA = os.getenv('DIR_RAW_DATA')
DIR_PROCESSED_DATA = os.getenv('DIR_PROCESSED_DATA')
DIR_LOGS = os.getenv('DIR_LOGS')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

def configurar_logger(nome_arquivo_log):
    if not os.path.exists(DIR_LOGS):
        os.mkdirs(DIR_LOGS)

    log_path = os.path.join(DIR_LOGS, nome_arquivo_log)

    logging.basicConfig(
        filename=log_path,
        level=getattr(logging, LOG_LEVEL),
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )

    return logging.getLogger()


