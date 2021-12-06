from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or (NOW - date).total_seconds()<0:
        raise ValueError
    else:
    
        difference = (NOW - date).total_seconds()
        
    
        if difference>=2*DAY:
            return (date.strftime('%m/%d/%y'))
        if difference<0:
            return ValueError
        else:
            for offset in TIME_OFFSETS:

                if difference/offset[0]<1:
                    if offset[2]!=None:
                        t = offset[1].format(int(difference/offset[2]))
                        break
                    if offset[2] == None and offset[0] == MINUTE:
                        t = offset[1].format(int(difference))
                        break
                    else:
                        t = offset[1]
                        break
                    break
            return t
    
