import csv
import os
from collections import Counter
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

from great_circle_calculator import great_circle_calculator as gcc
from tqdm import tqdm

from file_readers.generic.generic_geospatial import generic_geospatial

_tes_simple_parameters = {
    "radial_bins": 359,
    "distance_bins": None,
    "tornadoes_as_path": "D:/AcademicResearch/project-william/project-william/data/NWS/1950-2017-torn-aspath/1950-2017-torn-aspath.shp"
}


def TES_reader():
    """This reads the tornadoes as path file"""
    k = 0
    global _tes_simple_parameters
    tornadoes_as_path = generic_geospatial(_tes_simple_parameters["tornadoes_as_path"])
    eps = 0.01
    tornadoes_as_path = [tornado for tornado in tornadoes_as_path
                         if not tornado['slon'] + eps == tornado['elon'] and
                         not tornado['slat'] + eps == tornado['elat']]
    tornadoes_as_path = [tornado for tornado in tornadoes_as_path if len(tornado['shape'].points) > 1]
    for tornado in tqdm(tornadoes_as_path, desc="Processing file"):
        """
        There are two kinds of zip files for each severe thunderstorm hazard: paths and initial points. In the paths 
        file, all tornadoes are converted into a LineString, regardless of whether or not end point coordinates were 
        provided. To do this, if end point coordinates were not provided, the end point coordinates were set to be 
        +0.0001 degrees offset from the starting point. This was done to be able to include all reports into a single 
        file. (Shpfiles only allow a single geometry type.) The initial points file only includes the starting points 
        of all events.
        """
        tornado["datetime"] = datetime.strptime(f'{tornado["date"]}T{tornado["time"]}', "%Y-%m-%dT%H:%M:%S")
        tornado["direction"] = gcc.bearing_at_p1(tornado["shape"].points[0], tornado["shape"].points[-1])
        tornado["len_meters_calc"] = gcc.distance_between_points(tornado["shape"].points[0],
                                                                 tornado["shape"].points[-1])
        tornado["len_meters"] = tornado["len"] * 1609  # len in miles
        tornado["width_meters"] = tornado["wid"] * 0.9144  # Width in yards
    tornadoes_as_path = [tornado for tornado in tornadoes_as_path if round(tornado["direction"]) != 90]
    return tornadoes_as_path


class TornadoDataVisualizer:
    def __init__(self, tornadoes_as_path):
        self._tornadoes_as_path = tornadoes_as_path.copy()

    def magnitude_histogram(self):
        magnitude_counter = Counter([tornado['mag'] for tornado in self._tornadoes_as_path])
        magnitude_counter.pop(-9)
        mag, count = zip(*magnitude_counter.items())
        fig, ax = plt.subplots()
        ax.bar(mag, count)
        ax.set_xlabel("Magnitude")
        ax.set_ylabel("Count")
        ax.set_title("Tornado Magnitude Histogram")
        fig.show()

    def direction_histogram(self):
        fig, ax = plt.subplots()
        ax.grid(True)
        directions = [round(t.get("direction")) for t in self._tornadoes_as_path]
        directions = [abs(d) + 180 if d < 0 else d for d in directions]
        ax.hist(directions, bins=359)
        ax.set_xlabel("Direction")
        ax.set_ylabel("Count")
        ax.set_xticks(range(0, 360, 45))
        ax.set_title("Tornado Direction Histogram")
        fig.show()

    def direction_histogram_as_polar(self):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        directions = [round(t.get("direction")) for t in self._tornadoes_as_path]
        directions = [abs(d) + 180 if d < 0 else d for d in directions]
        direction_counter = Counter(directions)
        theta, radii = zip(*direction_counter.items())
        width = 1/90
        ax.bar(theta, radii, width=width)
        ax.set_theta_direction(-1)
        # ax.set_rlim(0)
        # ax.set_rscale('log')
        ax.set_title('log-polar matplotlib')
        ax.set_xlabel("Direction")
        ax.set_ylabel("Count")
        ax.set_title("Tornado Direction Histogram")
        ax.set_theta_zero_location("N")

        fig.show()


if __name__ == '__main__':
    print(f"Running... {os.path.basename(__file__)}")
    tornadoes = TES_reader()
    visualizer = TornadoDataVisualizer(tornadoes)
    visualizer.magnitude_histogram()
    visualizer.direction_histogram()
    visualizer.direction_histogram_as_polar()
    pass
