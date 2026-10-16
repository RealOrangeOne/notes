# Recipes
@default:
    just --list

@hugo-serve:
    hugo serve

@index-serve:
    watchexec --delay-run 1s -d 1s -- pagefind --site public

@build:
    hugo --minify
    pagefind --site public

[parallel]
start: hugo-serve index-serve
