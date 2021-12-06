import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc_aware = utc.replace(tzinfo=pytz.utc)

    localized_times = []

    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError('not a valid timezone')

        tz = pytz.timezone(tz)
        localized_times.append(utc_aware.astimezone(tz))

    return all(dt.hour in MEETING_HOURS for dt in localized_times)