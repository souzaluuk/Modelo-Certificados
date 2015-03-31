Modelo de certificados
======================

Modelo de certificados utilizado nos cursos do CACo - Centro Acadêmico da
Computação da Unicamp.

O modelo consiste de um script em Python capaz de gerar os certificados
individuais a partir de uma lista de alunos e de alguns arquivos base.

Arquivos base
-------------

Os arquivos base podem ser encontrados e modificados no diretório base do
repositório, eles definem o estilo do certificato e o nome dos membros
responsáveis por assinar o certificado

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
`year`, todos como Strings.

Caso necessário incluir o caractere '%', use '%%', atente-se que este
caractere, caso não seja escapado em LaTeX, será considerado como início de
comentário.

### class.csv

Este arquivo deve conter os dados necessários para preencher o texto no
`content.tex`. A primeira linha deve conter o nome de cada campo, como escrito
no texto do certificado.

As linhas seguintes devem conter as informações dos participantes, separadas
por vírgulas.
