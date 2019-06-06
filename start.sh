#!/bin/bash

python3 gen_cert.py "$1" --out-dir $(pwd)/"$1"/certificados

if [ $? -eq 0 ];then
    cd $(pwd)/"$1"/certificados
    vet_tex=($(ls|grep .tex))
    for arquivo_tex in ${vet_tex[@]};do
        pdflatex $arquivo_tex
        echo "PDF criado em $(pwd)/$1/certificados/$arquivo_tex"
    done
fi