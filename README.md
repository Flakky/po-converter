# po-converter
.po file converter into .csv and vise versa.

## Usage 

### PO to CSV
To convert .po to .csv. If path is provided, it will convert all .po files inside (not recursively)
```shell
python main.py -pc relative/path/to/file.po

python main.py --potocsv relative/path/to/file.po

python main.py -pc relative/path/with/po/files
```

### CSV to PO
To convert .csv to .po. If path is provided, it will convert all .csv files inside (not recursively)
```shell
python main.py -cp relative/path/to/file.csv

python main.py --csvtopo relative/path/to/file.csv

python main.py -cp relative/path/with/po/files
```
