export PATH := "./env/bin:" + env_var('PATH')

# Recipes
@default:
    just --list

setup:
    python -m venv env
    env/bin/pip install -r requirements.txt

@start:
    mkdocs serve

@build:
    mkdocs build -v
