from datetime import datetime
from datetime import date
MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    times = []
    for reboot in reboots.strip().splitlines():
        extracted_time = ' '.join(reboot.split()[-4:])
        times.append(datetime.strptime(extracted_time, '%a %b %d %H:%M'))
    counter = 1
    deltas = []
    for time in times: 
        if counter < len(times):
            deltas.append(times[counter-1]-times[counter])
            counter+=1
    return max(deltas).days, '2021'+times[deltas.index(max(deltas))].strftime("-%m-%d")