import os
import pandas as pd
from source.utils.helpers import configurar_logger, DIR_PROCESSED_DATA

# === CONFIGURAÇÕES ===
logger = configurar_logger('log_transform_olist.log')

# === EXECUÇÃO ===

# função para normalizar nomes das colunas
def tratar_colunas(df):
    """
    deixa os nomes das colunas no padrão pré definido para o load no banco
    """
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

# tratar a tabela de clientes
def tratar_tab_clientes(df):
    logger.info('Transformando tabela: clientes')
    df = tratar_colunas(df)
    return df

# tratar a tabela de produtos
def tratar_tab_produtos(df):
    logger.info('Transformando tabela: produtos')
    df = tratar_colunas(df)
    return df

# tratar tabela de pedidos
def tratar_tab_pedidos(df):
    logger.info('Transformando tabela: pedidos')
    df = tratar_colunas(df)
    # identificar e tratar colunas de data
    colunas_data = [col for col in df.columns if 'timestamp' in col or 'date' in col]
    for col in colunas_data:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

# tratar tabela de itens pedido
def tratar_tab_itens_pedidos(df):
    logger.info('Transformando tabela: itens pedidos')
    df = tratar_colunas(df)

    # converter o preço e valor do frete para float
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['freight_value'] = pd.to_numeric(df['freight_value'], errors='coerce')
    return df

# tratar tabela de pagamentos 
def tratar_tab_pagamentos(df):
    logger.info('Transfomando tabela: pagamentos')
    df = tratar_colunas(df)
    # converter valor para float
    df['payment_value'] = pd.to_numeric(df['payment_value'], errors='coerce')
    return df

# tratar tabela reviews
def tratar_tab_reviews(df):
    logger.info('Transformando tabela: reviews')
    df = tratar_colunas(df)
    # converter colunas de date para datetime
    colunas_data = [col for col in df.columns if 'date' in col]
    for col in colunas_data:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

# tratar tabela de fornecedores
def tratar_tab_fornecedores(df):
    logger.info('Transformando tabela: fornecedores')
    df = tratar_colunas(df)
    return df

# tratar tabela de categorias de produtos
def tratar_tab_categorias_produtos(df):
    logger.info('Transformando tabela: categorias de produtos')
    df = tratar_colunas(df)
    return df

# funçao que orquestra todas as transformações
def transformar(dataframes):
    """ 
    Recebe um dic dos dfs extraidos,
    aplica as transformações específicas por tabela
    e salva as alterações no diretorio data\processed 
    """

    if not os.path.exists(DIR_PROCESSED_DATA):
        os.makedirs(DIR_PROCESSED_DATA)

    for nome, df in dataframes.items():
        logger.info(f'Iniciando transformacao para: {nome}')
        if 'customers' in nome:
            df = tratar_tab_clientes(df)
        elif 'products' in nome:
            df = tratar_tab_produtos(df)
        elif 'orders' in nome:
            df = tratar_tab_pedidos(df)
        elif 'order_items' in nome:
            df = tratar_tab_itens_pedidos(df)
        elif 'order_payments' in nome:
            df = tratar_tab_pagamentos(df)
        elif 'order_reviews' in nome:
            df = tratar_tab_reviews(df)
        elif 'sellers' in nome:
            df = tratar_tab_fornecedores(df)
        elif 'product_category_name_translation' in nome:
            df = tratar_tab_categorias_produtos(df)
        else:
            # caso tenha não tenha regra específica, padroniza as colunas
            df = tratar_colunas(df)
    
        # salva os arquivos transformados no diretorio para comparação de alterações posteriormente
        output_path = os.path.join(DIR_PROCESSED_DATA, f'{nome}_clean.csv')
        df.to_csv(output_path, index=False)
        logger.info(f'Tabela transformada e salva em {output_path}')

    logger.info('Transformacoes concluidas para todas as tabelas!')