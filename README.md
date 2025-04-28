# ETL Olist Brazil



# 📦 ETL - Extração de Arquivos CSV

Este módulo realiza a extração de arquivos CSV de um diretório específico, carregando-os em dataframes Pandas e registrando logs de todo o processo.

## 📄 Descrição

O script `extract_files.py` percorre o diretório de dados configurado, identifica os arquivos CSV disponíveis, carrega cada arquivo em um dataframe e armazena todos os dataframes em um dicionário Python.

Os logs de execução são gravados em arquivos `.log`, armazenando informações de início e fim do processo, além de mensagens de sucesso, warnings e erros.

## 🚀 Tecnologias utilizadas

- Python 3.12
- Pandas
- Logging

## 📂 Estrutura de Diretórios


