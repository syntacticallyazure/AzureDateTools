alias b := build

default:
    just --list;

build:
    uv run pyinstaller today.spec --noconfirm
    uv run pyinstaller tomorrow.spec --noconfirm
    uv run pyinstaller yesterday.spec --noconfirm
