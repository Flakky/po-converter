import sys
import os

from converter import Converter
from csv2po import ConverterCSV2Po
from po2csv import ConverterPo2CSV

script_path = os.path.dirname(__file__)
if getattr(sys, 'frozen', False):   # if application is frozen exe, get path differently
    script_path = os.path.dirname(sys.executable)

print('Script path: ' + script_path)


def convert():

    filepath = os.path.join(script_path, sys.argv[1])

    file_name, file_extension = os.path.splitext(filepath)

    extension_converter_classes = {
        ".po": ConverterPo2CSV,
        ".csv": ConverterCSV2Po
    }

    converter_class: Converter = extension_converter_classes[f"{file_extension}"]
    if converter_class is None:
        print(f"Error: Converter class was not found for '{file_extension}' file extension!")
        return False

    return converter_class.convert(filepath)


convert()
