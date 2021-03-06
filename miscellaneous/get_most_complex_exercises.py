import csv
import os
from pathlib import Path
import re
from urllib.request import urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats) as f:
        reader = csv.reader(f, delimiter=';')
        # skip header
        next(reader)
        ret = sorted(reader,
                     key=lambda row: row[1] != 'None' and float(row[1]),
                     reverse=True)
        return [re.sub(r'Bite (\d+).*', r'\1', row[0]) for row in ret[:N]]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)