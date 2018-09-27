#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:46:35 2018

@author: Mohamed Laradji
"""

from autokeras.image_supervised import ImageClassifier, load_image_dataset


x_train, y_train = load_image_dataset(csv_file_path="data/train/labels.csv",
                                      images_path="data/train")

x_val, y_val = load_image_dataset(csv_file_path="data/val/labels.csv",
                                    images_path="data/val")

if __name__ == '__main__':

    clf = ImageClassifier(verbose=True)
    clf.fit(x_train, y_train, time_limit=12 * 60 * 60) # Currently results in errors.
    clf.final_fit(x_train, y_train, x_val, y_val, retrain=True)
    y = clf.evaluate(x_val, y_val)

