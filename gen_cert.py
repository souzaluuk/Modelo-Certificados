#!/usr/bin/env python3
# encoding: utf-8

""" A script to generate certificates for CACo - Centro Acadêmico da Computação
da Unicamp """

import argparse
import csv
import os
import sys

# Create argument parser
parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument('--base-dir', default='base',
                    help='directory for base files')
parser.add_argument('--pre', default='preamble.tex',
                    help='preamble file (relative to BASE_DIR)')
parser.add_argument('--head', default='header.tex',
                    help='header file (relative to BASE_DIR)')
parser.add_argument('--sig', default='signature.tex',
                    help='signature file (relative to BASE_DIR)')

parser.add_argument('course', help='Name of the course')
parser.add_argument('--course-dir', default=None,
                    help='directory where course data is stored (defaults to' +
                    ' course)')
parser.add_argument('--content', default='content.tex',
                    help='content of certificate (relative to COURSE_DIR)')
parser.add_argument('--list', default='class.csv',
                    help='course participants file (relative to COURSE_DIR)')

parser.add_argument('--out-dir', default='certificates',
                    help='directory where the tex files will be saved')

parser.add_argument('-q', '--quiet', action='store_const', const=True,
                    default=False, help='quiet output')

args = parser.parse_args()

# Base of the certificate
base_dir = args.base_dir
pre_fn = args.pre
head_fn = args.head
sig_fn = args.sig

# Course info
course = args.course
if not args.course_dir:  # input dir defaults to course name
    in_dir = course
cont_fn = args.content
list_fn = args.list

# Where individual .tex will be saved (relative to input dir)
out_dir = args.out_dir
full_out_dir = os.path.join(in_dir, out_dir)

quiet = args.quiet

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

    if not quiet:
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

