import logging

from file_readers.generic.generic_geospatial import generic_geospatial
from parameters.par_file_reader import par_file_reader
from utilities.my_logging_setup import setup_logging


def project_william():
    """
    This is the code for project william.
    :return:
    """
    print(f"Project William")
    logging.info("Running Project William")
    pars = par_file_reader()
    torn_as_path = generic_geospatial(pars["tornadoes_as_path"])
    lsrs = generic_geospatial(pars["LSR"])
    sbws = generic_geospatial(pars["SBW"])
    return 0


if __name__ == '__main__':
    setup_logging(project_name="ProjectWilliamOklahoma")
    project_william()
