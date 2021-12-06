from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    return sorted(set([datetime.strptime(x, '%Y-%m-%d').date() for x in re.findall(r'(\d{4}-\d{2}-\d{2})', data)]), reverse=True)

def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    if (TODAY-dates[0]).days not in range(0,2):
        return 0
    else:
        deltas = [(dates[n]-dates[n+1]).days for n in range(len(dates)-1)]
    
        if all(1 == x for x in deltas):
            return len(deltas)+1
        else:
            for n, d in enumerate(deltas):
                if d != 1:
                    return n+1
                    break