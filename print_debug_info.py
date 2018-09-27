#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:45:40 2018

@author: Mohamed Laradji
"""

import pkg_resources
import sys

print('Python' + ' - ' + sys.version.split('|',1)[0])

pkgs = ['autokeras', 'scikit-learn', 'numpy', 'keras', 'scipy', 'tensorflow', 'pytorch']

for pkg in pkgs:
    
    try:
        version = pkg_resources.get_distribution(pkg).version
        
    except pkg_resources.DistributionNotFound:
        version = 'None'
    
    print(pkg + ' - ' + version)
