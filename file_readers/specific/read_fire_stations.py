import logging

from file_readers.generic.generic_geospatial import generic_geospatial_files


def fire_station_file_reader(args, pars, as_dict=False):
    files = pars.get('fire_stations')
    print('Reading Fire Station Files')
    logging.info('Reading Fire Station Files')
    stations = generic_geospatial_files(files)
    logging.debug(f"Read {len(stations)} fire stations")
    if as_dict:
        past = len(stations)
        stations = {station['name']: station for station in stations}
        if past != len(stations):
            logging.warning(f"Length of stations is inconsistent, "
                            f"we lost {past - len(stations)} "
                            f"stations converting it to a dict.")
            logging.warning(f"This is (probably) due to two stations having identical names"
                            f"Beware!")
    return stations

