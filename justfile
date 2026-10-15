# Recipes
@default:
    just --list

@hugo-serve:
    hugo serve

@index-serve:
    sleep 0.5
    watchexec -d 500ms -w public -i pagefind -- pagefind --site public

@build:
    hugo --minify
    pagefind --site public

[parallel]
start: hugo-serve index-serve
