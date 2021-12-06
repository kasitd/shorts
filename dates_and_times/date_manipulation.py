from datetime import datetime, timedelta

SPECIAL_DATE = datetime(year=2016, month=12, day=19)


def gen_special_dates(step=timedelta(days=100)):
    date_list = []

    for i in range(1,20):
        if i%3 != 0:
            single_date = SPECIAL_DATE + i*step
            date_list.append(single_date)
        if i%3 == 0:
            single_date = SPECIAL_DATE + i * step
            date_list.append(single_date)
            bday = int(i / 3)
            date_list.append(SPECIAL_DATE + 3.65*bday*step)
    return sorted(date_list)