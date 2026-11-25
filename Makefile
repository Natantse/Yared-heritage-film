.PHONY: install validate

install:
	pip install -r requirements.txt

validate:
	python pipeline.py
