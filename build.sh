#!/bin/sh

set -xe

nasm -f macho64 hello.asm
ld -lSystem -o hello hello.o
