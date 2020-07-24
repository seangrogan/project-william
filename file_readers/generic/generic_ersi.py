import logging

import shapefile
from tqdm import tqdm
from utilities.get_filename_from_path import get_filename


def generic_esri_reader(shape_file, encoding='ISO-8859-1'):
    """Reads and parses the shape file into a more usable format"""
    print(f'Reading Shapefile : {get_filename(shape_file)}')
    logging.info(f'Reading Shapefile : {shape_file}')
    file = []
    with shapefile.Reader(shape_file, encoding=encoding) as sf:
        shapes, fields, records = sf.shapes(), sf.fields, sf.records()
        heading = [h.lower() for h in list(zip(*fields)).pop(0)[1:]]  # Note 1
        for record, shape in zip(tqdm(records, desc=f"Processing Shape File : {get_filename(shape_file)}"), shapes):
            item = dict(zip(heading, list(record)))
            item['shape'] = shape
            file.append(item)
    return file

# Note 1 :
# this takes the field names and just pushes out the header. [1:] is included because I don't care about the deletion
# flag field. I'm also making sure that everything is lower case
