import logging
from collections import namedtuple
import csv

from utilities.to_numeric import to_numeric


def generic_csv_reader(csv_file, encoding='ISO-8859-1'):
    """Reads and parses the csv file into a more usable format"""
    print(f'Reading file {csv_file}')
    logging.debug(f'Reading file: {csv_file}')
    TempShape = namedtuple("Shape", ("bbox", "parts", "points", "shapeType", "shapeTypeName"))
    file = []
    with open(csv_file, encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for entry in reader:
            entry = {k.lower(): to_numeric(v) for k, v in entry.items()}
            if 'x' in entry:
                entry["shape"] = TempShape([entry['x'], entry['y'], entry['x'], entry['y']],
                                           [],
                                           [(entry['x'], entry['y'])],
                                           1,
                                           "POINT")
                entry['coordinate'] = \
                    entry['location'] = \
                    entry['point'] = \
                    (entry['x'], entry['y'])
            elif 'lon' in entry:
                entry["shape"] = TempShape([entry['lon'], entry['lat'], entry['lon'], entry['lat']],
                                           [],
                                           [(entry['lon'], entry['lat'])],
                                           1,
                                           "POINT")
                entry['coordinate'] = \
                    entry['location'] = \
                    entry['point'] = \
                    (entry['lon'], entry['lat'])
            file.append(entry)
        return file
