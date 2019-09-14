import copy
from datetime import datetime
import pytz


def main():
    try:
        # Get utc & user's timezone time difference in minutes and adjust values for UI clock chart
        tz_user = pytz.timezone('Asia/Kathmandu')
        tz_utc = pytz.timezone('UTC')
        time_User = tz_user.localize(datetime(2002, 10, 27, 18, 26, 23))
        time_UTC = tz_utc.localize(datetime(2002, 10, 27, 18, 26, 23))
        time_diff = int(((time_UTC - time_User).total_seconds()) / 60)
        time_diff = time_diff - time_diff % 30
        time_diff = 30

        jsondata_value = {
            'value': [{'minute': i+2, 'expected': '%s-E' % i} for i in range(0, 1440, 30)]
        }

        per_halfhour_data = jsondata_value['value']
        per_halfhour_data_original = copy.deepcopy(jsondata_value['value'])
        if isinstance(per_halfhour_data, list):
            for per_halfhour_value in per_halfhour_data:
                new_time = per_halfhour_value['minute'] - time_diff
                if new_time >= 1440:
                    new_time = new_time - 1440
                if new_time < 0:
                    new_time = new_time + 1440

                per_halfhour_value['expected'] = per_halfhour_data_original[int(new_time) / 30]['expected']
                per_halfhour_value['minute'] = new_time
                print per_halfhour_value
    except Exception as ex:
        pass
        # print(str(ex))


if __name__=='__main__':
    main()