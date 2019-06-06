Modelo de certificados
======================

Modelo de certificados utilizado nos cursos do CACo - Centro Acadêmico da
Computação da Unicamp e adaptado para utilização no CCSL - Centro de Competência em Software Livre da UFPA.

O modelo consiste de um script em Python capaz de gerar os certificados
individuais a partir de uma lista de alunos e de alguns arquivos base, e foi estendido para
gerar os pdf  dos certificados de forma automatizada utilizando Shell Script.

Arquivos base
-------------

Os arquivos base podem ser encontrados e modificados no diretório base do
repositório, eles definem o estilo do certificato e o nome dos membros
responsáveis por assinar o certificado e as imagens utilizadas no certificado.

Arquivos específicos do curso
-----------------------------

Os arquivos específicos do curso devem ser fornecidos para cada curso. Os
arquivos são: `content.tex` e `class.csv`.

### content.tex

Neste arquivo fica o texto do certificado, este texto pode conter comandos em
LaTeX e marcações que serão preenchidas com os dados dos participantes. As
marcações são similares às do `printf` de C, porém são nomeadas. Por exemplo:

    Certificamos que %(name)s participou do curso %(course)s no dia %(day)s/%(month)s/%(year)s

Neste caso, os dados necessários serão `name`, `course`, `day`, `month` e
`year`, todos como Strings, porém estes são opcionais, podendo trabalhar apenas com `nome`.

Caso necessário incluir o caractere '%', use '%%', atente-se que este
caractere, caso não seja escapado em LaTeX, será considerado como início de
comentário.

### class.csv

Este arquivo deve conter os dados necessários para preencher o texto no
`content.tex`. A primeira linha deve conter o nome de cada campo, como escrito
no texto do certificado.

As linhas seguintes devem conter as informações dos participantes, separadas
por vírgulas.

Gerando os Certificados
-------------------------

### [start.sh](start.sh)

Originalmente a execução é feita através do arquivo [`gen_cert.py`](gen_cert.py), no entanto este apenas gera os arquivos `.tex`, assim foi criado o script [`start.sh`](start.sh) para que os PDFs fossem gerados na sequência. Seu modo de execução é:

```bash
[dir_repo] $ ./start.sh ['Nome do Curso']
```

O nome do curso deve ser igual ao diretório em que hospeda os dados que serão utilizados, ou seja, como no exemplo do 'Curso de Tese' teríamos `[dir_repo] $ ./start.sh Curso de Tese`.

Os PDFs são criados em `[dir_repo]/['Nome do Curso']/certificados`