
from datetime import datetime, timedelta
from pytz import timezone
import pytz


utc = pytz.utc
eastern = timezone('US/Eastern')
amsterdam = timezone('Europe/Amsterdam')
kathmandu = timezone('Asia/Kathmandu')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

loc_dt = kathmandu.localize(datetime(2002, 10, 27, 6, 0, 0))
# print loc_dt
# print loc_dt.strftime(fmt)

utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
loc_dt = utc_dt.astimezone(kathmandu)
print utc_dt
print loc_dt

print((loc_dt-utc_dt).total_seconds())