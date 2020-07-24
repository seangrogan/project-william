import datetime

import pytz


def time_parse(time_string, tzinfo=None):
    if tzinfo is None or tzinfo.lower() is 'utc':
        tzinfo = pytz.utc
    elif tzinfo.lower() in {'ok', 'oklahoma', 'america/chicago', 'chicago', 'central', 'cdt', 'cst'}:
        tzinfo = pytz.timezone('America/Chicago')
    else:
        tzinfo = pytz.timezone(tzinfo)
    if len(str(time_string)) == 14:
        d = datetime.datetime.strptime(str(time_string), '%Y%m%d%H%M%S')
    if len(str(time_string)) == 12:
        d = datetime.datetime.strptime(str(time_string), '%Y%m%d%H%M')
    if len(str(time_string)) == 10:
        d = datetime.datetime.strptime(str(time_string), '%Y%m%d%H')
    if len(str(time_string)) == 8:
        d = datetime.datetime.strptime(str(time_string), '%Y%m%d')
    d = tzinfo.localize(d)
    return d


def parse_time_tuple(time_tuple):
    if isinstance(time_tuple, datetime.datetime):
        return time_tuple
    assert len(time_tuple) == 2
    if isinstance(time_tuple, dict):
        t_str, tzinfo = time_tuple.get("time"), time_tuple.get("tz", 'utc')
    elif isinstance(time_tuple, list) or isinstance(time_tuple, tuple):
        t_str, tzinfo, *_ = time_tuple
    return time_parse(t_str, tzinfo)
