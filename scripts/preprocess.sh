#!/bin/bash


rm -f ./data/*.zip
rm -f ./data/*.json
rm -f ./data/*.csv

wget --no-check-certificate 'https://drive.usercontent.google.com/download?id=1WFWDt7c2A5jsZ1NmPjsqKo2id3WVVtMq&export=download&authuser=0&confirm=t' -O ./data/archive.zip

unzip -o ./data/archive.zip -d ./data

rm -f ./output/*.csv
rm -f ./output/*.json
rm -f ./output/*.log

python ./scripts/clean_data.py
