# Recipes
@default:
    just --list

@start:
    hugo serve

@build:
    hugo --minify
