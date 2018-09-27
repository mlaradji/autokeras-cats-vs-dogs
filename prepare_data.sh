#!/bin/bash

cd data
# unzip!
    unzip kaggle-dogs-vs-cats-all.zip -x sampleSubmission.csv
    unzip train.zip
    unzip test1.zip
    
    echo "Successfully extracted sub-zips."
    
    # Prepare directories.
    mv test1 test
    mv train preshuffle
    mkdir train
    mkdir val
    
    cd preshuffle
    
    # sanity check
    find . -type f -name 'cat*' | wc -l # 12500
    find . -type f -name 'dog*' | wc -l # 12500

    # Randomly move 90% into train and val, 
    # if reproducability is important you can pass in a source to shuf
    find . -type f | shuf -n11250 | xargs -I file mv file ../val
    find . -maxdepth 1 -type f | xargs -I file mv file ../train
    
    echo "Successfully completed find's."

    # requires gnu utils (brew install coreutils)
    # use gmv instead of mv on osx
    #echo cat*.jpg | xargs mv -t cat
    #echo dog*.jpg | xargs mv -t dog
    
cd ../..
# create labels csv file.
    python3 create_csv_labels.py --directory='data/train' --output-csv='data/train/labels.csv'
    python3 create_csv_labels.py --directory='data/val' --output-csv='data/val/labels.csv'
