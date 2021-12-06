from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
       
    x = list(rrule(DAILY, count=+100, byweekday=(MO,TU,WE,TH,FR), dtstart=start_date))
    return [el.date() for el in x]