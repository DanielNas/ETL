import sys
import os

# adicionar a raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from source.extract import extract_files
from source.transform import transform_customers

if __name__ == '__main__':
    print('Extraindo arquivos...')
    dataframes = extract_files.carregar_arquivos_csv()

    print('Transformando arquivos...')
    transform_customers.transformar_e_salvar(dataframes)

    print('Processo de extração e transformção concluido com sucesso!')