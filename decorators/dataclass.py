from dataclasses import dataclass
import datetime
import dateutil


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    a_born = datetime.datetime.strptime(actor.born, "%B %d, %Y")
    r_date = datetime.datetime.strptime(movie.release_date, "%B %d, %Y")
    age = int(((r_date-a_born).days)/365)
    return  '{} was {} years old when {} came out.'.format(actor.name, age, movie.title)