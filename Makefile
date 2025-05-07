# Makefile

.PHONY: all setup_env install_r install_python run_python run_r clean

# Usage: make [target] DIR=
DIR ?= .

all: setup_env install_r install_python run_python run_r

setup_env:
	@echo "NOTE: Make cannot persist environment activation across steps."
	@echo ""
	@echo "👉 Before running make, ensure environments are activated:"
	@echo "   - For Python: run 'source ./venv/bin/activate' (or equivalent)"
	@echo "   - For R: use 'renv::activate()' in R, or ensure packages are globally available"
	@echo ""

install_r:
	@echo "Installing R dependencies..."
	Rscript requirements.R

install_python:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt

run_python:
	@echo "Running Python pipeline for directory $(DIR)..."
	./run_all_py.sh $(DIR)

run_r:
	@echo "Running R pipeline for directory $(DIR)..."
	./run_all_r.sh $(DIR)

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
