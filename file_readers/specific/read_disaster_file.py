import logging

from file_readers.generic.generic_geospatial import generic_geospatial_files


def read_disaster_files(args, pars):
    print('Reading Disaster Files')
    logging.info('Reading Disaster Files')
    sbw_files = pars.get('sbws')
    lsr_files = pars.get('lsrs')
    sbws = generic_geospatial_files(sbw_files)
    lsrs = generic_geospatial_files(lsr_files)
    return sbws, lsrs


