#!/usr/bin/env python3
# encoding: utf-8

""" A script to generate certificates for CACo - Centro Acadêmico da Computação
da Unicamp """

import csv
import os
import sys

# Base of the certificate
base_dir = 'base'
pre_fn = 'preamble.tex'
head_fn = 'header.tex'
sig_fn = 'signature.tex'

# Course info (input dir will be course name by default)
in_dir = 'Curso de Git'
course = in_dir
cont_fn = 'content.tex'
list_fn = 'class.csv'

# Where individual .tex will be saved (relative to input dir)
out_dir = 'cert'
full_out_dir = os.path.join(in_dir, out_dir)

verbose = True

# Check output directory
if os.path.isdir(full_out_dir):
    if os.listdir(full_out_dir):
        print('error: directory ' + out_dir + ' exists and is non-empty',
              file=sys.stderr)
        exit(1)
    else:
        print('warning: directory ' + out_dir + ' exists but is empty')
else:
    os.mkdir(full_out_dir)

# Open relevant files
try:
    pre_f = open(os.path.join(base_dir, pre_fn), 'r')
    head_f = open(os.path.join(base_dir, head_fn), 'r')
    sig_f = open(os.path.join(base_dir, sig_fn), 'r')
    cont_f = open(os.path.join(in_dir, cont_fn), 'r')
    list_f = open(os.path.join(in_dir, list_fn), 'r')
except:
    print('error: problem opening input files', file=sys.stderr)
    exit(1)

# Read class data
data = csv.DictReader(list_f, delimiter=',')

# Read base files
pre = pre_f.read()
head = head_f.read()
sig = sig_f.read()
cont = cont_f.read()

# Generate individual tex files
for d in data:
    name = d['name']
    cur_f = open(os.path.join(full_out_dir, name + '.tex'), 'w')

    if verbose:
        print('Building ' + name + '.tex')

    # Build certificate text
    cur_text = pre + '\n'
    cur_text = cur_text + ('\\newcommand{\\course}{%s}' % course) + '\n'
    cur_text = cur_text + head + '\n'
    try:
        cur_text = cur_text + (cont % d) + '\n'
    except:
        print('error: missing information on ' + d, file=sys.stderr)
        exit(1)
    cur_text = cur_text + sig + '\n'

    # Write file
    cur_f.write(cur_text)

