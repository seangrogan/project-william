import os


def shp_or_csv(file):
    if is_shp(file):
        return 'shp'
    if is_csv(file):
        return 'csv'
    return None


def is_csv(file):
    csv_exts = {"csv"}
    root, ext = os.path.splitext(file)
    return ext.replace('.', '') in csv_exts


def is_shp(file):
    shp_exts = {"shp", "dbf", "shx", "prj"}
    root, ext = os.path.splitext(file)
    return ext.replace('.', '') in shp_exts
