from dateutil.rrule import *

from datetime import date


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start_date = sorted(dates)[0]
    end_date = sorted(dates)[-1]
    
    difference = (end_date-start_date).days
    all_datimes = list(rrule(DAILY, count=difference, dtstart=start_date))
    all_dates = [x.date() for x in all_datimes]
    return list(set(all_dates).difference(dates))