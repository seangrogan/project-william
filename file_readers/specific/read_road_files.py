import concurrent.futures
import logging

from tqdm import tqdm

from file_readers.generic.generic_geospatial import generic_geospatial


def read_road_files(args, pars):
    print("Reading road files")
    if args.mp:
        return _read_road_files_mp(args, pars)
    else:
        return _read_road_files(args, pars)


def _read_road_files_mp(args, pars):
    """
    Parallel processes using concurrent.futures.ProcessPoolExecutor()
    :param pars: a list of shape file locations that are roads or some other indicators that make up where people are
    :return: the road points, a list of roads, each road has a list of points that make up the road.
    """
    logging.info("Reading road files, multiprocessing")
    files = pars.get("road_file", None)
    [logging.debug(f"Road File Passed {f}") for f in files]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(generic_geospatial, file)
                   for file in tqdm(files, desc='Reading Road Files', position=0, leave=True)]
        road_points = list()
        for result in concurrent.futures.as_completed(results):
            road_points += [road.get("shape").points
                            for road in tqdm(result.result(), desc="Processing Road Files", position=0, leave=True)]
    logging.info("Finished reading files")
    logging.debug(f"len={len(road_points)}")
    return road_points


def _read_road_files(args, pars):
    """
    :param pars: a list of shapefiles.
    :return: the road points, a list of roads, each road has a list of points that make up the road.
    """
    logging.info("Reading road files")
    files = pars.get("road_file", None)
    [logging.debug(f"Road File Passed {f}") for f in files]
    results = [generic_geospatial(file) for file in files]
    road_points = [road.get("shape").points for result in results for road in
                   tqdm(result, desc="Processing Road Files")]
    logging.info("finished reading files")
    logging.debug(f"len={len(road_points)}")
    return road_points
