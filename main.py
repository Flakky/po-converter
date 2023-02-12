from argparse import ArgumentParser
import sys
import os

from converter import Converter
from csv2po import ConverterCSV2Po
from po2csv import ConverterPo2CSV

script_path = os.path.dirname(__file__)
if getattr(sys, 'frozen', False):   # if application is frozen exe, get path differently
    script_path = os.path.dirname(sys.executable)

print('Script path: ' + script_path)

parser = ArgumentParser()

parser.add_argument('-pc', '--potocsv',
                    dest='potocsv',
                    type=str,
                    help='Convert .po file to .csv')

parser.add_argument('-cp', '--csvtopo',
                    dest='csvtopo',
                    type=str,
                    help='Convert .csv file to .po')

args = parser.parse_args()

print(f'Po to CSV argument: {args.potocsv}')
print(f'CSV to PO argument: {args.csvtopo}')

if args.potocsv is not None:
    filepath = os.path.join(script_path, args.potocsv)
    ConverterPo2CSV.convert(filepath)

if args.csvtopo is not None:
    filepath = os.path.join(script_path, args.csvtopo)
    ConverterCSV2Po.convert(filepath)
