from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    delta = timedelta()
    pattern = re.findall(r'\w{2,3}', delay_time)
    for el in pattern:

        if el[-1] == 'd':
            delta_d=int(re.findall(r'\d*', el)[0])
            delta+=timedelta(days=delta_d)
        
        if el[-1] == 'h':
            delta_h=int(re.findall(r'\d*', el)[0])
            delta+=timedelta(hours=delta_h)
            
        if el[-1]== 'm':
            delta_m=int(re.findall(r'\d*',el)[0])
            
            delta+=timedelta(minutes=delta_m)

        if el[-1]== 's' or not re.search(r'[a-z]', el[-1]):
             delta_s=int(re.findall(r'\d*',el)[0])
             delta+=timedelta(seconds=delta_s)
            
    return ('{} @ {}'.format(task, NOW+delta))