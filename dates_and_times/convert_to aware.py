from pytz import timezone, UTC

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    
    utc_dt = naive_utc_dt.replace(tzinfo=UTC) #convert ot aware
    austalia_dt = utc_dt.astimezone(AUSTRALIA)    #convert to australia
    spain_dt = utc_dt.astimezone(SPAIN) #convert to spain
    return austalia_dt, spain_dt