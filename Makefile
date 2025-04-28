.PHONY: extract tranform load etl docker-up docker-down logs

extract:
	@echo "Iniciando extração..."
	python source/extract/extract_files.python

tranform:
	@echo "Iniciando tranformação..."
	python source/tranform/tranform_customers.python