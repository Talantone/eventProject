import datetime

import pytz


def convert_tz():
    """Converts pytz timezones for Choices in Profile django model"""
    converted_tzs = [tz.split('/') for tz in pytz.common_timezones]
    tz_dict = {}

    for tz in converted_tzs:
        if len(tz) > 1:
            tz_dict.update({pytz.common_timezones[converted_tzs.index(tz)]: tz[1]})
        else:
            tz_dict.update({tz[0]: tz[0]})
    return [(k, v) for k, v in tz_dict.items()]


def time_to_tz_naive(dt, tz_in, tz_out):
    """Converts time to users timezone"""
    return tz_in.localize(datetime.datetime.combine(dt, dt.time())).astimezone(tz_out)

