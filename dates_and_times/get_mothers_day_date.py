from datetime import date, datetime
from dateutil.rrule import *


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    m_year = datetime.strptime(str(year), '%Y').date()
    d_list = list(rrule(YEARLY, count=1, bymonth=5, byweekday=SU(2), dtstart=m_year))
    return d_list[0].date()