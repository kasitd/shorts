from datetime import date
from operator import attrgetter
from typing import Dict, Sequence, NamedTuple, Counter


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    month_costs: Counter[str] = Counter()
    for movie in renting_history:
        date = movie.date
        key = f"{date.year}-{date.month}"
        month_costs[key] += movie.price

    return {
        ym: STREAM if cost > streaming_cost_per_month else RENT
        for ym, cost in month_costs.items()
    }