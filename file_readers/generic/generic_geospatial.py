import os

from file_readers.generic.generic_csv import generic_csv_reader
from file_readers.generic.generic_ersi import generic_esri_reader


def generic_geospatial(file, encoding='ISO-8859-1'):
    if __is_shp(file):
        return generic_esri_reader(file, encoding)
    elif __is_csv(file):
        return generic_csv_reader(file, encoding)
    else:
        raise TypeError(f"File {file} is not in the shapefile form or the csv form")


def generic_geospatial_files(file_iterable, encoding='ISO-8859-1'):
    if isinstance(file_iterable, set) or isinstance(file_iterable, list):
        files = []
        for file in file_iterable:
            files.append(generic_geospatial(file, encoding))
        if len(files) == 1:
            return files[0]
        return files
    return generic_geospatial(file_iterable)


def _shp_or_csv(file):
    if __is_shp(file):
        return 'shp'
    if __is_csv(file):
        return 'csv'
    return None


def __is_csv(file):
    csv_exts = {"csv"}
    root, ext = os.path.splitext(file)
    return ext.replace('.', '') in csv_exts


def __is_shp(file):
    shp_exts = {"shp", "dbf", "shx", "prj"}
    root, ext = os.path.splitext(file)
    return ext.replace('.', '') in shp_exts
