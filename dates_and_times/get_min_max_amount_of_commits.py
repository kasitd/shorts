from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def _get_int(ins_del_str):
    return int(ins_del_str.split()[0])


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    res = Counter()
    with open(commits) as f:
        for line in f.readlines():
            date, stats = line.split('|')
            dt = parse(date.replace('Date:', '').strip())

            if year and dt.year != year:
                continue

            mods = stats.split(', ')
            if len(mods) == 3:
                _, inserts, deletes = mods
            else:
                # in this case we have only inserts or deletes
                if 'insert' in mods[1]:
                    _, inserts = mods
                    deletes = '0 deletions'
                else:
                    _, deletes = mods
                    inserts = '0 insertions'

            yymm = YEAR_MONTH.format(y=dt.year, m=dt.month)
            res[yymm] += _get_int(inserts) + _get_int(deletes)

        most_common = res.most_common()
        return most_common[-1][0], most_common[0][0]