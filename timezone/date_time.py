
import time
from datetime import datetime


def convert(logs_from_date, logs_upto_date):
    from_datetime = datetime.strptime(str(logs_from_date),
                                      "%m/%d/%Y")
    logs_from_ts = int(time.mktime(from_datetime.timetuple()))

    upto_datetime = datetime.strptime(str(logs_upto_date),
                                      "%m/%d/%Y")
    logs_upto_ts = int(time.mktime(
        upto_datetime.timetuple()))
    return logs_from_ts, logs_upto_ts


logs_from_date = "05/10/2019"
logs_upto_date = "08/11/2019"

from_ts, upto_ts = convert(logs_from_date, logs_upto_date)

print("{}={}, {}={}".format(
    logs_from_date, from_ts, logs_upto_date, upto_ts
))
