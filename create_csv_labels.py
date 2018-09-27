#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:52:40 2018

@author: Mohamed Laradji

Some code was obtained from:
    users 'anselm' and 'z0r' at
      https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
    users 'Andy Hayden' and 'Ninjakannon' at
      https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it#13786327
"""

import argparse
import os
import pandas as pd


# Parse commandline arguments.

parser = argparse.ArgumentParser(description='Auto-Keras Cats vs Dogs example.')

parser.add_argument('--directory', default='data/', type=str, metavar='N', help='The directory containing the images.')
parser.add_argument('--output-csv', default='data/labels.csv', type=str, metavar='N', help='Filename to which the csv with image labels should be saved.')

args = parser.parse_args()

# Iterate over files in train directory and check the prepended labels.

directory_in_str = args.directory

directory = os.fsencode(directory_in_str)

files = list()
label = dict()

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    label[filename] = filename.split('.',1)[0]

    files.append(filename)

# Create and save dataframe to a csv.

columns = [ 'Label' ]
data = {'Label': label}
df = pd.DataFrame(data, index=files, columns=columns)
df.to_csv(args.output_csv, index_label = 'File Name')