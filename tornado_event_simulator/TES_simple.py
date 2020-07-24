from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


from great_circle_calculator import great_circle_calculator as gcc
from tqdm import tqdm

from file_readers.generic.generic_geospatial import generic_geospatial

_tes_simple_parameters = {
    "radial_bins": 359,
    "distance_bins": None,
    "tornadoes_as_path": "D:/research/project-william/data/NWS/1950-2017-torn-aspath/1950-2017-torn-aspath.shp"
}


def TES_simple():
    """
    This function will generate tornadoes using simple distributions.  That is,
    we take a radial distribution of orientations, intensity, distance, width, and
    number of occurrences in a day.
    :return:
    """
    k = 0
    global _tes_simple_parameters
    tornadoes_as_path = generic_geospatial(_tes_simple_parameters["tornadoes_as_path"])
    tornadoes_as_path = [tornado for tornado in tornadoes_as_path if len(tornado['shape'].points) > 1]
    for tornado in tqdm(tornadoes_as_path, desc="Processing file"):
        """
        There are two kinds of zip files for each severe thunderstorm hazard: paths and initial points. 
        In the paths file, all tornadoes are converted into a LineString, 
        regardless of whether or not end point coordinates were provided. 
        To do this, if end point coordinates were not provided, the end point 
        coordinates were set to be +0.0001 degrees offset from the starting point. 
        This was done to be able to include all reports into a single file. 
        (Shpfiles only allow a single geometry type.) The initial points file 
        only includes the starting points of all events.
        """
        tornado["datetime"] = datetime.strptime(f'{tornado["date"]}T{tornado["time"]}', "%Y-%m-%dT%H:%M:%S")
        if len(tornado['shape'].points) <= 1:
            k += 1
            continue
        # if tornado['slat'] + 0.0001 == tornado['elat']:
        #     if tornado['slon'] + 0.0001 == tornado['elon']:
        #         continue
        tornado["direction"] = gcc.bearing_at_p1(tornado["shape"].points[0], tornado["shape"].points[-1])
        tornado["len_meters_calc"] = gcc.distance_between_points(tornado["shape"].points[0],
                                                                 tornado["shape"].points[-1])
        tornado["len_meters"] = tornado["len"] * 1609  # len in miles
        tornado["width_meters"] = tornado["wid"] * 0.9144  # Width in yards
    directions = [tornado["direction"] for tornado in tornadoes_as_path]
    lens = [tornado["len_meters"] for tornado in tornadoes_as_path]
    width = [tornado["width_meters"] for tornado in tornadoes_as_path]
    # directions = [d for d in directions if not 44 < d < 46]
    plt.hist(directions, _tes_simple_parameters.get('radial_bins'), density=True, facecolor='g', alpha=0.75)
    plt.xlabel('count')
    plt.ylabel('Direction')
    plt.title('Histogram')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.xlim(40, 160)
    # plt.ylim(0, 0.03)
    plt.grid(True)
    plt.show()
    return 0


if __name__ == '__main__':
    TES_simple()
