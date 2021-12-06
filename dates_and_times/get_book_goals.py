from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    
    if day_of_year == None:
        day_of_year = datetime.today().timetuple().tm_yday
   
    if books_read >= (books_goal/365)*day_of_year:
        return True
    else:
        return False